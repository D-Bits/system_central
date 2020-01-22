"""
A simple Python script to update currently installed packages.
"""
from subprocess import run, CalledProcessError
from platform import system

# Define options for updates
options = {
    0: "Return to main menu.",
    1: "Windows updates, via Chocolatey & WSL/Ubuntu.",
    2: "Linux updates, via APT.",
    3: "MacOS updates via Homebrew",
}

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
        
    for key, val in options.items():

        print(key, val)

    print()

    os_type = int(input('Enter an int from the options above: '))

    if os_type == 0:
        pass
    elif os_type == 1:
        win_updates()
    elif os_type == 2:
        linux_updates()
    elif os_type == 3:
        mac_updates()
            