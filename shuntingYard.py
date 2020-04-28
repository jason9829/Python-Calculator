import arithmetic as ar
import stack as st
import stringInterpreter as sI
import operandToken as operandT
import operatorToken as operatorT
import myGlobal as myGlobal


# NOTE: The expression pass in are expected to have spaces between numbers and operators.
#       Will try to fix this bug soon. 5 Mar 2020
# Def: Calculate the expression using shunting yard algorithm with stack
# Param: operandStack, operatorStack, expression
# Retval: Calculated final answer operand token
def shuntingYard(operandStack, operatorStack, expression):
    if not sI.isAlphaInStr(expression):  # If there are alphabet in str, return the call
        # expression = sI.addSpaceBetweenCharacters(expression)  # Add space between character for splitting
        expressionList = expression.split()
        expressionListLength = len(expressionList)
        listIndex = 0
        previousToken = None
        endOfOperationFlag = False

    while not isOperationCompleted(expressionListLength, endOfOperationFlag):
        if expressionListLength != 0: token = createToken(listIndex, expressionList, previousToken)
        else: token.tokenType = "END_OF_OPERATION_TOKEN"

        if token.tokenType == "OPERAND_TOKEN":  # Directly push into the operand stack
            pushTokenToStack(token, operandStack, operatorStack)
            previousToken = token

        elif token.tokenType == "OPERATOR_TOKEN": # If the token type is operator
            if isStacksReadyForOperation(operandStack, operatorStack, token) == "NO":
                pushTokenToStack(token, operandStack, operatorStack)
                previousToken = token

            while isStacksReadyForOperation(operandStack, operatorStack, token) == "YES":
                calculateAnsAndPushToOperandStack(operandStack, operatorStack)
                pushTokenToStack(token, operandStack, operatorStack)
                previousToken = token
            while isStacksReadyForOperation(operandStack, operatorStack, token) == "SAME_PRECEDENCE":
                previousToken = handleSameAssociativityAndReturnToken(operandStack, operatorStack, token)


        else:
            calculateAnsAndPushToOperandStack(operandStack, operatorStack)
            expressionListLength += 1  # To offset the decrement later
        listIndex += 1
        expressionListLength -= 1

        if expressionListLength == 0 and len(operatorStack) == 0:
            endOfOperationFlag = True

    return st.popStack(operandStack)
"""
def shuntingYard(operandStack, operatorStack, expression):
    if not sI.isAlphaInStr(expression):  # If there are alphabet in str, return the call
        # expression = sI.addSpaceBetweenCharacters(expression)  # Add space between character for splitting
        expressionList = expression.split()
        expressionListLength = len(expressionList)
        listIndex = 0
        previousToken = None
        endOfOperationFlag = False

    while not isOperationCompleted(expressionListLength, endOfOperationFlag):
        if expressionListLength != 0: token = createToken(listIndex, expressionList, previousToken)
        else: token.tokenType = "END_OF_OPERATION_TOKEN"

        if token.tokenType == "OPERAND_TOKEN":  # Directly push into the operand stack
            pushTokenToStack(token, operandStack, operatorStack)
            previousToken = token

        elif token.tokenType == "OPERATOR_TOKEN": # If the token type is operator
            if len(operatorStack) == 0: # If the operator stack is empty then push to stack directly
                pushTokenToStack(token, operandStack, operatorStack)
                previousToken = token
            elif operatorT.isOperatorInStackHigherPrecedenceThanCurrentToken(operatorStack, token):
                if isNoOfTokensValidForOperation(operandStack, operatorStack):
                    calculateAnsAndPushToOperandStack(operandStack, operatorStack)
                    pushTokenToStack(token, operandStack, operatorStack)
                    previousToken = token
                    if expressionListLength == 0 and len(operatorStack) == 0:
                        endOfOperationFlag = True

            elif operatorT.isOperatorInStackSamePrecedenceWithCurrentToken(operatorStack, token):
                previousToken = handleSameAssociativityAndReturnToken(operandStack, operatorStack, token)

            else:
                pushTokenToStack(token, operandStack, operatorStack)
                previousToken = token
        else:
            #if operatorT.isOperatorInStackSamePrecedenceWithCurrentToken(operatorStack, token):
            #    previousToken = handleSameAssociativityAndReturnToken(operandStack, operatorStack, token)
            #else:
            calculateAnsAndPushToOperandStack(operandStack, operatorStack)
            if expressionListLength == 0 and len(operatorStack) == 0:
                endOfOperationFlag = True
            expressionListLength += 1 # To offset the decrement later
        listIndex += 1
        expressionListLength -= 1

    return st.popStack(operandStack)

"""



# Desc: Verify whether the operation is completed
# Param: expression list length, endOfOperationFlag
# Retval: True/ False
def isOperationCompleted(expressionListLength, endOfOperationFlag):
    if expressionListLength == 0:
        if endOfOperationFlag:
            return True
        else:
            return False
    else:
        return False


# Desc: Verify the operator in the str
# Param: Str (non alphabet)
# Retval: True/ False
"""
def isOperatorInExpressionValid(expression):
    FIRST_CHAR_FLAG = True
    expressionLen = len(expression)
    
    while expressionLen != 0:   # Loop until end of str
        if ()
        expressionLen -= 1
        FIRST_CHAR_FLAG = False

"""


# Desc: Verify the expression before processing it
# Param: Expression
# Retval: True/ raise
def isExpressionValid(expression):
    if sI.isAlphaInStr(expression):
        return False
    else:
        return True


# Desc: Get the char from operand or operator token
# Param: Token
# Retval: Char
def getCharFromToken(token):
    if not token is None:
        if token.tokenType == "OPERAND_TOKEN":
            return str(token.num)
        elif token.tokenType == "OPERATOR_TOKEN":
            return token.symbol
    else:  # If token is None
        return None


# NOTE: Use when the token are extract from list
# Desc: Create and push operand or operator token to respective stack
# Param: listIndex, expressionList, operandStack, operatorStack, previousToken
# Retval: Token

def createAndPushTokenToStack(listIndex, expressionList, operandStack, operatorStack, previousToken):
    currentChar = expressionList[listIndex]
    if sI.isNumber(currentChar):  # formatNumber(number)
        token = operandT.createOperandToken(sI.formatNumber(sI.stringToNumber(currentChar)))
        st.pushStack(operandStack, token)
    elif sI.isOperator(currentChar):  # Raise exception when non operator detected
        token = operatorT.createOperatorToken(operatorT.getOperatorStrAffix(getCharFromToken(previousToken),
                                                                            expressionList[listIndex + 1],
                                                                            currentChar))
        st.pushStack(operatorStack, token)
    return token


# Desc: Create operand or operator token and return the token
# Param: listIndex, expressionList, operandStack, operatorStack, previousToken
# Retval: Token
def createToken(listIndex, expressionList, previousToken):
    currentChar = expressionList[listIndex]
    if sI.isNumber(currentChar):  # formatNumber(number)
        token = operandT.createOperandToken(sI.formatNumber(sI.stringToNumber(currentChar)))
    elif sI.isOperator(currentChar):  # Raise exception when non operator detected, required next char to check get
        # affix
        token = operatorT.createOperatorToken(operatorT.getOperatorStrAffix(getCharFromToken(previousToken),
                                                                            expressionList[listIndex + 1],
                                                                            currentChar))
    return token


# Desc: Push token to respective stack
# Param: Token, operandStack, operatorStack
# Desc: Pop the operand and operator to do the calculation
def pushTokenToStack(token, operandStack, operatorStack):
    if token.tokenType == "OPERATOR_TOKEN":
        st.pushStack(operatorStack, token)

    elif token.tokenType == "OPERAND_TOKEN":
        st.pushStack(operandStack, token)


# Desc: Calculate operand with operator in respective stack and return the answer token
# Param: Operand stack, operator stack
# Retval: Operand token (w/ calculated ans)
def calculateAndReturnAnsToken(operandStack, operatorStack):
    num2Token = st.popStack(operandStack)   # Pop the second operand for calculation (FILO)
    num1Token = st.popStack(operandStack)   # Pop the first operand for calculation (FILO)
    operator = st.popStack(operatorStack)   # Pop the operator for calculation
    ans = ar.calculationBasedOnOperator(num1Token.num, num2Token.num, operator.symbol) # Get the calculated ans
    token = operandT.createOperandToken(sI.formatNumber(ans)) # Create the operand token based on calculated ans
    return token


# Desc: Calculate operand with operator in respective stack, then push back the operand answer
# Param: Operand stack, operator stack
# Retval: None
def calculateAnsAndPushToOperandStack(operandStack, operatorStack):
    st.pushStack(operandStack, calculateAndReturnAnsToken(operandStack, operatorStack))


# Desc: Check if number of tokens in respective stack is enough for operation
# Param: Operand stack, operator stack
# Retval: True/ False
def isNoOfTokensValidForOperation(operandStack, operatorStack):
    if len(operandStack) >= 2 and len(operatorStack) >= 1:
        return True
    else:
        return False


# Desc: Perform the actions when the operator stack's head operator and token's associativity are same
# Param: Operand stack, operator stack, token
# Retval: Token that pass in, to ease the update at main function
def handleSameAssociativityAndReturnToken(operandStack, operatorStack, token):
    if token.associativity == operatorStack[len(operatorStack) - 1].associativity:
        if token.associativity == myGlobal.LEFT_TO_RIGHT: # LTR, perform left operation first
            calculateAnsAndPushToOperandStack(operandStack, operatorStack)
            pushTokenToStack(token, operandStack, operatorStack)

        else: # RTL, perform right operation first, or no associativity
            pushTokenToStack(token, operandStack, operatorStack)

    return token


# Desc: Perform the operations when all the token are pushed
# Param: Operand stack, operator stack
# Retval: Operated token
def operateAfterAllTokenPushed(operandStack, operatorStack):
    sizeOfOperatorStack = len(operatorStack)
    

# Desc: Check if the tokens in respective stack is ready for operation
#       Check for no of tokens and operator precedence
# Param: Operand stack, operator stack, token
# Retval: YES, NO, SAME_PRECEDENCE
def isStacksReadyForOperation(operandStack, operatorStack, token):
    if isNoOfTokensValidForOperation(operandStack, operatorStack) and \
            operatorT.isOperatorInStackHigherPrecedenceThanCurrentToken(operatorStack, token):
       return "YES"

    elif operatorT.isOperatorInStackSamePrecedenceWithCurrentToken(operatorStack, token):
            if isNoOfTokensValidForOperation(operandStack, operatorStack):
                return "SAME_PRECEDENCE_AND_READY"
            else:
                return "SAME_PRECEDENCE_BUT_XREADY"

    else:
        return "NO"
