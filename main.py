from os import chdir
from subprocess import call
from hashing import hashing_main
from files import files_main
from emails import emails_main
from dirs import create_dirs



choices = {
    1: 'Hashing Things',
    2: 'File/Folder Automation',
    3: 'Email Automation',
    4: 'Directory Automation.'
}


if __name__ == "__main__":
    
    for key, val in choices.items():

        print(key, val)

    print() # Blank line for readability

    u_choice = int(input('Enter a choice, based on the above values: '))

    if u_choice == 1:
        hashing_main()
        input('Mission accomplished. Press enter to exit.')
    elif u_choice == 2:
        files_main()
        input('Mission accomplished. Press enter to exit.')
    elif u_choice == 3:
        emails_main()
        input('Mission accomplished. Press enter to exit.')
    elif u_choice == 4:
        dir_num_choice = int(input("Enter the number of directories you want to create: "))
        u_dir_choice = input("Enter the location where you want to create directories (Ex: /users/me/home/documents/projects): ")
        chdir(u_dir_choice)
        create_dirs(dir_num_choice, u_dir_choice)
    else:
        raise Exception('Invalid value entered.')
