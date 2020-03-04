import unittest
import shuntingYard as sY


class TestCaseShuntingYard(unittest.TestCase):
    def test_shuntingYard_given_1_plus_157_expect_correct(self):
        operandStack = []
        operatorStack = []
        # shuntingYard(operandStack, operatorStack, expression)
        self.assertEqual(1 + 157, sY.shuntingYard(operandStack, operatorStack, "1 +157"))


if __name__ == '__main__':
    unittest.main()
