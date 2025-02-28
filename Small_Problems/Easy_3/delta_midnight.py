"""
As seen in the previous exercise, the time of day can be represented as the
number of minutes before or after midnight. If the number of minutes is
positive, the time is after midnight. If the number of minutes is negative,
the time is before midnight.

Write a function that takes a time of day in 24 hour format, and an additional
parameter before_or_after and return the number of minutes before or after
midnight, respectively. The function should return a value in the range 0
through 1439.

You may not use Python's datetime module.
"""
import sys


def delta_midnight(timestamp: str, before_or_after: str) -> int:
    """Returns the number of minutes the timestamp is before or after midnight

    :param timestamp (str): the timestamp to analyze
    :param before_or_after (str): "before"/"after"
    :returns delta (int): the number of minutes before or after midnight
    """
    hour, minute = timestamp.split(":")
    total_mins = int(hour) * 60 + int(minute)
    delta = (1440 - total_mins) if before_or_after == "before" else total_mins
    return delta % 1440


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
delta_midnight is defined on line 11. It has 2 parameters, timestamp and
before_or_after, both of which are strings.

On line 18, timestamp is unpacked to two lcoal variables, hour and minute,
using the split method.
Another local variable total_mins is calculated on line 19 by coercing hour
to it's integer representation and multiplying it by 60, and then adding the
integer representation of minute.

The local variable delta is defined on line 20, and its calculation either
subtracts its total from 1440, or assigns it directly to total_mins depending
on the value of before_or_after.

Finally, delta is returned after a mod 1440 operation to bring the return
value within the correct range of 0 and 1439.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert delta_midnight("00:00", "after") == 0
        assert delta_midnight("00:00", "before") == 0
        assert delta_midnight("12:34", "after") == 754
        assert delta_midnight("12:34", "before") == 686
        assert delta_midnight("24:00", "after") == 0
        assert delta_midnight("24:00", "before") == 0
