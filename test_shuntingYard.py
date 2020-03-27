import unittest
import shuntingYard as sY
import myGlobal as DictConstant
import operandToken as operandT
import operatorToken as operatorT
import stack as st


class TestCaseShuntingYard(unittest.TestCase):
    def test_a_shuntingYard_given_1_plus_157_expect_correct(self):
        operandStack = []
        operatorStack = []
        # shuntingYard(operandStack, operatorStack, expression)
        self.assertEqual(1 + 157, (sY.shuntingYard(operandStack, operatorStack, "1 + 157")).num)

    def test_b_shuntingYard_given_100point9_divide_50point5_expect_correct(self):
        operandStack = []
        operatorStack = []
        # shuntingYard(operandStack, operatorStack, expression)
        self.assertEqual(100.9 * 50.5, (sY.shuntingYard(operandStack, operatorStack, "100.9 * 50.5")).num)

    """def test_c_shuntingYard_given_100point9_plus_2point4_multiply_2_expect_correct(self):
        operandStack = []
        operatorStack = []
        # shuntingYard(operandStack, operatorStack, expression)
        self.assertEqual(100.9 + 2.4 * 2, sY.shuntingYard(operandStack, operatorStack, "100.9 + 2.4 * 2"))
    """


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


class TestCaseCreateToken(unittest.TestCase):
    def test_a_createToken_given_operand_expect_return_operand_token(self):
        # createToken(listIndex, expressionList, previousToken)
        listIndex = 0
        expressionList = ["1"]
        previousToken = None

        tokenCreated = sY.createToken(listIndex, expressionList, previousToken)
        # Test for token i
        self.assertEqual(1, tokenCreated.num)    # First token so index is 0
        self.assertEqual("int", tokenCreated.numType)
        self.assertEqual("OPERAND_TOKEN", tokenCreated.tokenType)


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
        self.assertEqual("OPERAND_TOKEN", operandStack[0].tokenType)

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


class TestCaseCreateToken(unittest.TestCase):
    def test_a_createToken_given_prefix_plus_expect_return_operator_token(self):
        expressionList = ["+", "0"]  # The function uses next character to determine affix type
        # createToken(listIndex, expressionList, previousToken)
        tokenCreated = sY.createToken(0, expressionList, None)
        self.assertEqual("+", tokenCreated.symbol)
        self.assertEqual(DictConstant.RIGHT_TO_LEFT, tokenCreated.associativity)
        self.assertEqual(DictConstant.STRONG, tokenCreated.precedence)
        self.assertEqual("PREFIX", tokenCreated.affix)

    def test_b_createToken_given_8_expect_return_operand_token(self):
        expressionList = ["8"]
        # createToken(listIndex, expressionList, previousToken)
        tokenCreated = sY.createToken(0, expressionList, None)
        self.assertEqual(8, tokenCreated.num)
        self.assertEqual("int", tokenCreated.numType)
        self.assertEqual("OPERAND_TOKEN", tokenCreated.tokenType)


class TestCasePushTokenToStack(unittest.TestCase):
    def test_a_pushTokenToStack_given_operand_1_expect_token_pushed(self):
        expressionList = ["1"]
        operandStack = []
        operatorStack = []
        # createToken(listIndex, expressionList, previousToken)
        tokenCreated = sY.createToken(0, expressionList, None)
        # pushTokenToStack(token, operandStack, operatorStack)
        sY.pushTokenToStack(tokenCreated, operandStack, operatorStack)
        self.assertEqual(1, operandStack[0].num)
        self.assertEqual("int", operandStack[0].numType)
        self.assertEqual("OPERAND_TOKEN", operandStack[0].tokenType)

    def test_b_pushTokenToStack_given_operand_open_bracket_expect_token_pushed(self):
        expressionList = ["(", "1"]  # The function uses next character to determine affix type
        operandStack = []
        operatorStack = []
        # createToken(listIndex, expressionList, previousToken)
        tokenCreated = sY.createToken(0, expressionList, None)
        # pushTokenToStack(token, operandStack, operatorStack)
        sY.pushTokenToStack(tokenCreated, operandStack, operatorStack)
        self.assertEqual("(", operatorStack[0].symbol)
        self.assertEqual(DictConstant.LEFT_TO_RIGHT, operatorStack[0].associativity)
        self.assertEqual(DictConstant.WEAK, operatorStack[0].precedence)
        self.assertEqual(None, operatorStack[0].affix)


class TestCaseCalculateAnsAndPushToOperandStack(unittest.TestCase):
    def test_a_calculateAnsAndPushToOperandStack_given_2_plus_2_expect_2_in_operand_stack(self):
        expressionList = ["2", "+", "2"]  # The function uses next character to determine affix type
        operandStack = []
        operatorStack = []
        # createToken(listIndex, expressionList, previousToken)
        token1 = sY.createToken(0, expressionList, None)
        # pushStack(stack, data)
        st.pushStack(operandStack, token1)
        token2 = sY.createToken(1, expressionList, token1)
        st.pushStack(operatorStack, token2)
        token3 = sY.createToken(2, expressionList, token2)
        st.pushStack(operandStack, token3)

        # calculateAnsAndPushToOperandStack(operandStack, operatorStack)
        sY.calculateAnsAndPushToOperandStack(operandStack, operatorStack)
        self.assertEqual(2+2, operandStack[0].num)

    def test_b_calculateAnsAndPushToOperandStack_given_10_divide_2_expect_5_in_operand_stack(self):
        expressionList = ["10", "/", "2"]  # The function uses next character to determine affix type
        operandStack = []
        operatorStack = []
        # createToken(listIndex, expressionList, previousToken)
        token1 = sY.createToken(0, expressionList, None)
        # pushStack(stack, data)
        st.pushStack(operandStack, token1)
        token2 = sY.createToken(1, expressionList, token1)
        st.pushStack(operatorStack, token2)
        token3 = sY.createToken(2, expressionList, token2)
        st.pushStack(operandStack, token3)

        # calculateAnsAndPushToOperandStack(operandStack, operatorStack)
        sY.calculateAnsAndPushToOperandStack(operandStack, operatorStack)
        self.assertEqual(10/2, operandStack[0].num)


class TestCaseIsNoOfTokensValidForOperation(unittest.TestCase):
    # One operand and one operator will cause error because the function to create token
    # will check for next token for operator token
    def test_a_isNoOfTokensValidForOperation_given_2_operand_and_1_operator_expect_true(self):
        expressionList = ["10", "/", "2"]  # The function uses next character to determine affix type
        operandStack = []
        operatorStack = []

        # createToken(listIndex, expressionList, previousToken)
        token1 = sY.createToken(0, expressionList, None)
        # pushStack(stack, data)
        st.pushStack(operandStack, token1)
        token2 = sY.createToken(1, expressionList, token1)
        st.pushStack(operatorStack, token2)
        token3 = sY.createToken(2, expressionList, token2)
        st.pushStack(operandStack, token3)
        # isNoOfTokensValidForOperation(operandStack, operatorStack)
        self.assertEqual(True, sY.isNoOfTokensValidForOperation(operandStack, operatorStack))

    def test_b_isNoOfTokensValidForOperation_given_1_operand_and_no_operator_expect_true(self):
        expressionList = ["-", "2"]  # The function uses next character to determine affix type
        operandStack = []
        operatorStack = []

        # createToken(listIndex, expressionList, previousToken)
        token1 = sY.createToken(0, expressionList, None)
        # pushStack(stack, data)
        st.pushStack(operandStack, token1)
        token2 = sY.createToken(1, expressionList, token1)
        st.pushStack(operatorStack, token2)
        # isNoOfTokensValidForOperation(operandStack, operatorStack)
        self.assertEqual(False, sY.isNoOfTokensValidForOperation(operandStack, operatorStack))

    def test_c_isNoOfTokensValidForOperation_given_3_operand_and_2_operator_expect_true(self):
        expressionList = ["1", "-", "2", "+", "3"]  # The function uses next character to determine affix type
        operandStack = []
        operatorStack = []

        # createToken(listIndex, expressionList, previousToken)
        token1 = sY.createToken(0, expressionList, None)
        # pushStack(stack, data)
        st.pushStack(operandStack, token1)
        token2 = sY.createToken(1, expressionList, token1)
        st.pushStack(operatorStack, token2)
        token3 = sY.createToken(1, expressionList, token1)
        st.pushStack(operandStack, token3)
        token4 = sY.createToken(1, expressionList, token1)
        st.pushStack(operatorStack, token4)
        token5 = sY.createToken(1, expressionList, token1)
        st.pushStack(operandStack, token5)
        # isNoOfTokensValidForOperation(operandStack, operatorStack)
        self.assertEqual(True, sY.isNoOfTokensValidForOperation(operandStack, operatorStack))


"""class TestCaseIsStacksReadyForOperation(unittest.TestCase):
    def test_a_isStacksReadyForOperation_given_1_plus_2_token_is_minus_3_expect_true(self):
        expressionList = ["1", "+", "2", "-", "3"]  # The function uses next character to determine affix type
        operandStack = []
        operatorStack = []

        # createToken(listIndex, expressionList, previousToken)
        token1 = sY.createToken(0, expressionList, None)
        # pushStack(stack, data)
        st.pushStack(operandStack, token1)
        token2 = sY.createToken(1, expressionList, token1)
        st.pushStack(operatorStack, token2)
        token3 = sY.createToken(1, expressionList, token1)
        st.pushStack(operandStack, token3)
        token4 = sY.createToken(1, expressionList, token1)
        # isStacksReadyForOperation(operandStack, operatorStack, token)
        self.assertEqual(True, sY.isStacksReadyForOperation(operandStack, operatorStack, token4))
"""


if __name__ == '__main__':
    unittest.main()
