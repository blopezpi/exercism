import datetime


class Clock:
    def __init__(self, hour, minute):
        now = datetime.datetime.now()
        from_midnigth = datetime.datetime(year=now.year, month=now.month,
                                          day=now.day, hour=0, minute=0)
        self.date = from_midnigth + datetime.timedelta(hours=hour,
                                                       minutes=minute)
        self.time = self.date.time()

    def __repr__(self):
        return self.time.strftime("%H:%M")

    def __eq__(self, other):
        return self.time == other

    def __add__(self, minutes):
        new_time = self.date + datetime.timedelta(minutes=minutes)
        return new_time.strftime("%H:%M")

    def __sub__(self, minutes):
        new_time = self.date - datetime.timedelta(minutes=minutes)
        return new_time.strftime("%H:%M")
