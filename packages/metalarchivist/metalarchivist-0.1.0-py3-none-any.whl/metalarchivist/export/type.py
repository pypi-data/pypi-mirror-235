
import re

from enum import StrEnum, auto
from datetime import datetime
from dataclasses import dataclass, field, InitVar

import lxml.html


def normalize_keyword_casing(dictionary: dict):
    def normalize_to_snakecase(match: re.Match):
        preceding_text = match.group(1)
        text = match.group(2).lower()

        if preceding_text == '':
            return text

        return f'{preceding_text}_{text}'

    camel_case = re.compile(r'(\b|[a-z])([A-Z])')

    return {camel_case.sub(normalize_to_snakecase, k): v
            for k, v in dictionary.items()}


class MetalArchivesDirectory:

    @staticmethod
    def upcoming_releases(echo=0, display_start=0, display_length=100,
                          from_date=datetime.now().strftime('%Y-%m-%d'), 
                          to_date='0000-00-00'):

        return (f'https://www.metal-archives.com/release/ajax-upcoming/json/1'
                f'?sEcho={echo}&iDisplayStart={display_start}&iDisplayLength={display_length}'
                f'&fromDate={from_date}&toDate={to_date}')


class InvalidAttributeError(Exception):
    ...


@dataclass
class BandLink:
    name: str = field(init=False)
    link: str = field(init=False)

    def __init__(self, html: str):
        html_anchor = lxml.html.fragment_fromstring(html)
        self.name = html_anchor.text
        self.link = html_anchor.attrib['href']


@dataclass
class AlbumLink:
    name: str = field(init=False)
    link: str = field(init=False)

    def __init__(self, html: str):
        html_anchor = lxml.html.fragment_fromstring(html)
        self.name = html_anchor.text
        self.link = html_anchor.attrib['href']


class GenrePeriod(StrEnum):
    EARLY = auto()
    MID = auto()
    LATER = auto()
    ALL = auto()
    ERROR = auto()

    @classmethod
    def has_value(cls, value) -> set:
        return value in cls._value2member_map_


class GenreJunk(StrEnum):
    METAL = auto()
    ELEMENTS = auto()
    INFLUENCES = auto()
    MUSIC = auto()
    AND = auto()
    WITH = auto()

    @classmethod
    def has_value(cls, value) -> bool:
        return value.lower() in cls._value2member_map_


@dataclass(frozen=True)
class GenrePhase:
    name: str
    period: GenrePeriod = field(default=GenrePeriod.ALL)


@dataclass
class Genres:
    """ Handle genres specified in text assuming 
        the conventions applied by metal-archives.com
        
        Phases: separated by semicolons (;), denotes a change
            in a bands sound over a series of periods wrapped in
            parentheses, *early*, *mid*, and *later*. See `GenrePhase`.

            *e.g* Doom Metal (early); Post-Rock (later)

        Multiples: A slash (/) indicates that a band fits within
            multiple genres. Phases are subdivided into multiples,
            where applicable. Bands without phases will likewise
            contain multiples.

            *e.g* Drone/Doom Metal (early); Psychedelic/Post-Rock (later),
                Progressive Death/Black Metal

        Modifiers: A genre can be modified into a variant with descriptive
            text, delimited by a space ( ).

            *e.g* Progressive Death Metal

        Junk: Words that are largely uninformative can be removed, the most
            common being "Metal". See `GenreJunk`.

            *e.g* Symphonic Gothic Metal with Folk influences
    """

    full_genre: str
    clean_genre: str = field(init=False)
    phases: list[GenrePhase] = field(init=False)

    def __post_init__(self):
        # scrub anomalies
        clean_genre = re.sub(' Metal', '', self.full_genre)
        clean_genre = re.sub(r'\u200b', '', clean_genre)
        clean_genre = re.sub(chr(1089), chr(99), clean_genre)
        clean_genre = re.sub(r'(\w)\(', r'\g<1> (', clean_genre)
        clean_genre = re.sub(r'\)\/? ', r'); ', clean_genre)
        clean_genre = re.sub(r' \- ', ' ', clean_genre)

        phases = clean_genre.split(';')

        # strip and use regex to parse genre phase components
        phases = list(map(self._parse_phase, map(str.lstrip, phases)))

        # explode strings into multiple records by character
        phases = self._explode_phases_on_delimiter(phases, '/')
        phases = self._explode_phases_on_delimiter(phases, ',')

        # remove meaningless text
        phases = self._scrub_phases_of_junk(phases)

        # convert genres that appear in all phases to a single ALL record
        phases = self._collapse_recurrent_phases(phases)

        self.phases = phases = list(set(phases))
        sorted_genres = sorted(phases, key=self._phase_sort_key)
        self.clean_genre = ', '.join(map(lambda n: n.name, sorted_genres))

    @staticmethod
    def _phase_sort_key(phase: GenrePhase):
        return (GenrePeriod._member_names_.index(phase.period.name), phase.name)

    @staticmethod
    def _collapse_recurrent_phases(phases: list[GenrePhase]) -> list[GenrePhase]:
        total_phases = len(set(map(lambda n: n.period, phases)))

        phase_counts = dict()
        for phase in phases:
            try:
                phase_counts[phase.name] += 1
            except KeyError:
                phase_counts[phase.name] = 1

        consistent_genres = set(g for g, c in phase_counts.items() if c == total_phases)
        collapsed_phases = list(map(GenrePhase, consistent_genres)) 
        collapsed_phases += list(filter(lambda p: p.name not in consistent_genres, phases))

        return collapsed_phases

    @staticmethod
    def _scrub_phases_of_junk(phases: list[GenrePhase]) -> list[GenrePhase]:
        def scrub(phase):
            return [GenrePhase(p, phase.period)
                    for p in phase.name.split(' ')
                    if not GenreJunk.has_value(p)]
        
        return sum(list(map(scrub, phases)), [])

    @staticmethod
    def _explode_phases_on_delimiter(phases: list[GenrePhase], delimiter: str) -> list[GenrePhase]:
        def explode(phase):
            return [GenrePhase(n.strip(), phase.period) for n in phase.name.split(delimiter)]
            
        return sum(list(map(explode, phases)), [])

    @staticmethod
    def _parse_phase(phase: str) -> GenrePhase:
        phase_match = re.compile(r'^(?P<name>.*?)(\((?P<period>[\w\/\, ]+)\))?$').match(phase)
        
        phase_record = phase_match.groupdict() if phase_match else dict(name=phase, period='all')
        try:
            period = phase_record['period']
            phase_record['period'] = GenrePeriod[period.upper()] if period else GenrePeriod.ALL
        except KeyError:
            phase_record['period'] = GenrePeriod.ERROR

        return GenrePhase(**phase_record)


@dataclass
class AlbumRelease:    
    band: BandLink
    album: AlbumLink

    release_type: str
    genres: Genres
    release_date_display: InitVar[str]
    added_date_display: InitVar[str]

    release_date: datetime = field(init=False)
    added_date: datetime | None = field(init=False)

    def __post_init__(self, release_date_display, added_date_display):
        release_date = re.sub(r',', '', release_date_display)
        release_date = re.sub(r'(\d)st', r'\g<1>', release_date)
        release_date = re.sub(r'(\d)nd', r'\g<1>', release_date)
        release_date = re.sub(r'(\d)rd', r'\g<1>', release_date)
        release_date = re.sub(r'(\d)th', r'\g<1>', release_date)
        release_date = re.sub(r'\s(\d)\s', r' 0\g<1> ', release_date)

        release_date_parsed = self._try_parse_release_date(release_date, '%B %d %Y')
        if not release_date_parsed:
            release_date_parsed = self._try_parse_release_date(release_date, '%B %Y')

        self.release_date = release_date_parsed

        if added_date_display == 'N/A':
            added_date = None
        else:
            added_date = re.sub(r'\/(\d)\/', '/0\1/', added_date_display)
            self.added_date = datetime.strptime(added_date, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def _try_parse_release_date(release_date: str, date_format: str):
        try:
            return datetime.strptime(release_date, date_format)
        except ValueError:
            return None


@dataclass
class ReleasePage:
    total_records: int = field(init=False)
    total_display_records: int = field(init=False)
    echo: int = field(init=False)
    data: list[AlbumRelease] = field(init=False)

    def __init__(self, i_total_records: int, i_total_display_records: int,
                 s_echo: int, aa_data: list):

        self.total_records = i_total_records
        self.total_display_records = i_total_display_records
        self.echo = s_echo
        self.data = sum(list(map(self._process_album_release, aa_data)), [])

    def __add__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError('ReleasePage objects can only be summed '
                            'with other ReleasePage objects')

        self.data += other.data
        return self
    
    @staticmethod
    def _process_album_release(record: list[str]) -> list[AlbumRelease]:
        """ returns a list to handle the potential for splits """

        band_link, album_link, release_type, genres, *dates = record

        if re.search(r'>\s?\/\s?<', band_link):
            band_links = band_link.split(' / ')
            genre_list = genres.split(' | ')

            return [AlbumRelease(BandLink(link), AlbumLink(album_link), 
                                 release_type, Genres(genre), *dates)
                    for link, genre in zip(band_links, genre_list)]

        return [AlbumRelease(BandLink(band_link), AlbumLink(album_link), 
                             release_type, Genres(genres), *dates)]


class ReleasePages(list):
    def combine(self) -> ReleasePage:
        first_page, *remaining = self
        return sum(remaining, start=first_page)


@dataclass(frozen=True)
class BandMember:
    alias: str
    role: str
    profile: str = field(hash=True)


@dataclass(frozen=True)
class BandDescription:
    country_of_origin: str = field(kw_only=True)
    location: str = field(kw_only=True)
    status: str = field(kw_only=True)
    formed_in: str = field(kw_only=True)
    genre: str = field(kw_only=True)
    themes: str = field(kw_only=True, default=None)
    lyrical_themes: str = field(kw_only=True, default=None)
    years_active: str = field(kw_only=True)
    last_label: str = field(kw_only=True, default=None)
    current_label: str = field(kw_only=True, default=None)


@dataclass
class BandProfile:
    url: str
    html: InitVar[bytes]
    
    name: str = field(init=False)
    metallum_id: str = field(init=False)
    lineup: dict[str, list[BandMember]] = field(init=False)
    description: BandDescription = field(init=False)


    def __post_init__(self, profile_html: bytes):
        self.metallum_id = int(self.url.split('/')[-1])

        profile_document = lxml.html.document_fromstring(profile_html)
        profile_band_name_xpath = '//h1[@class="band_name"]/a/text()'
        self.name = profile_document.xpath(profile_band_name_xpath).pop()


        lineup = self._parse_lineup(profile_document)
        if len(lineup) == 0:
            lineup = self._parse_lineup(profile_document, all_members=False)
        
        self.lineup = lineup

        desc_titles = profile_document.xpath('//div[@id="band_stats"]/dl/dt//text()')
        desc_detail_xpath = '//div[@id="band_stats"]/dl/dt/following-sibling::dd//text()'
        desc_detail = profile_document.xpath(desc_detail_xpath)
        
        self.description = self._parse_description(desc_titles, desc_detail)

    @staticmethod
    def _parse_lineup(profile_document, all_members=True) -> dict[str, list[BandMember]]:
        member_selection = 'band_tab_members_all' if all_members else 'band_tab_members_current'
        lineup_tablerows_xpath = (f'//div[@id="{member_selection}"]'
                                  f'//table[contains(@class, "lineupTable")]'
                                  f'//tr[@class="lineupHeaders" or @class="lineupRow"]')
        
        lineup_tablerows = profile_document.xpath(lineup_tablerows_xpath)

        lineup = dict()
        current_section = None if all_members else 'Current'

        for tablerow in lineup_tablerows:
            
            if tablerow.attrib['class'] == 'lineupHeaders':
                current_section = tablerow.xpath('td/text()').pop().strip()
            
            elif tablerow.attrib['class'] == 'lineupRow':
                member_profile_anchor = tablerow.xpath('td[1]/a').pop()
                member_alias = member_profile_anchor.text.strip()
                member_profile = member_profile_anchor.attrib['href']

                member_role = tablerow.xpath('td[2]/text()').pop() \
                                      .strip().replace('\xa0', ' ')

                member = BandMember(member_alias, member_role, member_profile)

                try:
                    lineup[current_section].append(member)
                except KeyError:
                    lineup[current_section] = [member]
            
            else:
                raise InvalidAttributeError
            
        return lineup



    @staticmethod
    def _parse_description(description_titles, description_details) -> BandDescription:
        description = {str(dt).lower(): str(dd).strip() 
                       for dt, dd in zip(description_titles, description_details)}
        
        # scrub non alpha and whitespace
        description = {re.sub(r'[^\w\s]+', '', dt): None if dd == 'N/A' else dd 
                       for dt, dd in description.items()}
        
        # underscores
        description = {re.sub(r'\s+', '_', dt): dd
                       for dt, dd in description.items()}

        return BandDescription(**description)
    
@dataclass
class AlbumTrack:
    number: int
    title: str
    length: str


@dataclass
class AlbumDescription:
    release_type: str
    release_date: str
    catalog_id: str
    label: str
    media_format: str
    version_desc: str | None = field(default=None)
    limitation: str | None = field(default=None)
    reviews: str | None = field(default=None)


@dataclass
class AlbumProfile:
    url: str
    html: InitVar[bytes]

    name: str = field(init=False)
    metallum_id: int = field(init=False)
    tracklist: list[AlbumTrack] = field(init=False)
    description: AlbumDescription = field(init=False)

    def __post_init__(self, profile_html):
        self.metallum_id = int(self.url.split('/')[-1])

        profile_document = lxml.html.document_fromstring(profile_html)
        album_desc_titles_xpath = '//div[@id="album_info"]/dl/dt/text()'
        album_desc_titles = profile_document.xpath(album_desc_titles_xpath)

        album_desc_detail_xpath = '//div[@id="album_info"]/dl/dd/text()'
        album_desc_detail = profile_document.xpath(album_desc_detail_xpath)

        self.description = self._parse_description(album_desc_titles, album_desc_detail)

    @classmethod
    def _parse_description(cls, description_titles, description_details) -> AlbumDescription:
        description = {str(dt).lower(): str(dd).strip() 
                       for dt, dd in zip(description_titles, description_details)}
        
        # scrub non alpha and whitespace
        description = {re.sub(r'[^\w\s]+', '', dt): None if dd == 'N/A' else dd 
                       for dt, dd in description.items()}
        
        # underscores
        description = {re.sub(r'\s+', '_', dt): dd
                       for dt, dd in description.items()}
        
        # scrub invalid key names
        description = {cls._scrub_key_names(dt): dd
                       for dt, dd in description.items()}

        return AlbumDescription(**description)
    
    @staticmethod
    def _scrub_key_names(key: str) -> str:
        if key == 'type':
            return 'release_type'

        if key == 'format':
            return 'media_format'

        return key
