"""
A simple program for automating file management.
"""
from shutil import move
from os import chdir, mkdir, getcwd
from hashlib import md5, sha1, sha256, sha512, sha3_256


# Move all files from one dir to another
def move_dirs():

    src_dir = input('Input the full path of source directory: ')
    target_dir = input('Input the full path of target directory you want to move files to: ')

    move(src_dir, target_dir)


# Automate the creation of multiple directories
def create_dirs(dir_num):

    for i in range(dir_num):

        dir_name = input('Enter a name for your directory: ')
        mkdir(dir_name)

    print(f'{dir_num} directories created in {getcwd()}. Press Enter to exit.')


# Calculate a checksum for a file
def file_checksum(file_name):

    hash_options = {
        1: 'MD5',
        2: 'SHA1',
        3: 'SHA256',
        4: 'SHA512',
        5: 'SHA3_256',
    }

    # Show the user their hashing options
    for key, val in hash_options.items():

        print(key, val)

    print() # Blank line for readability

    hash_choice = int(input("Enter an int to choose a hashing algorithm from above (If you seriously choose MD5, then you should be ashamed of yourself): "))

    if hash_choice == 1:
        hasher = md5
        with open(file_name, "rb") as open_file:
            content = open_file.read()
        return hasher(content).hexdigest().upper()
    elif hash_choice == 2:
        hasher = sha1
        with open(file_name, "rb") as open_file:
            content = open_file.read()
        return hasher(content).hexdigest().upper()
    elif hash_choice == 3:
        hasher = sha256
        with open(file_name, "rb") as open_file:
            content = open_file.read()
        return hasher(content).hexdigest().upper()
    elif hash_choice == 4:
        hasher = sha512
        with open(file_name, "rb") as open_file:
            content = open_file.read()
        return hasher(content).hexdigest().upper()
    elif hash_choice == 5:
        hasher = sha3_256
        with open(file_name, "rb") as open_file:
            content = open_file.read()
        return hasher(content).hexdigest().upper()
    else:
        print("Invalid value entered.")


def files_main():

    choices = {
        1: 'Move Directory',
        2: 'Calculate a File Checksum.',
        3: 'Create multiple directories.',
    }

    for key, val in choices.items():

        print(key, val)

    print() # Blank line for readability

    u_choice = int(input('Enter a choice, based on the above values: '))

    if u_choice == 1:
        move_dirs()
    elif u_choice == 2:
        file_path = input('Enter the file path & name (ex: c:/uname/documents/file.txt): ')
        print(f'Your file hash is:', file_checksum(file_path))
        print()
    elif u_choice == 3:
        file_path = input('Enter the file path & name (ex: c:/uname/documents/file.txt): ')
        no_of_dirs = int(input('Enter the number of directories you want to make: '))
        chdir(file_path)
        create_dirs(no_of_dirs)
    else:
        input('Invalid value entered. Press enter to exit.')
