import random

signs = ['!', '#', '$', '%', '&', '*', '(', ')', '+']
digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
caps_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

weak = True
while weak:
    number_of_lowers = int(input("how many lower case letters?"))
    number_of_caps = int(input("how many capital letters?"))
    number_of_digits = int(input("how many digits?"))
    number_of_signs = int(input("how many signs?"))
    password_chars = []

    for i in range(number_of_signs):
        new_sign = random.choice(signs)
        password_chars.append(new_sign)
        
    for i in range(number_of_digits):
        new_digit = random.choice(digits)
        password_chars.append(new_digit)

    for i in range(number_of_lowers):
        new_letter = random.choice(lower_letters)
        password_chars.append(new_letter)

    for i in range(number_of_caps):
        new_letter = random.choice(caps_letters)
        password_chars.append(new_letter)

    password = ""

    random.shuffle(password_chars)

    for char in password_chars:
        password += char

    if len(password) < 8:
        weakness = input(f"your password only contains {len(password)}. it's safer if your password has at least 8 characters.\ndo you want to try again with more characters?(y/n)").lower()
        if weakness == "n":
            weak = False
    else:
        weak = False
    
print(f"your password is {password}")