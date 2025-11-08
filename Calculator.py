class Calculator:
    def add(a, b):
        sum = a + b
        print(f"The sum is {sum}")

    def subtract(a, b):
        diff = a - b
        print(f"The difference is {diff}")

    def multiply(a, b):
        product = a * b
        print(f"The product is {product}")

    def divide(a, b):
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            quotient = a / b
            print(f"The quotient is {quotient}")


calculator = Calculator

calculator.add(2, 4)
calculator.subtract(10, 3)
calculator.multiply(5, 6)
calculator.divide(8, 0)