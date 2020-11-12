import datetime


def convert_time(time_string, fmt="%Y%m%d-%H%M%S"):
    # 仅ORM使用，
    return datetime.datetime.strptime(time_string, fmt)
