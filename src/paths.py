from pathlib import Path


def get_path_via_home(*subdirs):
    user_home_path = Path().home()

    if subdirs:
        return user_home_path.joinpath(subdirs)
    else:
        return user_home_path
