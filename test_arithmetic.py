import unittest
import arithmetic as ar


class TestCaseArithmeticSubFunctions(unittest.TestCase):
    def test_a_additionOf2Numbers_1_plus_5_expect_6(self):
        # additionOf2Numbers(num1, num2)
        self.assertEqual(1 + 5, ar.additionOf2Numbers(1, 5))

    def test_b_additionOf2Numbers_1point77_plus_99point99_expect_101point76(self):
        # additionOf2Numbers(num1, num2)
        self.assertEqual(1.77 + 99.99, ar.additionOf2Numbers(1.77, 99.99))

    def test_c_subtractionOf2Numbers_1_minus_5_expect_correct(self):
        # additionOf2Numbers(num1, num2)
        self.assertEqual(1 - 5, ar.subtractionOf2Numbers(1, 5))

    def test_d_subtractionOf2Numbers_111point77_minus_99point99_expect_correct(self):
        # additionOf2Numbers(num1, num2)
        self.assertEqual(111.77 - 99.99, ar.subtractionOf2Numbers(111.77, 99.99))

    def test_e_multiplicationOf2Numbers_22_times_5_expect_correct(self):
        # additionOf2Numbers(num1, num2)
        self.assertEqual(22 * 5, ar.multiplicationOf2Numbers(22, 5))

    def test_f_subtractionOf2Numbers_111point77_times_999point99_expect_correct(self):
        # additionOf2Numbers(num1, num2)
        self.assertEqual(111.77 * 999.99, ar.multiplicationOf2Numbers(111.77, 999.99))

    def test_g_multiplicationOf2Numbers_22_divide_50_expect_correct(self):
        # additionOf2Numbers(num1, num2)
        self.assertEqual(22 / 50, ar.divisionOf2Numbers(22, 50))

    def test_h_subtractionOf2Numbers_1111point77_divide_999point99_expect_correct(self):
        # additionOf2Numbers(num1, num2)
        self.assertEqual(1111.77 / 999.99, ar.divisionOf2Numbers(1111.77, 999.99))


class TestCaseMainFunction(unittest.TestCase):
    def test_a_calculationBasedOnOperator_given_12_12_plus_expect_correct(self):
        # calculationBasedOnOperator(num1, num2, operator)
        self.assertEqual(12 + 12, ar.calculationBasedOnOperator(12, 12, '+'))

    def test_b_calculationBasedOnOperator_given_88point888_12point44_plus_expect_correct(self):
        # calculationBasedOnOperator(num1, num2, operator)
        self.assertEqual(88.888 + 12.44, ar.calculationBasedOnOperator(88.888, 12.44, '+'))

    def test_c_calculationBasedOnOperator_given_56_66_minus_expect_correct(self):
        # calculationBasedOnOperator(num1, num2, operator)
        self.assertEqual(56 - 66, ar.calculationBasedOnOperator(56, 66, '-'))

    def test_d_calculationBasedOnOperator_given_8point888_8point888_minus_expect_correct(self):
        # calculationBasedOnOperator(num1, num2, operator)
        self.assertEqual(8.888 - 8.888, ar.calculationBasedOnOperator(8.888, 8.888, '-'))

    def test_e_calculationBasedOnOperator_given_88point888_12point44_minus_expect_correct(self):
        # calculationBasedOnOperator(num1, num2, operator)
        self.assertEqual(88.888 - 12.44, ar.calculationBasedOnOperator(88.888, 12.44, '-'))

    def test_f_calculationBasedOnOperator_given_55_55_multiply_expect_correct(self):
        # calculationBasedOnOperator(num1, num2, operator)
        self.assertEqual(55 * 55, ar.calculationBasedOnOperator(55, 55, '*'))

    def test_g_calculationBasedOnOperator_given_88point888_12point44_multiply_expect_correct(self):
        # calculationBasedOnOperator(num1, num2, operator)
        self.assertEqual(88.888 * 12.44, ar.calculationBasedOnOperator(88.888, 12.44, '*'))

    def test_h_calculationBasedOnOperator_given_8_5_divide_expect_correct(self):
        # calculationBasedOnOperator(num1, num2, operator)
        self.assertEqual(8 / 5, ar.calculationBasedOnOperator(8, 5, '/'))

    def test_i_calculationBasedOnOperator_given_88point888_124point44_divide_expect_correct(self):
        # calculationBasedOnOperator(num1, num2, operator)
        self.assertEqual(88.888 / 124.44, ar.calculationBasedOnOperator(88.888, 124.44, '/'))

    def test_j_calculationBasedOnOperator_given_88point888_124point44_equal_expect_exception_raised(self):
        # calculationBasedOnOperator(num1, num2, operator)
        try:
            self.assertEqual(None, ar.calculationBasedOnOperator(88.888, 124.44, '='))

        except Exception as e:
            print(e)


if __name__ == '__main__':
    unittest.main()
