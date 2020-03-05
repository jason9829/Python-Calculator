

# NOTE: The float str acquisition terminate by operator symbol or end of str
#       Caller can use isAlphaInStr before passing the parameter
# Desc: Extract float in str
# Param: Str
# Retval: Float in str
def extractFloatStr(expression):
    FIRST_DECIMAL_DETECTED = False
    END_FLAG = False
    newExpression = ""
    expressionLen = len(expression)
    indexNo = 0

    while not END_FLAG: # Toggle when the terminating condition meet (return function call)
        if expressionLen != 0:  # When it's not the end of str
            if expression[indexNo].isdigit():   # If it's digit
                newExpression += expression[indexNo]    # Copy to new object
            elif (expression[indexNo] == '.') & (not FIRST_DECIMAL_DETECTED):   # Decimal point detected, and if
                FIRST_DECIMAL_DETECTED = True                                   # no decimal point detected before
                newExpression += expression[indexNo]
            elif isOperator(expression[indexNo]):   # If operating symbol found, terminate the process and return
                END_FLAG = True
            expressionLen -= 1
            indexNo += 1
        else:
            END_FLAG = True
    return newExpression


# WARNING: Will not work for decimal point value
# Desc: Add space between characters of the string
#       (will not add if there are already space between character)
# Param: Expression to add spaces
# Retval: Expression with spaces between characters
def addSpaceBetweenCharacters(expression):
    elementNo = 0
    tempNo = 1
    expressionCopy = expression
    expressionLength = len(expression)
    while expressionLength != 1:    # Last character no need to check/ add
        if (expression[elementNo +1] != ' ') & (not isFloat(expression[elementNo] + expression[elementNo + 1])):
            expressionCopy = insertCharactersInString(' ', expressionCopy, elementNo +tempNo)    # Update the new string
            tempNo += 1
            elementNo += 1
        expressionLength -= 1
    return expressionCopy


# Desc: Add space between characters of math expression
#       (will not add if there are already space between character)
# Param: Math expression to add spaces
# Retval: Math expression with spaces between characters
def addSpaceBetweenMathCharacters(expression):
    FIRST_CHARACTER_FLAG = True
    elementNo = 0
    tempNo = 1
    expressionCopy = expression
    expressionLength = len(expression)
    while expressionLength != 0:    # Last character no need to check/ add

        expressionLength -= 1
    return expressionCopy


# Decs: Insert string/ character at the specified location (index)
# Param: String/ character to add, Original string, index
# Retval: New string with added string/ character
# Ref: https://stackoverflow.com/questions/5254445/add-string-in-a-certain-position-in-python
def insertCharactersInString(characters, expression, index):
    return expression[:index] + characters + expression[index:]


# Desc: Check whether the string is number (int/ double/ float)
# Param: String
# Retval: True/ False
# Ref: https://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float/354130
def isNumber(expression):
    try:
        float(expression)
        return True
    except ValueError:
        return False


# Desc: Check whether the character is a operator for calculations
# Param: Character
# Retval: True/ False
def isOperator(expression):
    operatorList = ('+', '-', '*', '/', '(', ')')
    if len(expression) > 1:  # Return false when string is received
        return False
    elif not type(expression) == str:  # Return false when non character is received
        return False
    else:  # Find whether parameter is match with operatorList, if yes then return True, else return false
        index = 0
        listLength = len(operatorList)
        while listLength != 0:
            if expression == operatorList[index]:
                return True
            else:
                index += 1
                listLength -= 1

        return False


# Desc: Convert String to Number
# Param: String
# Retval: Number (int or float)
def stringToNumber(expression):
    if isNumber(expression):
        return float(expression)
    else:
        raise ValueError("Exception: stringToNumber() received invalid parameter to be convert.")


# Desc: Remove the decimal point if there's 0 after decimal point, etc 1.0-> 1
# Param: Number to be formatted
# Retval: Formatted number
# Ref: https://stackoverflow.com/questions/38282697/how-can-i-remove-0-of-float-numbers
def formatNumber(num):
    if num % 1 == 0:  # Example: 4.0 % 1 = 0, 4.1 % 1 = 0.1
        return int(num)
    else:
        return num


# Desc: Detect whether it' float
# Param: String
# Retval: True/ False
def isFloat(expression):
    floatStr = extractFloatStr(expression)
    Num = formatNumber(stringToNumber(floatStr))
    if type(Num) == int:
        return False
    else:
        return True


# Desc: Move String to right (like moving pointer in c)
# Param: String, iteration to move the str
# Retval: Moved String
def moveStr(expression, iteration):
    newExpression = ""
    expressionLength = len(expression)
    noOfIterations = expressionLength - iteration
    while noOfIterations != 0:
        newExpression += expression[iteration]
        iteration += 1
        noOfIterations -= 1
    return newExpression


# Desc: Check whether there's alphabet in a str
# Param: String
# Retval: True/ False
# Ref: https://stackoverflow.com/questions/15558392/how-to-check-if-character-in-string-is-a-letter-python
def isAlphaInStr(expression):
    for char in expression:
        if char.isalpha():
            return True

    return False


# Desc: Extract token from string
# Param: String
# Retval: Token
# def getTokenFromStr(expression):
