import unittest
import operatorToken as oT
import myGlobal as dictConstant


class TestCaseGetOperatorTokenInfo(unittest.TestCase):
    def test_getOperatorTokenInfo_given_INFIX_PLUS_expect_LEFT_TO_RIGHT_WEAK(self):
        """
        From myGlobal.py
        Associativity: LEFT_TO_RIGHT = 4
        Precedence: WEAK = 10
        """
        # getOperatorTokenInfo(operatorStr)
        tokenInfo = oT.getOperatorTokenInfo("INFIX_PLUS")
        self.assertEqual(dictConstant.LEFT_TO_RIGHT, tokenInfo[dictConstant.Associativity])
        self.assertEqual(dictConstant.WEAK, tokenInfo[dictConstant.Precedence])

    def test_getOperatorTokenInfo_given_PREFIX_MINUS_expect_RIGHT_TO_LEFT_STRONG(self):
        """
        From myGlobal.py
        Associativity: RIGHT_TO_LEFT = 5
        Precedence: STRONG = 11
        """
        # getOperatorTokenInfo(operatorStr)
        tokenInfo = oT.getOperatorTokenInfo("PREFIX_MINUS")
        self.assertEqual(dictConstant.RIGHT_TO_LEFT, tokenInfo[dictConstant.Associativity])
        self.assertEqual(dictConstant.STRONG, tokenInfo[dictConstant.Precedence])

    def test_getOperatorTokenInfo_given_invalid_operator_expect_None(self):
        # getOperatorTokenInfo(operatorStr)
        tokenInfo = oT.getOperatorTokenInfo("!")
        self.assertEqual(None, tokenInfo)


if __name__ == '__main__':
    unittest.main()
