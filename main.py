from hashing import hashing_main
from filesys import files_main
from emails import emails_main
from updates import updates_main
from sysinfo import sysinfo_main


choices = {
    0: "Exit Program",
    1: "Hashing Things",
    2: "File/Directory Automation",
    3: "Automate Updates.",
    4: "Get System Info",
}

# Run the program
def main():
    
    for key, val in choices.items():

        print(key, val)

    print() # Blank line for readability

    u_choice = int(input('Enter a choice, based on the above values: '))

    if u_choice == 0:
        pass
    elif u_choice == 1:
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
        #print()
        main()
    else:
        print()
        print('***Invalid value entered.***')
        print()
        main()


main()