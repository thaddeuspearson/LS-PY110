"""
Write a function that takes a floating point number representing an angle
between 0 and 360 degrees and returns a string representing that angle in
degrees, minutes, and seconds. You should use a degree symbol (°) to
represent degrees, a single quote (') to represent minutes, and a double
quote (") to represent seconds. There are 60 minutes in a degree, and 60
seconds in a minute.
"""
import sys


DEGREE = "\u00B0"


def dms(angle=None):
    """Returns the degrees, minutes, and seconds of the given angle.

    :param angle (float): the angle
    :returns (str): formatted string giving degree, minutes, and seconds
    """
    if angle is None:
        angle = input("Enter a float representing the degree of an angle: ")

    minute = (angle - int(angle)) * 60
    second = (minute - int(minute)) * 60
    return f"{int(angle)}{DEGREE}{int(minute):02}'{int(second):02}\""


# pylint: disable=pointless-string-statement
"""CODE EXPLANATION
dms is defined on line 15, and accepts a single parameter, angle. The
conditional block on line 21 checks to see if angle has an argument provided,
and if not, promts the user to input one.

On line 24, the local variable minute is instantiaed to the decimal portion
of angle and multiploied by 60. On line 25, a local variable second is
instantiated to the decimal portion of minute and multiplied by 60.

On line 26, the properly formatted string is returned using string
interpolation with padding where necessary.
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
