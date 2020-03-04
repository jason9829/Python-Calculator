import myGlobal as dictConstant

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


# def: Get operator info from operatorDict
# Param: Operator in str (Key in operatorDict)
# Retval: Value of key in operatorDict(associativity, affix, precedence)
def getOperatorTokenInfo(operatorStr):
    return operatorDict.get(operatorStr)

