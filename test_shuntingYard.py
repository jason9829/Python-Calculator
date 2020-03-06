import unittest
import shuntingYard as sY
import myGlobal as DictConstant
import operandToken as operandT
import operatorToken as operatorT


class TestCaseShuntingYard(unittest.TestCase):
    def test_a_shuntingYard_given_1_plus_157_expect_correct(self):
        operandStack = []
        operatorStack = []
        # shuntingYard(operandStack, operatorStack, expression)
        self.assertEqual(1 + 157, sY.shuntingYard(operandStack, operatorStack, "1 + 157"))

    def test_b_shuntingYard_given_100point9_divide_50pont5_expect_correct(self):
        operandStack = []
        operatorStack = []
        # shuntingYard(operandStack, operatorStack, expression)
        self.assertEqual(100.9 * 50.5, sY.shuntingYard(operandStack, operatorStack, "100.9 * 50.5"))


class TestCaseIsExpressionValid(unittest.TestCase):
    def test_a_isExpressionValid_given_1a_plus_1_expect_false(self):
                                # isExpressionValid(expression):
        self.assertEqual(False, sY.isExpressionValid("1a + 1"))

    def test_b_isExpressionValid_given_1_plus_1_expect_true(self):
                                # isExpressionValid(expression):
        self.assertEqual(True, sY.isExpressionValid("1 + 1"))


class TestCaseGetCharFromToken(unittest.TestCase):
    def test_a_getCharFromToken_given_operand_token_expect_return_value_of_token_in_str(self):
        # createOperandToken(operandStr)
        operandToken = operandT.createOperandToken("123")
        # getCharFromToken(token):
        self.assertEqual("123", sY.getCharFromToken(operandToken))

    def test_a_getCharFromToken_given_operator_token_expect_return_char_of_operator_token_symbol(self):
        # Get the operator symbol in str then create the token
        # createOperatorToken(operatorStr)          getOperatorStrAffix(previousChar, nextChar, operatorSymbol)
        operatorToken = operatorT.createOperatorToken(operatorT.getOperatorStrAffix(None, "1", "+"))
        # getCharFromToken(token):
        self.assertEqual("+", sY.getCharFromToken(operatorToken))


class TestCaseCreateAndPushTokenToStack(unittest.TestCase):
    def test_a_createAndPushTokenToStack_given_operand_expect_push_in_operand_stack(self):
        # createAndPushTokenToStack(listIndex, expressionList, operandStack, operatorStack, previousToken)
        listIndex = 0
        expressionList = ["1"]
        operandStack = []
        operatorStack = []
        previousToken = None

        tokenCreated = sY.createAndPushTokenToStack(listIndex, expressionList, operandStack, operatorStack, previousToken)
        # Test for token return from function
        self.assertEqual(1, tokenCreated.num)
        self.assertEqual("int", tokenCreated.numType)
        self.assertEqual("OPERAND_TOKEN", tokenCreated.tokenType)

        # Test for token in the operand stack
        self.assertEqual(1, operandStack[0].num)    # First token so index is 0
        self.assertEqual("int", operandStack[0].numType)
        self.assertEqual("OPERAND_TOKEN", tokenCreated.tokenType)

    def test_b_createAndPushTokenToStack_given_operator_expect_push_in_operator_stack(self):
        # createAndPushTokenToStack(listIndex, expressionList, operandStack, operatorStack, previousToken)
        listIndex = 0
        expressionList = ["+", "-"]  # The function uses next character to determine affix type
        operandStack = []
        operatorStack = []
        previousToken = None

        tokenCreated = sY.createAndPushTokenToStack(listIndex, expressionList, operandStack, operatorStack, previousToken)
        # Test for token return from function
        self.assertEqual("+", tokenCreated.symbol)
        self.assertEqual(DictConstant.RIGHT_TO_LEFT, tokenCreated.associativity)
        self.assertEqual(DictConstant.STRONG, tokenCreated.precedence)
        self.assertEqual("PREFIX", tokenCreated.affix)

        # Test for token in the operator stack
        self.assertEqual("+", operatorStack[0].symbol)  # First token so index is 0
        self.assertEqual(DictConstant.RIGHT_TO_LEFT, operatorStack[0].associativity)
        self.assertEqual(DictConstant.STRONG, operatorStack[0].precedence)
        self.assertEqual("PREFIX", operatorStack[0].affix)


if __name__ == '__main__':
    unittest.main()
