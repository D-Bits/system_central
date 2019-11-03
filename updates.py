"""
A simple Python script to update currently installed packages.
"""
from subprocess import run
from platform import system


# Windows updates
def win_updates():

    # Chocolatey updates
    run(['choco', 'upgrade', 'all'], check=True)
    # WSL/Ubuntu updates
    run(['wsl', 'sudo', 'apt-get', 'update'], check=True)
    run(['wsl', 'sudo', 'apt-get', 'upgrade'], check=True)


# Updates for Ubuntu/Linux
def linux_updates():

    run(['sudo', 'apt-get', 'update'], check=True)
    run(['sudo', 'apt-get', 'upgrade'], check=True)


# Updates for MacOS
def mac_updates():

    # HomeBrew updates
    run(['brew', 'update'], check=True)
    run(['brew', 'upgrade'], check=True)


def updates_main():
    
    os_type = int(input('Enter 1 for Windows updates, 2 for Linux, and 3 for MacOS: '))

    if os_type == 1:
        win_updates()
    elif os_type == 2:
        linux_updates()
    elif os_type == 3:
        mac_updates()