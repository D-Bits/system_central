from os import chdir
from subprocess import call
from hashing import hashing_main
from filesys import files_main
from emails import emails_main
from updates import updates_main
from sysinfo import sysinfo_main


choices = {
    1: 'Hashing Things',
    2: 'File/Directory Automation',
    3: 'Automate Updates.',
    4: "Get System Info",
}

# Run the program
def main():
    
    for key, val in choices.items():

        print(key, val)

    print() # Blank line for readability

    u_choice = int(input('Enter a choice, based on the above values: '))

    if u_choice == 1:
        hashing_main()
        print()
        main()
    elif u_choice == 2:
        files_main()
        print()
        main()
    elif u_choice == 3:
        updates_main()
        print()
        main()  
    elif u_choice == 4:
        sysinfo_main()
        print()
        main()
    else:
        raise Exception('Invalid value entered.')


main()