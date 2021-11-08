import enum

class WeekDay(enum.IntEnum):
    MONDAY: int
    TUESDAY: int
    WEDNESDAY: int
    THURSDAY: int
    FRIDAY: int
    SATURDAY: int
    SUNDAY: int
    @classmethod
    def get_weekday_number(cls, week_day_str): ...
