import os
import time
import random
import string
import argparse

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


def generate_password(input_length):
    if input_length < 14:
        raise ValueError("Minimum 14 characters or more required!")
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
    return final_password

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--length', type=int, help='Password length')
    parser.add_argument('--save', type=str, choices=['yes', 'no'], default='no', help='Save password to file (yes/no)')
    args = parser.parse_args()
    show_welcome()
    if args.length:
        input_length = args.length
    else:
        try:
            input_length = int(input(f"{cyan}How many characters do you want? \033[90m(minimum 14){default}\n> "))
        except ValueError:
            print(f"{red}Please enter a valid number!{default}")
            exit(1)
    try:
        final_password = generate_password(input_length)
    except ValueError as ve:
        print(f"{red}{ve}{default}")
        exit(1)
    print(f"{cyan}\nGenerated Password:{default} {final_password}")
    if args.save.lower() in ['yes', 'y']:
        save = 'y'
    else:
        try:
            save = input(f"{purple}\nDo you want to save this password to a file?{default} {cyan}(Y/n){default}: ").strip().lower()
        except EOFError:
            print(f"{blue}🛈 Skipping save prompt due to non-interactive environment.{default}")
            save = 'n'
    if save == 'y':
        try:
            with open('.password.txt', 'w+', encoding='utf-8', newline='') as file:
                file.write(f'Your password : {final_password}\n')
                print(f'\n✅ {green} Password save to .password.txt {default}')
        except Exception as e:
            print(f"{red}Failed to save password: {e}{default}")
    else:
        print(f'\n{blue}🛈 Password not saved{default}')
