
# Assignment 1

# Aviv Yefet
# ID:208495267

# Q1
# if one of the parameters is not a float we were asked printing "Error: parameters should be float"
# if the denominator is zero we were asked to return a string "Not a number – denominator equals zero"
def my_func(x1, x2, x3):
    if isinstance(x1, float) and isinstance(x2, float) and isinstance(x3, float):
        denom = x1+x2+x3
        if denom == 0:
            return "Not a number – denominator equals zero"
        else:
            numer = denom*(x2+x3)*x3
            return numer/denom
    else:
        print("Error: parameters should be float")

# Tests Q1
# print(my_func(1.0, 7.0, 9.0))            # expected: 144.0
# my_func(1, 1.0, 2.5)                     # expected: "Error: parameters should be float"
# print(my_func(1.0,-2.0,1.0))             # expected: "Not a number – denominator equals zero"


#Q2
# the function gets two positive parameters (must be float or int)
# the function return float or int value depending on input types
def convert(hours, minutes):
    if (isinstance(hours, float) or isinstance(hours, int)) and (isinstance(minutes, float) or isinstance(minutes, int)):
        if hours >= 0 and minutes >= 0:
            hours_to_sec = hours * 60 * 60
            minutes_to_sec = minutes*60
            return hours_to_sec+minutes_to_sec
        else:
            return "Input error!"
    else:
        return "Input error!"

# Tests Q2
# print(convert(1,3))                      # expected: 3780
# print(convert(1.75, 30))                 # expected: 8100.0
# print(convert(1, 45))                    # expected: 6300

