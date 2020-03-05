import unittest
import operatorToken as operatorT
import myGlobal as dictConstant


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

    def test_c_createOperatorToken_given_CURLY_BRACKET_expect_exception_raised(self):
        try:                        # createOperatorToken(operatorStr)
            operatorToken = operatorT.createOperatorToken("CURLY_BRACKET")
            self.assertEqual(None, operatorToken.associativity)
            self.assertEqual(None,  operatorToken.precedence)
            self.assertEqual(None, operatorToken.symbol)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
