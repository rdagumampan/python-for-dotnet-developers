import unittest


# create basic unit test
class Calculator:
    def sum(self, first_number, second_number):
        return first_number + second_number

    def subtract(self, first_numner, second_number):
        raise NotImplementedError("Feature not yet implemented")


# inherits from unittest.TestCase
class BasicTest(unittest.TestCase):

    # basic unit tests
    def test_sum_ok(self):
        # arrange
        calculator = Calculator()

        # act
        result = calculator.sum(10, 15)

        # assert
        self.assertEqual(result, 25)

    def test_sum_fail(self):
        # arrange
        calculator = Calculator()

        # act
        result = calculator.sum(10, 15)

        # assert
        self.assertEqual(result, 30)

    # expecting exception
    def test_subtract_fail_not_yet_implemented(self):
        # arrange
        calculator = Calculator()

        # act
        result = calculator.subtract(20, 5)

        # assert
        self.assertEqual(result, 15)

    # ignore or skip test from runner
    def test_multiply_skip(self):
        unittest.skip("Skipping this test intentionally")


# run this with $ python main.py -v
if __name__ == '__main__':
    unittest.main()

# https://docs.python.org/3/library/unittest.html
# https://realpython.com/python-testing/
