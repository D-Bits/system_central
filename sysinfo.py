"""
Functions for getting various info about the user's system.
"""
from platform import (
    node, 
    platform, 
    architecture, 
    python_version, 
    machine, 
    processor
)
from socket import gethostbyname, socket, gethostname


# Get info about the OS
def os_info():

    print() # Blank line for readability
    print("OS Info:")
    print("Device Name:", node())
    # print("User:", getuser())
    print("OS:", platform())
    print("Architechture:", str(architecture()))
    print("Python Version:", str(python_version()))
    print()


# Get hardware info
def hw_info():

    print("Hardware Info: ")
    print("CPU Type:", machine())
    print("CPU Info:", processor())
    print()


def network_info():

    host_name = gethostname()
    ip_address = gethostbyname(host_name)

    print("Network Info: ")
    print("Host:", host_name)
    print("IP Address:", ip_address)
    print()


def sysinfo_main():

    print()

    u_options = {
        1: "Get OS Info",
        2: "Get Hardware Info",
        3: "Get Network Info",
    }

    

     # Show the user their options
    for key, val in u_options.items():

        print(key, val)

    print()

    # Prompt the user to select an option
    u_choice = int(input("Enter an int to choose one of the above options: "))

    print()

    if u_choice == 1:
        os_info()
    elif u_choice == 2:
        hw_info()
    elif u_choice == 3:
        network_info()
    else:
        print("Invalid option.")

        
