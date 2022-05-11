from enum import Enum


class Frequency(Enum):
    """ Frequency of events. """
    NO_FREQUENCY = -1       # null frequency
    ONCE = 0                # only once, e.g., a zero - coupon
    ANNUAL = 1              # once a year
    SEMIANNUAL = 2          # twice a year
    EVERY_FOURTH_MONTH = 3  # every fourth month
    QUARTERLY = 4           # every third month
    BIMONTHLY = 6           # every second month
    MONTHLY = 12            # once a month
    EVERY_FOURTH_WEEK = 13  # every fourth week
    BIWEEKLY = 26           # every second week
    WEEKLY = 52             # once a week
    DAILY = 365             # once a day
    OTHER_FREQUENCY = 999   # some other unknown frequency
