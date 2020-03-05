import arithmetic as ar
import stack as st
import stringInterpreter as sI
import operandToken as operandT
import operatorToken as operatorT


# NOTE: The expression pass in are expected to have spaces between numbers and operators.
#       Will try to fix this bug soon. 5 Mar 2020
# Def: Calculate the expression using shunting yard algorithm with stack
# Param: operandStack, operatorStack, expression
# Retval: Calculated final answer
def shuntingYard(operandStack, operatorStack, expression):
    if not sI.isAlphaInStr(expression):  # If there are alphabet in str, return the call
        # expression = sI.addSpaceBetweenCharacters(expression)  # Add space between character for splitting
        expressionList = expression.split()
        expressionListLength = len(expressionList)
        listIndex = 0
        previousToken = None

    while expressionListLength != 0:
        currentChar = expressionList[listIndex]
        if sI.isNumber(currentChar):  # formatNumber(number)
            token = operandT.createOperandToken(sI.formatNumber(sI.stringToNumber(currentChar)))
            st.pushStack(operandStack, token)
        elif sI.isOperator(currentChar):  # Raise exception when non operator detected
            token = operatorT.createOperatorToken(operatorT.getOperatorStrAffix(str(previousToken.num),
                                                                                expressionList[listIndex + 1],
                                                                                currentChar))
            st.pushStack(operatorStack, token)
        listIndex += 1
        expressionListLength -= 1
        previousToken = token

    num2Token = st.popStack(operandStack)
    num1Token = st.popStack(operandStack)
    operator = st.popStack(operatorStack)
    ans = ar.calculationBasedOnOperator(num1Token.num, num2Token.num, operator.symbol)
    st.pushStack(operandStack, ans)
    return st.popStack(operandStack)


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
# Retval: True/ raise exception (false)
def isExpressionValid(expression):
    if sI.isAlphaInStr(expression):
        return False
    else:
        return True
