import sys;

class Calculator:
    def sum(self, first_number, second_number):
        return first_number + second_number

    def subtract(self, first_numner, second_number):
        raise NotImplementedError("Feature not yet implemented")


if __name__ == '__main__':
    try:
        calculator = Calculator();
        result = calculator.sum(10, 15)
        print("Result is " + str(result))
    except:
        pass

    try:
        calculator = Calculator();
        result = calculator.subtract(10, 15)
        print("Result is " + str(result))
    except:
        print("Result was an error. ", sys.exc_info()[0])
        # raise
    finally:
        print("Finally is executed")

# https://docs.python.org/3/tutorial/errors.html