def main():
    # Ask for user's name
    name = input("What is your name? ")

    # Ask for user's age
    age = int(input("How old are you? "))

    # Print a greeting with the user's name
    print(f"Hello, {name}!")

    # Calculate age in 10 years
    future_age = age + 10

    # Print the user's age in 10 years
    print(f"In 10 years, you will be {future_age} years old.")

if __name__ == "__main__":
    main()
