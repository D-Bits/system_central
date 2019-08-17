"""
A file for automating the execution of manage.py tasks in Django.
"""
from os import chdir
from subprocess import call


# Store the user's choices in a dictionary
choices = {
    1: 'Boot the dev server',
    2: 'Makemigrations & migrate',
    3: 'Add another app to your project.',
    4: 'Create a superuser.',
    5: 'Collect static files.',
    6: 'Run unit tests.'
}


# Add another app to your Django project
def add_app():

    app_name = input('Enter the name of the app that you want to add to your project: ')

    if not app_name:

        input('App name cannot be null! Press enter to exit.')

    call(['python', 'manage.py', 'startapp', app_name])


if __name__ == "__main__":

    # Change into the dir that manage.py is located in
    chdir('danabases')

    # Blank line for readability
    print()

    # Show the user their choices
    for key, val in choices.items():

        print(key, val)

    print()

    # Prompt the user to make a choice
    u_choice = int(input('Execute a process, based on the above options: '))

    if u_choice == 1:
        call(['python', 'manage.py', 'runserver'])
    elif u_choice == 2:
        app_name = input('Enter the name of the app that you want to do migrations for: ')
        call(['python', 'manage.py', 'makemigrations', app_name])
        call(['python', 'manage.py', 'migrate'])
    elif u_choice == 3:
        add_app()
    elif u_choice == 4:
        call(['python', 'manage.py', 'createsuperuser'])
    elif u_choice == 5:
        call(['python', 'manage.py', 'collectstatic'])
    elif u_choice == 6:
        call(['python', 'manage.py', 'test', 'postings.tests'])
    else:
        input('Invalid option. Press enter to exit')
