import time
import urllib3
import concurrent.futures

from .type import BandProfile



class BandError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code

    def __repr__(self):
        return self.__name__ + f'<{self.status_code}>'


class Band:
    
    @staticmethod
    def get_profile(profile_url: str) -> BandProfile:
        while True:
            response = urllib3.request('GET', profile_url)
            status_code = response.status

            if status_code == 520:
                time.sleep(30)
                continue

            elif status_code != 200:
                raise BandError(status_code)
            
            break

        return BandProfile(profile_url, response.data)
    
    @staticmethod
    def _get_profile_thread(profile_url: str) -> tuple[BandProfile | None, str]:
        response = urllib3.request('GET', profile_url)
        status_code = response.status

        if status_code == 520:
            return None, profile_url

        elif status_code != 200:
            raise BandError(status_code)

        return BandProfile(profile_url, response.data), profile_url

    @classmethod
    def get_profiles(cls, profile_urls: list[str], segment_size=16, 
                     depth=0, max_depth=3) -> list[BandProfile]:
        profile_urls_swap = list()
        profiles = list()
        profile_urls_len = len(profile_urls)

        with concurrent.futures.ThreadPoolExecutor() as executor:

            # don't throw them all in at once
            for segment_start in range(0, profile_urls_len + segment_size, segment_size):
                segment_end = min(segment_start + segment_size, profile_urls_len)

                # feed the beast
                band_futures = (executor.submit(cls._get_profile_thread, url) 
                                for url in profile_urls[segment_start:segment_end])

                # examine the remains
                for future in concurrent.futures.as_completed(band_futures):
                    profile, profile_url = future.result()
                    if profile is None:
                        profile_urls_swap.append(profile_url)
                    else:
                        profiles.append(profile)

        # if there's any left, throw them back into the pit
        if len(profile_urls_swap) > 0 and max_depth > depth:
            profiles += cls.get_profiles(profile_urls_swap,
                                         segment_size=segment_size,
                                         depth=depth + 1, 
                                         max_depth=max_depth)
        
        return profiles
