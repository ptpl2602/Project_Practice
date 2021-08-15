#Project: Random Password Generator

import string
import random

LETTERS = string.ascii_letters
NUMBERS = string.digits
PUNCTUATION = string.punctuation

def get_password_length():
    pass_length = input("How long do you want your password: ")
    return(int(pass_length))

def pass_generator(length=8):
    printable = f'{LETTERS}{NUMBERS}{PUNCTUATION}'
    
    printable = list(printable)
    random.shuffle(printable)                         #đảo trộn ngẫu nhiên các ký tự các nhau
    
    random_pass = random.choices(printable, k=length) #chọn ra 8 ký tự ngẫu nhiên
    random_pass = ''.join(random_pass)                #nối 8 ký tự ngẫu nhiên thành 1 chuỗi
    return random_pass

def main():
    length = get_password_length()
    passed = pass_generator(length)
    print(passed)

main()


