import unittest
import operatorToken as operatorT
import myGlobal as dictConstant
import stack

class TestCaseIsOperatorStrValid(unittest.TestCase):
    def test_a_isOperatorStrValid_given_PREFIX_MINUS_expect_true(self):
        # verifyOperatorStr(operatorStr)
        self.assertEqual(True, operatorT.isOperatorStrValid("PREFIX_MINUS"))

    def test_b_isOperatorStrValid_given_INFIX_MULTIPLY_expect_true(self):
        # verifyOperatorStr(operatorStr)
        self.assertEqual(True, operatorT.isOperatorStrValid("INFIX_MULTIPLY"))

    def test_c_isOperatorStrValid_given_INFIX_OR_expect_false(self):
        # verifyOperatorStr(operatorStr)
        self.assertEqual(False, operatorT.isOperatorStrValid("INFIX_OR"))


class TestCaseGetOperatorSymbol(unittest.TestCase):
    def test_a_getOperatorSymbol_given_INFIX_PLUS_expect_plus_sign(self):
        # getOperatorSymbol(operatorStr)
        self.assertEqual('+', operatorT.getOperatorSymbol("INFIX_PLUS"))

    def test_b_getOperatorSymbol_given_CLOSE_BRACKET_expect_close_bracket_sign(self):
        # getOperatorSymbol(operatorStr)
        self.assertEqual(')', operatorT.getOperatorSymbol("CLOSE_BRACKET"))

    def test_c_getOperatorSymbol_given_AND_expect_error_message(self):
        # getOperatorSymbol(operatorStr)
        self.assertEqual("Error: getOperatorSymbol() received invalid operator string.",
                         operatorT.getOperatorSymbol("AND"))


class TestCaseGetOperatorTokenInfo(unittest.TestCase):
    def test_a_getOperatorTokenInfo_given_INFIX_PLUS_expect_LEFT_TO_RIGHT_WEAK(self):
        """
        From myGlobal.py
        Associativity: LEFT_TO_RIGHT = 4
        Precedence: WEAK = 10
        """
        # getOperatorTokenInfo(operatorStr)
        tokenInfo = operatorT.getOperatorTokenInfo("INFIX_PLUS")
        self.assertEqual(dictConstant.LEFT_TO_RIGHT, tokenInfo[dictConstant.Associativity])
        self.assertEqual(dictConstant.WEAK, tokenInfo[dictConstant.Precedence])

    def test_b_getOperatorTokenInfo_given_PREFIX_MINUS_expect_RIGHT_TO_LEFT_STRONG(self):
        """
        From myGlobal.py
        Associativity: RIGHT_TO_LEFT = 5
        Precedence: STRONG = 12
        """
        # getOperatorTokenInfo(operatorStr)
        tokenInfo = operatorT.getOperatorTokenInfo("PREFIX_MINUS")
        self.assertEqual(dictConstant.RIGHT_TO_LEFT, tokenInfo[dictConstant.Associativity])
        self.assertEqual(dictConstant.STRONG, tokenInfo[dictConstant.Precedence])

    def test_c_getOperatorTokenInfo_given_invalid_operator_expect_None(self):
        # getOperatorTokenInfo(operatorStr)
        tokenInfo = operatorT.getOperatorTokenInfo("!")
        self.assertEqual(None, tokenInfo)


class TestCaseCreateOperatorToken(unittest.TestCase):
    def test_a_createOperatorToken_given_INFIX_DIVIDE_expect_return_token_with_correct_info(self):
        """
        From myGlobal.py
        Associativity: LEFT_TO_RIGHT = 4
        Precedence: MEDIUM = 11
        """
        # createOperatorToken(operatorStr)
        operatorToken = operatorT.createOperatorToken("INFIX_DIVIDE")
        self.assertEqual(dictConstant.LEFT_TO_RIGHT, operatorToken.associativity)
        self.assertEqual(dictConstant.MEDIUM, operatorToken.precedence)
        self.assertEqual('/', operatorToken.symbol)
        self.assertEqual("OPERATOR_TOKEN", operatorToken.tokenType)

    def test_b_createOperatorToken_given_OPEN_BRACKET_expect_return_token_with_correct_info(self):
        """
        From myGlobal.py
        Associativity: LEFT_TO_RIGHT = 4
        Precedence: WEAK = 10
        """
        # createOperatorToken(operatorStr)
        operatorToken = operatorT.createOperatorToken("OPEN_BRACKET")
        self.assertEqual(dictConstant.LEFT_TO_RIGHT, operatorToken.associativity)
        self.assertEqual(dictConstant.WEAK, operatorToken.precedence)
        self.assertEqual('(', operatorToken.symbol)
        self.assertEqual("OPERATOR_TOKEN", operatorToken.tokenType)

    def test_c_createOperatorToken_given_CURLY_BRACKET_expect_exception_raised(self):
        try:                        # createOperatorToken(operatorStr)
            operatorToken = operatorT.createOperatorToken("CURLY_BRACKET")
            self.assertEqual(None, operatorToken.associativity)
            self.assertEqual(None,  operatorToken.precedence)
            self.assertEqual(None, operatorToken.symbol)
            self.assertEqual("OPERATOR_TOKEN", operatorToken.tokenType)

        except Exception as e:
            print(e)


class TestCaseGetOperatorSignAffixStr(unittest.TestCase):
    def test_a_getPlusSignOperatorStr_given_prev_None_next_minus_expect_PREFIX_PLUS(self):
        # getPlusSignOperatorStr(previousChar, nextChar)
        self.assertEqual("PREFIX_PLUS", operatorT.getPlusSignOperatorStr(None, "-"))

    def test_b_getPlusSignOperatorStr_given_prev_1_next_4_expect_INFIX_PLUS(self):
        # getPlusSignOperatorStr(previousChar, nextChar)
        self.assertEqual("INFIX_PLUS", operatorT.getPlusSignOperatorStr("1", "4"))

    def test_c_getPlusSignOperatorStr_given_prev_None_next_1_expect_PREFIX_PLUS(self):
        # getPlusSignOperatorStr(previousChar, nextChar)
        self.assertEqual("PREFIX_PLUS", operatorT.getPlusSignOperatorStr(None, "1"))
    # Didn't test for getMinusSignOperatorStr() because the code are same as getPlusSignOperatorStr()

    def test_d_getOperatorStrAffix_given_prev_None_next_1_minus_expect_PREFIX_MINUS(self):
        # getOperatorStrAffix(previousChar, nextChar, operatorSymbol)
        self.assertEqual("PREFIX_MINUS", operatorT.getOperatorStrAffix(None, "1", "-"))

    def test_e_getOperatorStrAffix_given_prev_1_next_6point11_plus_expect_INFIX_PLUS(self):
        # getOperatorStrAffix(previousChar, nextChar, operatorSymbol)
        self.assertEqual("INFIX_PLUS", operatorT.getOperatorStrAffix("1", "6.11", "+"))

    def test_f_getOperatorStrAffix_given_prev_None_next_None_multiply_expect_INFIX_MULTIPLY(self):
        # getOperatorStrAffix(previousChar, nextChar, operatorSymbol)
        self.assertEqual("INFIX_MULTIPLY", operatorT.getOperatorStrAffix(None, None, "*"))

    def test_g_getOperatorStrAffix_given_prev_10_next_6point11_divide_expect_INFIX_DIVIDE(self):
        # getOperatorStrAffix(previousChar, nextChar, operatorSymbol)
        self.assertEqual("INFIX_DIVIDE", operatorT.getOperatorStrAffix("10", "6.11", "/"))

    def test_h_getOperatorStrAffix_given_prev_None_next_None_open_bracket_expect_OPEN_BRACKET(self):
        # getOperatorStrAffix(previousChar, nextChar, operatorSymbol)
        self.assertEqual("OPEN_BRACKET", operatorT.getOperatorStrAffix(None, None, "("))

    def test_i_getOperatorStrAffix_given_prev_10_next_6point11_close_bracket_expect_CLOSE_BRACKET(self):
        # getOperatorStrAffix(previousChar, nextChar, operatorSymbol)
        self.assertEqual("CLOSE_BRACKET", operatorT.getOperatorStrAffix("10", "6.11", ")"))

    def test_j_getAffixFromOperatorStr_given_PREFIX_MINUS_expect_PREFIX(self):
        # getAffixFromOperatorStr(operatorStr)
        self.assertEqual("PREFIX", operatorT.getAffixFromOperatorStr("PREFIX_PLUS"))

    def test_k_getAffixFromOperatorStr_given_INFIX_DIVIDE_expect_INFIX(self):
        # getAffixFromOperatorStr(operatorStr)
        self.assertEqual("INFIX", operatorT.getAffixFromOperatorStr("INFIX_DIVIDE"))


class TestIsOperatorInStackHigherPrecedence(unittest.TestCase):
    def test_a_isOperatorInStackHigherPrecedence_given_prefix_plus_at_stack_and_infix_plus_as_token_expect_true(self):
        operatorStack = []  # Initialise operator stack

        # Initialise operator token to insert to stack
        operatorToken = operatorT.OperatorToken()
        operatorToken.associativity = dictConstant.RIGHT_TO_LEFT
        operatorToken.precedence = dictConstant.STRONG
        operatorToken.symbol = '+'
        operatorToken.affix = "PREFIX"
        operatorToken.tokenType = "OPERATOR_TOKEN"

        # Initialise current token
        currentToken = operatorT.OperatorToken()
        currentToken.associativity = dictConstant.LEFT_TO_RIGHT
        currentToken.precedence = dictConstant.WEAK
        currentToken.symbol = '+'
        currentToken.affix = "INFIX"
        currentToken.tokenType = "OPERATOR_TOKEN"
        # Push operator token into stack
        stack.pushStack(operatorStack, operatorToken)
        # isOperatorInStackHigherPrecedence(operatorStack, token)
        self.assertEqual(True, operatorT.isOperatorInStackHigherPrecedence(operatorStack, currentToken))

    def test_b_isOperatorInStackHigherPrecedence_given_empty_stack_expect_false(self):
        operatorStack = []  # Initialise operator stack

        # Initialise current token
        currentToken = operatorT.OperatorToken()
        currentToken.associativity = dictConstant.LEFT_TO_RIGHT
        currentToken.precedence = dictConstant.WEAK
        currentToken.symbol = '+'
        currentToken.affix = "INFIX"
        currentToken.tokenType = "OPERATOR_TOKEN"

        # isOperatorInStackHigherPrecedence(operatorStack, token)
        self.assertEqual(False, operatorT.isOperatorInStackHigherPrecedence(operatorStack, currentToken))

    def test_c_isOperatorInStackHigherPrecedence_given_infix_plus_at_stack_and_prefix_plus_as_token_expect_false(self):
        operatorStack = []  # Initialise operator stack

        # Initialise operator token to insert to stack
        currentToken = operatorT.OperatorToken()
        currentToken.associativity = dictConstant.LEFT_TO_RIGHT
        currentToken.precedence = dictConstant.WEAK
        currentToken.symbol = '+'
        currentToken.affix = "INFIX"
        currentToken.tokenType = "OPERATOR_TOKEN"

        # Initialise current token
        operatorToken = operatorT.OperatorToken()
        operatorToken.associativity = dictConstant.RIGHT_TO_LEFT
        operatorToken.precedence = dictConstant.STRONG
        operatorToken.symbol = '+'
        operatorToken.affix = "PREFIX"
        operatorToken.tokenType = "OPERATOR_TOKEN"
        # Push operator token into stack
        stack.pushStack(operatorStack, operatorToken)
        # isOperatorInStackHigherPrecedence(operatorStack, token)
        self.assertEqual(True, operatorT.isOperatorInStackHigherPrecedence(operatorStack, currentToken))


if __name__ == '__main__':
    unittest.main()
