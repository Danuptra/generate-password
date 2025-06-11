import os
import time
import random
import string

purple = '\033[95m'
green = '\033[92m'
blue = '\033[94m'
default = '\033[0m'
cyan = '\033[96m'
red = '\033[0;31m'

def show_welcome():
    print(purple + '+----------------------------------------------+')
    print('|                                              |')
    print(f'|  {green}🔐  Welcome to Password Generator CLI  {purple}     |')
    print('|                                              |')
    print('|                                              |')
    print('|        ' + blue + 'Made with ❤️  by ' + green + 'danuptra' + purple + '              |')
    print('+----------------------------------------------+' + default)
    time.sleep(1)
show_welcome()


def generate_password():
    try:
        input_length = int(input(f"{cyan}How many characters do you want? \033[90m(minimum 14){default}\n> "))
    except ValueError:
        print(f"{red}Please enter a valid number!{default}")
        return

    if input_length < 14:
        print(f"{red}Minimum 14 characters or more required!{default}")
        return
    
    # Rules Character
    char1 = list(string.ascii_lowercase)
    char2 = list(string.ascii_uppercase)
    char3 = list(string.digits)
    char4 = list(string.punctuation)

    random.shuffle(char1)
    random.shuffle(char2)
    random.shuffle(char3)
    random.shuffle(char4)

    step_one = round(input_length * (20/100))
    step_two = round(input_length * (30/100))
    remaining = input_length - (step_one * 2 + step_two * 2)

    password = []

    password.extend(random.choices(char1, k=step_one))
    password.extend(random.choices(char2, k=step_one))
    password.extend(random.choices(char3, k=step_two))
    password.extend(random.choices(char4, k=step_two))

    full_password = char1 + char2 + char3 + char4
    password.extend(random.choices(full_password, k=remaining))

    random.shuffle(password)
    final_password = ''.join(password)
    print(f"{cyan}Generated Password:{default} {final_password}")

    try:
        with open('.password.txt', 'w+', encoding='utf-8', newline='') as file:
            file.write(f'Your password : {final_password}\n')
    except FileNotFoundError:
        return 
generate_password()
    