"""
Write a function that takes a floating point number representing an angle
between 0 and 360 degrees and returns a string representing that angle in
degrees, minutes, and seconds. You should use a degree symbol (°) to
represent degrees, a single quote (') to represent minutes, and a double
quote (") to represent seconds. There are 60 minutes in a degree, and 60
seconds in a minute.
"""
import sys


def dms():
    pass


# pylint: disable=pointless-string-statement
"""CODE EXPLAINATION

"""


# Test Cases
if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "test":
        assert dms(30) == "30°00'00\""
        assert dms(76.73) == "76°43'48\""
        assert dms(254.6) == "254°35'59\""
        assert dms(93.034773) == "93°02'05\""
        assert dms(0) == "0°00'00\""
        assert dms(360) == "360°00'00\"" or dms(360) == "0°00'00\""
    else:
        print(dms()) 
