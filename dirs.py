from os import mkdir, chdir


# Automate the 
def create_dirs(dir_num, u_dir):

    for i in range(dir_num):

        dir_name = input('Enter a name for your directory: ')
        mkdir(dir_name)

    input(f'{dir_num} directories created. Press Enter to exit.')



