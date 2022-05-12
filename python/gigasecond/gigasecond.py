from datetime import timedelta, datetime

def add(moment: datetime) -> datetime:
    """
    Add a gigasecond to a datetime.
    :param moment: The datetime to add a gigasecond to.
    :return: The datetime after the gigasecond has been added.
    """
    return moment + timedelta(seconds=1_000_000_000)