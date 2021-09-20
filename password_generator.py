# 5 - Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""
for letter in range(0, nr_letters):
    password += random.choice(letters)
for symbol in range(0, nr_symbols):
    password += random.choice(symbols)
for number in range(0, nr_numbers):
    password += random.choice(numbers)
print(f"Your easy password {password}")

# hard level:
password_list = []
for x in password:
    password_list.append(x)

random.shuffle(password_list)
# comment 1

random_password = ""
for p in password_list:
    random_password += p
print(f"Your random password {random_password}")


# comment 1 - shuffle too
# for i in range(0, 55):
#     a = random.randint(0, len(password_list)-1)
#     b = random.randint(0, len(password_list)-1)
#     c = password_list[a]
#     password_list[a] = password_list[b]
#     password_list[b] = c