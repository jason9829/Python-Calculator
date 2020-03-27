import myGlobal as dictConstant
import stringInterpreter as sI


class OperatorToken:
    def __init__(self):
        self.symbol = None
        self.associativity = None
        self.precedence = None
        self.affix = None
        self.tokenType = None


# Ref: https://en.cppreference.com/w/c/language/operator_precedence
#      https://github.com/jason9829/ShuntingYard/blob/master/src/OperatorPrecedence_wTable.c
#    : https://tinyurl.com/rm4elpd
operatorDict = {"INFIX_PLUS": (dictConstant.LEFT_TO_RIGHT, dictConstant.WEAK),
                "INFIX_MINUS": (dictConstant.LEFT_TO_RIGHT, dictConstant.WEAK),
                "INFIX_MULTIPLY": (dictConstant.LEFT_TO_RIGHT, dictConstant.MEDIUM),
                "INFIX_DIVIDE": (dictConstant.LEFT_TO_RIGHT, dictConstant.MEDIUM),
                "PREFIX_PLUS": (dictConstant.RIGHT_TO_LEFT, dictConstant.STRONG),
                "PREFIX_MINUS": (dictConstant.RIGHT_TO_LEFT, dictConstant.STRONG),
                "OPEN_BRACKET": (dictConstant.LEFT_TO_RIGHT, dictConstant.WEAK),
                "CLOSE_BRACKET": (dictConstant.LEFT_TO_RIGHT, dictConstant.WEAK)
                }

operatorSymbolSwitch = {
    "INFIX_PLUS": '+',
    "INFIX_MINUS": '-',
    "INFIX_MULTIPLY": '*',
    "INFIX_DIVIDE": '/',
    "PREFIX_PLUS": '+',
    "PREFIX_MINUS": '-',
    "OPEN_BRACKET": '(',
    "CLOSE_BRACKET": ')',
}

operatorStrVerifySwitch = {
    "INFIX_PLUS": True,
    "INFIX_MINUS": True,
    "INFIX_MULTIPLY": True,
    "INFIX_DIVIDE": True,
    "PREFIX_PLUS": True,
    "PREFIX_MINUS": True,
    "OPEN_BRACKET": True,
    "CLOSE_BRACKET": True,
}


# Desc: Verify the operator in str
# Param: Operator in str
# Retval: True/ False
def isOperatorStrValid(operatorStr):
    return operatorStrVerifySwitch.get(operatorStr, False)


# Desc: Convert operator in str (Affix) to operator symbol
# Param: Operator in str
# Retval: Operator symbol
def getOperatorSymbol(operatorStr):
    return operatorSymbolSwitch.get(operatorStr, "Error: getOperatorSymbol() received invalid operator string.")


# Desc: Get operator info from operatorDict
# Param: Operator in str (Key in operatorDict)
# Retval: Value of key in operatorDict(associativity, affix, precedence)
def getOperatorTokenInfo(operatorStr):
    return operatorDict.get(operatorStr)


# Desc: Generate operator token
# Param: Operator in str (Key in operatorDict)
# Retval: Operator token
def createOperatorToken(operatorStr):
    if not isOperatorStrValid(operatorStr):  # operator str is invalid, raise exception
        raise ValueError("Error: createOperatorToken() received invalid operator str.")

    tokenInfo = getOperatorTokenInfo(operatorStr)
    token = OperatorToken()
    token.associativity = tokenInfo[dictConstant.Associativity]
    token.precedence = tokenInfo[dictConstant.Precedence]
    token.symbol = getOperatorSymbol(operatorStr)
    token.affix = getAffixFromOperatorStr(operatorStr)
    token.tokenType = "OPERATOR_TOKEN"
    return token


# Desc: Determine the affix for '+' sign with previous and next char
# Param: Previous char, next char
# Retval: '+' sign operator str
def getPlusSignOperatorStr(previousChar, nextChar):
    if (previousChar is None) & sI.isNumber(nextChar):
        return "PREFIX_PLUS"
    if (previousChar is None) & sI.isOperator(nextChar):
        return "PREFIX_PLUS"
    elif sI.isNumber(previousChar) | sI.isNumber(nextChar):
        return "INFIX_PLUS"


# Desc: Determine the affix for '-' sign with previous and next char
# Param: Previous char, next char
# Retval: '-' sign operator str
def getMinusSignOperatorStr(previousChar, nextChar):
    if (previousChar is None) & sI.isNumber(nextChar):
        return "PREFIX_MINUS"
    if (previousChar is None) & sI.isOperator(nextChar):
        return "PREFIX_MINUS"
    elif sI.isNumber(previousChar) | sI.isNumber(nextChar):
        return "INFIX_MINUS"


# Dict for operator affix function call/ return str
# When function search for the keyword (key), function (value)
#                       {key: value}
operatorAffixDict = {'+': getPlusSignOperatorStr,
                     '-': getMinusSignOperatorStr,
                     '*': "INFIX_MULTIPLY",
                     '/': "INFIX_DIVIDE",
                     '(': "OPEN_BRACKET",
                     ')': "CLOSE_BRACKET"
                     }


# NOTE: Caller must verify the operator symbol before call the funciton
# Desc: Determine the operator affix with previous and next character
# Param: Previous char, next char, operator
# Retval: Operator str
def getOperatorStrAffix(previousChar, nextChar, operatorSymbol):
    if (operatorSymbol == '+') | (operatorSymbol == '-'):
        return operatorAffixDict[operatorSymbol](previousChar, nextChar)
        #                             [Key]    (param1, param2)
    else:
        return operatorAffixDict[operatorSymbol]


# Desc: Extract affix from operator str
# Param: Operator str
# Retval: Affix
def getAffixFromOperatorStr(operatorStr):
    if "PREFIX" in operatorStr:
        return "PREFIX"
    elif "INFIX" in operatorStr:
        return "INFIX"


# Desc: Check if operator token in operator stack has higher precedence than current token
# Param: Operator stack, current token
# Retval: True/ False
def isOperatorTokenReadyToPush(operatorStack, token):
    stackLen = len(operatorStack)
    if not stackLen == 0:  # If the stack is not empty
        # If token's precedence is higher
        if operatorStack[stackLen-1].precedence < token.precedence or \
            operatorStack[stackLen - 1].precedence == token.precedence: # Same precedence
            return True
        else:  # If token's precedence is lower
            return False
    else:  # Stack is empty
        return True

