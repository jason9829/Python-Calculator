import unittest
import stringInterpreter as sI


class TestCaseInsertCharactersInString(unittest.TestCase):
    def test_insertCharactersInString_given_123_insert_equal_sign_at_index_1_expect_1_equal_sign_2_3(self):
        # insertCharactersInString(characters, expression, index), Index starts from 0 to x
        self.assertEqual("1=23", sI.insertCharactersInString("=", "123", 1))

    def test_insertCharactersInString_given_weird_symbols_insert_STOP_at_index_4_insert_correctly(self):
        # insertCharactersInString(characters, expression, index), Index starts from 0 to x
        self.assertEqual("!@#$STOP%^&*():", sI.insertCharactersInString("STOP", "!@#$%^&*():", 4))


class TesCaseAddSpaceBetweenCharacters(unittest.TestCase):
    def test_addSpaceBetweenCharacters_given_12space3_expect_1space2space3(self):
        # addSpaceBetweenCharacters(expression)
        self.assertEqual("1 2 3", sI.addSpaceBetweenCharacters("12 3"))

    def test_addSpaceBetweenCharacters_given_1plus2divide3_without_space_expect_spaces_between_characters(self):
        # addSpaceBetweenCharacters(expression)
        self.assertEqual("1 + 2 / 3", sI.addSpaceBetweenCharacters("1+2/3"))


if __name__ == '__main__':
    unittest.main()
