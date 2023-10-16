from ..export import Releases

import pandas as pd


def get_releases(range_start=None, range_stop=None):
    if range_start:
        release_page = Releases.get_range(range_start, range_stop)
    else:
        release_page = Releases.get_upcoming()

    release = pd.DataFrame(release_page.data)
    band = pd.DataFrame(list(release['band']))
    band = band.rename(columns=dict(name='band', link='profile_url'))

    album = pd.DataFrame(list(release['album']))
    album = album.rename(columns=dict(name='album', link='album_url'))

    genres = pd.DataFrame(list(release['genres']))
    genres = genres.rename(columns=dict(phases_display='cleaned_genre'))
    genres = genres.drop(['phases'], axis=1)

    release = release.drop(['band', 'album', 'genres'], axis=1)

    return pd.concat([band, album, genres, release], axis=1)
