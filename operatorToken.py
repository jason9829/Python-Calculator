import myGlobal as dictConstant


class OperatorToken:
    def __init__ (self):
        self.symbol = None
        self.associativity = None
        self.precedence = None


# Ref: https://en.cppreference.com/w/c/language/operator_precedence
#      https://github.com/jason9829/ShuntingYard/blob/master/src/OperatorPrecedence_wTable.c
#    : https://tinyurl.com/rm4elpd
operatorDict = {"INFIX_PLUS": (dictConstant.LEFT_TO_RIGHT, dictConstant.WEAK),
                "INFIX_MINUS": (dictConstant.LEFT_TO_RIGHT, dictConstant.WEAK),
                "INFIX_MULTIPLY": (dictConstant.LEFT_TO_RIGHT, dictConstant.MEDIUM),
                "INFIX_DIVIDE": (dictConstant.LEFT_TO_RIGHT, dictConstant.MEDIUM),
                "PREFIX_ADD": (dictConstant.RIGHT_TO_LEFT, dictConstant.STRONG),
                "PREFIX_MINUS": (dictConstant.RIGHT_TO_LEFT, dictConstant.STRONG),
                "OPEN_BRACKET": (dictConstant.LEFT_TO_RIGHT, dictConstant.WEAK),
                "CLOSE_BRACKET": (dictConstant.LEFT_TO_RIGHT, dictConstant.WEAK)
                }


operatorSymbolSwitch = {
                    "INFIX_PLUS": '+',
                    "INFIX_MINUS": '-',
                    "INFIX_MULTIPLY": '*',
                    "INFIX_DIVIDE": '/',
                    "PREFIX_ADD": '+',
                    "PREFIX_MINUS": '-',
                    "OPEN_BRACKET": '(',
                    "CLOSE_BRACKET": ')',
}

operatorStrVerifySwitch = {
    "INFIX_PLUS": True,
    "INFIX_MINUS": True,
    "INFIX_MULTIPLY": True,
    "INFIX_DIVIDE": True,
    "PREFIX_ADD": True,
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
    return token