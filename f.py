import random

def main():
    print("Welcome to the main function!")
    numbers = generate_random_numbers(10, 1, 100)
    print("Random numbers:", numbers)
    shuffled = shuffle_list(numbers)
    print("Shuffled numbers:", shuffled)
    reversed_list = reverse_list(numbers)
    print("Reversed list:", reversed_list)
    unique_numbers = remove_duplicates(numbers)
    print("List with duplicates removed:", unique_numbers)
    palindrome = is_palindrome("radar")
    print("Is 'radar' a palindrome?", palindrome)
    encrypted_text = encrypt_text("Hello, World!", 3)
    print("Encrypted text:", encrypted_text)
    decrypted_text = decrypt_text(encrypted_text, 3)
    print("Decrypted text:", decrypted_text)

def generate_random_numbers(n, start, end):
    return [random.randint(start, end) for _ in range(n)]

def shuffle_list(lst):
    shuffled = lst[:]
    random.shuffle(shuffled)
    return shuffled

def reverse_list(lst):
    return lst[::-1]

def remove_duplicates(lst):
    return list(set(lst))

def is_palindrome(string):
    return string == string[::-1]

def encrypt_text(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted += chr(shifted)
        else:
            encrypted += char
    return encrypted

def decrypt_text(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) - shift
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
            decrypted += chr(shifted)
        else:
            decrypted += char
    return decrypted

if __name__ == "__main__":
    main()
