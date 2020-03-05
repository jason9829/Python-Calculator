import unittest
import shuntingYard as sY


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


if __name__ == '__main__':
    unittest.main()
