import stringInterpreter as sI


class OperandToken:
    def __init__(self):
        self.num = None
        self.numType = None
        self.tokenType = None


# Desc: Determine whether the number is int/ float
# Param: Number (value), won't raise error if it's not number (caller need to raise the exception)
# Retval: int or float
def getNumberType(number):
    if type(number) == int:
        return "int"
    else:
        return "float"


# Desc: Generate operand token
# Param: Operand in str
# Retval: Operand token
def createOperandToken(operandStr):
    if not sI.isNumber(operandStr):  # Verify whether the parameter str is number
        # Raise exception if parameter is not number
        raise ValueError("Error: createOperandToken() received invalid operand str.")
    # Convert str to number, then format the numbe (remove decimal if it's int)
    token = OperandToken()
    token.num = sI.formatNumber(sI.stringToNumber(operandStr))
    token.numType = getNumberType(token.num)
    token.tokenType = "OPERAND_TOKEN"
    return token


