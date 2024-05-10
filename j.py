import math

def main():
    print("Welcome to the main function!")
    result = add_numbers(5, 7)
    print("The result of adding 5 and 7 is:", result)
    print("The factorial of 5 is:", factorial(5))
    print("The area of a circle with radius 5 is:", calculate_circle_area(5))
    print("The square root of 16 is:", calculate_square_root(16))
    print("Is 10 a prime number?", is_prime(10))
    print("The sum of the first 10 natural numbers is:", sum_of_natural_numbers(10))
    print("The Fibonacci sequence up to 10 terms is:", fibonacci_sequence(10))
    print("The multiplication table of 5 is:")
    print_multiplication_table(5)

def add_numbers(a, b):
    return a + b

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def calculate_circle_area(radius):
    return math.pi * radius**2

def calculate_square_root(number):
    return math.sqrt(number)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

def fibonacci_sequence(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

if __name__ == "__main__":
    main()
