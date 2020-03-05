import unittest
import stringInterpreter as sI


class TestCaseIsFloat(unittest.TestCase):
    def test_a_isFloat_given_5point1_expect_True(self):
        # isFloat(expression)
        self.assertEqual(True, sI.isFloat("5.1"))

    def test_b_isFloat_given_2_expect_false(self):
        # isFloat(expression)
        self.assertEqual(False, sI.isFloat("2"))


class TestCaseInsertCharactersInString(unittest.TestCase):
    def test_a_insertCharactersInString_given_123_insert_equal_sign_at_index_1_expect_1_equal_sign_2_3(self):
        # insertCharactersInString(characters, expression, index), Index starts from 0 to x
        self.assertEqual("1=23", sI.insertCharactersInString("=", "123", 1))

    def test_b_insertCharactersInString_given_weird_symbols_insert_STOP_at_index_4_insert_correctly(self):
        # insertCharactersInString(characters, expression, index), Index starts from 0 to x
        self.assertEqual("!@#$STOP%^&*():", sI.insertCharactersInString("STOP", "!@#$%^&*():", 4))


class TestCaseAddSpaceBetweenCharacters(unittest.TestCase):
    def test_a_addSpaceBetweenCharacters_given_12space3_expect_1space2space3(self):
        # addSpaceBetweenCharacters(expression)
        self.assertEqual("1 2 3", sI.addSpaceBetweenCharacters("12 3"))

    def test_b_addSpaceBetweenCharacters_given_1plus2divide3point3_without_space_expect_spaces_between_characters(self):
        # addSpaceBetweenCharacters(expression)
        self.assertEqual("1 + 2 / 3.3", sI.addSpaceBetweenCharacters("1+2/3.3"))


class TestCaseIsNumber(unittest.TestCase):
    def test_a_isNumber_given_1112_expect_true(self):
        # isNumber(expression)
        self.assertEqual(True, sI.isNumber("1112"))

    def test_b_isNumber_given_12point111111_expect_true(self):
        # isNumber(expression)
        self.assertEqual(True, sI.isNumber("12.111111"))

    def test_c_isNumber_given_symbols_expect_false(self):
        # isNumber(expression)
        self.assertEqual(False, sI.isNumber("@!@$%"))


class TestCaseIsOperator(unittest.TestCase):
    def test_a_isOperator_given_plus_sign_expect_true(self):
        # isOperator(expression)
        self.assertEqual(True, sI.isOperator('+'))

    def test_b_isOperator_given_open_bracket_expect_true(self):
        # isOperator(expression)
        self.assertEqual(True, sI.isOperator('('))

    def test_c_isOperator_given_minus_divide_sign_expect_exception_raised(self):
        try:
            self.assertEqual(False, sI.isOperator("-/"))

        except Exception as e:
            print(e)

    def test_d_isOperator_given_1_expect_exception_raised(self):
        try:
            self.assertEqual(False, sI.isOperator('1'))

        except Exception as e:
            print(e)

    def test_e_isOperator_given_comma_expect_exception_raised(self):
        try:
            self.assertEqual(False, sI.isOperator(','))

        except Exception as e:
            print(e)


class TestCaseStringToNumber(unittest.TestCase):
    def test_a_stringToNumber_given_155_str_expect_155_int(self):
        self.assertEqual(155, sI.stringToNumber("155"))

    def test_b_stringToNumber_given_2point5_str_expect_2point5_float(self):
        self.assertEqual(2.5, sI.stringToNumber("2.5"))

    def test_c_stringToNumber_given_abcd_str_expect_exception_raised(self):
        try:
            self.assertEqual(None, sI.stringToNumber("abcd"))

        except Exception as e:
            print(e)


class TestCaseFormatNumber(unittest.TestCase):
    def test_formatNumber_given_4_expect_4(self):
        # formatNumber(num)
        self.assertEqual(4, sI.formatNumber(4))

    def test_formatNumber_given_60point5_expect_60point5(self):
        # formatNumber(num)
        self.assertEqual(60.5, sI.formatNumber(60.5))


class TestCaseMoveStr(unittest.TestCase):
    def test_a_moveStr_given_123456789_and_2_expect_3456789(self):
        # moveStr(expression, iteration)
        self.assertEqual("3456789", sI.moveStr("123456789", 2))

    def test_a_moveStr_given_abcd1234_and_4_expect_1234(self):
        # moveStr(expression, iteration)
        self.assertEqual("1234", sI.moveStr("abcd1234", 4))


class TestCaseIsAlphaInStr(unittest.TestCase):
    def test_a_isAlphaInStr_given_abcdqef_expect_true(self):
        # isAlphaInStr(expression)
        self.assertEqual(True, sI.isAlphaInStr("abcdqef"))

    def test_b_isAlphaInStr_given_avc1234_expect_true(self):
        # isAlphaInStr(expression)
        self.assertEqual(True, sI.isAlphaInStr("avc1234"))

    def test_c_isAlphaInStr_given_111_expect_false(self):
        # isAlphaInStr(expression)
        self.assertEqual(False, sI.isAlphaInStr("111"))

    def test_d_isAlphaInStr_given_12point12_expect_false(self):
        # isAlphaInStr(expression)
        self.assertEqual(False, sI.isAlphaInStr("12.12"))


if __name__ == '__main__':
    unittest.main()
