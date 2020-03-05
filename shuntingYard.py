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
    if sI.isAlphaInStr(expression): # If the
        #expression = sI.addSpaceBetweenCharacters(expression)  # Add space between character for splitting
        expressionList = expression.split()
        expressionListLength = len(expressionList)
        listIndex = 0

    while expressionListLength != 0:
        currentToken = expressionList[listIndex]
        if sI.isNumber(currentToken):  # formatNumber(number)
            st.pushStack(operandStack, operandT.createOperandToken(sI.formatNumber(sI.stringToNumber(currentToken))))
        elif sI.isOperator(currentToken):  # Raise exception when non operator detected
            st.pushStack(operatorStack, operatorT.createOperatorToken(currentToken))
        listIndex += 1
        expressionListLength -= 1

    num2 = st.popStack(operandStack)
    num1 = st.popStack(operandStack)
    operator = st.popStack(operatorStack)
    ans = ar.calculationBasedOnOperator(num1, num2, operator)
    st.pushStack(operandStack, ans)
    return st.popStack(operandStack)


# Desc: Verify the expression before processing it
# Param: Expression
# Retval: True/ raise exception (false)
def isExpressionValid(expression):
    if sI.isAlphaInStr(expression):
        raise ValueError("Error: isExpressionValid() received invalid expression.")
    else:
        return True