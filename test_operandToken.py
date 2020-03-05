import unittest
import operandToken as operandT


class TestCaseGetNumberType(unittest.TestCase):
    def test_getNumberType_given_2point12_expect_float(self):
        # getNumberType(number)
        self.assertEqual("float", operandT.getNumberType(2.12))

    def test_getNumberType_given_1900_expect_int(self):
        # getNumberType(number)
        self.assertEqual("int", operandT.getNumberType(1900))


class TestCaseCreateOperandToken(unittest.TestCase):
    def test_createOperandToken_given_10point10_expect_token_with_correct_info(self):
        # createOperandToken(operandStr)
        operandToken = operandT.createOperandToken("10.10")
        self.assertEqual(10.10, operandToken.num)
        self.assertEqual("float", operandToken.type)

    def test_createOperandToken_given_1012_expect_token_with_correct_info(self):
        # createOperandToken(operandStr)
        operandToken = operandT.createOperandToken("1012")
        self.assertEqual(1012, operandToken.num)
        self.assertEqual("int", operandToken.type)

    def test_createOperandToken_given_abcd_expect_exception_raised(self):
        try:
            # createOperandToken(operandStr)
            operandToken = operandT.createOperandToken("abcd")
            self.assertEqual("abcd", operandToken.num)
            self.assertEqual(None, operandToken.type)

        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
