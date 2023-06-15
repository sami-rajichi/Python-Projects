# Compute whether the given year is a leap year.

###################################################
# Is leapyear formula
# Student should enter function on the next lines.
def is_leap_year(y):
    """
    Returns whether the given Gregorian year is a leap year.
    """	
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True 
    return False 


###################################################
# Tests
# Student should not change this code.

def test(year):
    """Tests the is_leapyear function."""
    if is_leap_year(year):
        print year, "is a leap year."
    else:
        print year, "is not a leap year."

test(2000)
test(1996)
test(1800)
test(2013)

###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#2000 is a leap year.
#1996 is a leap year.
#1800 is not a leap year.
#2013 is not a leap year.
