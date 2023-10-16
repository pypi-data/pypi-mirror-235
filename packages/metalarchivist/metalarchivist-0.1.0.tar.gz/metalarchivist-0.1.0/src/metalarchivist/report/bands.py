from ..export import Band

import pandas as pd


def get_bands(profile_urls: list[str]) -> pd.DataFrame:
    band_profile = pd.DataFrame(Band.get_profiles(profile_urls))
    band_profile_desc = pd.DataFrame(list(band_profile['description']))

    return pd.concat([band_profile, band_profile_desc], axis=1)
