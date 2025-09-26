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


# Find what ports are currently listening on localhost
def get_servers(ports: list):

    # Common ports to check
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 8080]
    if ports == None:
        for port in common_ports:

            sock = socket()

            result = sock.connect_ex(('localhost', port))

            if result == 0:
                print(f"Port {port} is listening.")
            else:
                print(f"Port {port} is NOT listening.")

            sock.close()
    else:
        for port in ports:

            sock = socket()

            result = sock.connect_ex(('localhost', int(port)))

            if result == 0:
                print(f"Port {port} is listening.")
            else:
                print(f"Port {port} is NOT listening.")

            sock.close()


def sysinfo_main():

    print()

    u_options = {
        0: 'Return to Main Menu',
        1: "Get OS Info",
        2: "Get Hardware Info",
        3: "Get Network Info",
        4: "Find Currently Running Servers"
    }

    

     # Show the user their options
    for key, val in u_options.items():

        print(key, val)

    print()

    # Prompt the user to select an option
    u_choice = int(input("Enter an int to choose one of the above options: "))

    print()

    if u_choice == 0:
        pass
    elif u_choice == 1:
        os_info()
    elif u_choice == 2:
        hw_info()
    elif u_choice == 3:
        network_info()
    elif u_choice == 4:
        ports = list(input("Enter ports to check (comma separated, or leave blank for common ports): ").split(","))
        if ports == ['']:
            get_servers(None)
        else:
            get_servers(ports)
    else:
        print("Invalid option.")
