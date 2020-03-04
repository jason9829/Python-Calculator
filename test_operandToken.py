import unittest
import operandToken as operandT


class TestCaseFormatNumber(unittest.TestCase):
    def test_formatNumber_given_4_expect_4(self):
        # formatNumber(num)
        self.assertEqual(4, operandT.formatNumber(4))

    def test_formatNumber_given_60point5_expect_60point5(self):
        # formatNumber(num)
        self.assertEqual(60.5, operandT.formatNumber(60.5))


if __name__ == '__main__':
    unittest.main()
