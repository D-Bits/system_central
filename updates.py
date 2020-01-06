"""
A simple Python script to update currently installed packages.
"""
from subprocess import run, CalledProcessError
from platform import system


# Windows updates
def win_updates():

    try:
        # Chocolatey updates
        run(['choco', 'upgrade', 'all'], check=True)
        # WSL/Ubuntu updates
        run(['wsl', 'sudo', 'apt-get', 'update'], check=True)
        run(['wsl', 'sudo', 'apt-get', 'upgrade'], check=True)
        # Update Pip globally
        run(['pip', 'install', '--upgrade', 'pip'], check=True)

        print("Updates completed successfully. Press enter to exit.")
        
    except CalledProcessError:

        print("Updates failed. We apologize for the inconvience.")


    # Updates for Ubuntu/Linux
def linux_updates():

    try:
        run(['sudo', 'apt-get', 'update'], check=True)
        run(['sudo', 'apt-get', 'upgrade'], check=True)

    except CalledProcessError:

        print("Updates failed. We apologize for the inconvience.")    


    # Updates for MacOS
def mac_updates():

    try:
        # HomeBrew updates
        run(['brew', 'update'], check=True)
        run(['brew', 'upgrade'], check=True)

    except CalledProcessError:

        print("Updates failed. We apologize for the inconvience.")


def updates_main():
        
    os_type = int(input('Enter 1 for Windows (including WSL/Ubuntu) updates, 2 for Linux, and 3 for MacOS (Homebrew), or 0 to return to main menu: '))

    if os_type == 0:
        pass
    elif os_type == 1:
        win_updates()
    elif os_type == 2:
        linux_updates()
    elif os_type == 3:
        mac_updates()
            