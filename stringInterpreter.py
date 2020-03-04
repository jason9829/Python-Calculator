

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
        if expression[elementNo+1] != ' ':
            expressionCopy = insertCharactersInString(' ', expressionCopy, elementNo+tempNo)
            tempNo += 1
            elementNo += 1
        expressionLength -= 1
    return expressionCopy


# Decs: Insert string/ character at the specified location (index)
# Param: String/ character to add, Original string, index
# Retval: New string with added string/ character
# Ref: https://stackoverflow.com/questions/5254445/add-string-in-a-certain-position-in-python
def insertCharactersInString(characters, expression, index):
    return expression[:index] + characters + expression[index:]
