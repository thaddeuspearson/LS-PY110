"""
The time of day can be represented as the number of minutes before or after
midnight. If the number of minutes is positive, the time is after midnight. If
the number of minutes is negative, the time is before midnight.

Write a function that takes a time using this minute-based format and returns
the time of day in 24-hour format (hh:mm). Your function should work with any
integer input.

You may not use Python's datetime module.
"""
import sys


MIN_IN_A_DAY = 1440


def time_of_day(delta: int) -> str:
    """Gives thetime of day from the given delta from midnight.

    :param delta (int): the number of minutes away from midnight
    :returns (str): the formatted time (HH:MM)
    """
    delta %= MIN_IN_A_DAY
    hour = int(delta / 60)
    minute = delta % 60
    return f"{hour:02d}:{minute:02d}"


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
time_of_day is defined on line 18, and has one parameter, delta. On line 24,
delta is reduced by the modulo operation, resulting in the number of minutes
being within the range of 0 and 1439 to acount for the minutes in a day.

On lines 25 and 26, two local variables hour and minute are instantiated
respectfully, hour to the result of dividing delta by 60 and coercing to its
int representation, and minute assigned to the result of mod 60.

The final result string is returned on line 27, and leverages string
interpolation, coupled with leading 0 padding.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert time_of_day(0) == "00:00"
        assert time_of_day(-3) == "23:57"
        assert time_of_day(35) == "00:35"
        assert time_of_day(-1437) == "00:03"
        assert time_of_day(3000) == "02:00"
        assert time_of_day(800) == "13:20"
        assert time_of_day(-4231) == "01:29"
