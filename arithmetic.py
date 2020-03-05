

# Desc: Add two numbers and return the result
# Param: Numbers to be added (num1 + num2)
# Retval: Added result
def additionOf2Numbers(num1, num2):
    return num1 + num2


# Desc: Subract two numbers and return the result
# Param: Numbers to be subtract from (num1 - num2)
# Retval: Subtracted result
def subtractionOf2Numbers(num1, num2):
    return num1 - num2


# Desc: Multiply two numbers and return the result
# Param: Numbers to be multiplied (num1 * num2)
# Retval: Multiplied result
def multiplicationOf2Numbers(num1, num2):
    return num1 * num2


# Desc: Divide two numbers and return the result
# Param: Numbers to be divided (num1 / num2)
# Retval: Divided result
def divisionOf2Numbers(num1, num2):
    return num1 / num2


# Dict for arithmetic function call
# When function search for the keyword (key), function (value)
#                       {key: value}
arithmeticFuntionDict = {'+': additionOf2Numbers,
                         '-': subtractionOf2Numbers,
                         '*': multiplicationOf2Numbers,
                         '/': divisionOf2Numbers,
                         }


# Desc: Do the calculation between two numbers based on operator character
# Retval: Num1, Num2, Operator character
# Retval: Calculated answer
def calculationBasedOnOperator(num1, num2, operator):
    try:
        return arithmeticFuntionDict[operator](num1, num2)
        #                             [Key]    (param1, param2)
    except ValueError:
        raise ValueError("Error: calculationBasedOnOperator() invalid operator received.")
