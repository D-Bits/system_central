from hashing import hashing_main
from files import files_main


choices = {
    '1': 'Hashing Things',
    '2': 'File/Folder Automation',
}


if __name__ == "__main__":
    
    for key, val in choices.items():

        print(key, val)

    print() # Blank line for readability

    u_choice = int(input('Enter a choice, based on the above values: '))

    if u_choice == 1:
        hashing_main()
    elif u_choice == 2:
        files_main()