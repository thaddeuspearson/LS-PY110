"""
Some people believe that Fridays that fall on the 13th day of the month are
unlucky days. Write a function that takes a year as an argument and returns
the number of Friday the 13ths in that year. You may assume that the year is
greater than 1752, which is when the United Kingdom adopted the modern
Gregorian Calendar. You may also assume that the same calendar will remain in
use for the foreseeable future.

P
    inputs: int
    outputs: int
    rules:
        Explicit Reqs:
            - accept an int
            - return an int
            - return int is the number of fri 13ths in the year
        Implicit Reqs:
            - the given year is after 1752
E
    friday_the_13ths(1986) == 1
    friday_the_13ths(2015) == 3
    friday_the_13ths(2017) == 2
D
    list
A
    - create a months list
    - loop through months of the year
    - create a datetime object for each 13th day
    - check if the day is a friday
        - if it is append to a months list
    - return the length of months list
C
"""
import sys
from datetime import datetime


def friday_the_13ths(year: int) -> int:
    """Returns the number of friday-the-13ths in the given year"""
    friday_13_months = [
        month for month in range(1, 13)
        if datetime(year, month, 13).strftime('%A') == "Friday"
    ]
    return len(friday_13_months)


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
Implementation Level:

On line 38, friday_the_13ths is defined with a single parameter, year,
which expects an int representing the year.

On line 40, a list comprehension is assigned to the local variable
friday_13_months. The comprehension loops through the months of the year
(in int represenation), creates a datetime object and uses strftime to get the
day of the week, checks this against the string literal "Friday" and appends
the month to the comprehension accordingly.

On line 44, the len of friday_13_months is returned.


User Level:

Friday_the_13ths takes a given year after 1752, and returns the number of
Friday the 13ths that occur in that given year using a list comprehension
and leveraging the datetime module.
"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert friday_the_13ths(1986) == 1
        assert friday_the_13ths(2015) == 3
        assert friday_the_13ths(2017) == 2
