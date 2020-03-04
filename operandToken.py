

# Desc: Remove the decimal point if there's 0 after decimal point, etc 1.0-> 1
# Param: Number to be formatted
# Retval: Formatted number
# Ref: https://stackoverflow.com/questions/38282697/how-can-i-remove-0-of-float-numbers
def formatNumber(num):
    if num % 1 == 0:  # Example: 4.0 % 1 = 0, 4.1 % 1 = 0.1
        return int(num)
    else:
        return num