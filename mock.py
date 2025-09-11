"""
UDFs for generating mock data using the Faker library.
"""
from faker import Faker
import random
import hashlib


choices = {
     0: 'Return to Main Menu',
     1: 'Generate mock people data',
     2: 'Generate mock company data',
     3: 'Generate mock geographical data',
     4: 'Generate mock user data',
}

fake = Faker()


def mock_people(num: int, output_loc: str, dtype: str = 'csv'):
    """
    Generate mock people data and save to a file.

    Args:
        num (int): Number of mock people to generate.
        output_loc (str): File path to save the generated data.
    """
    if dtype.lower() != 'csv':
        with open(output_loc, 'w') as f:
            for _ in range(num):
                lname = fake.last_name()
                fname = fake.first_name()
                address = fake.address().replace('\n', ', ')
                email = fake.email()
                phone = fake.phone_number()
                # Create a CSV header 
                if _ == 0:
                    f.write("lname,fname,street_address,email,phone\n")
                # Write the values to a CSV  file
                f.write(f"{lname},{fname},{address},{email},{phone}\n")
    elif dtype=='json':
        with open(output_loc, 'w') as f:
            f.write("[\n")
            for _ in range(num):
                lname = fake.last_name()
                fname = fake.first_name()
                address = fake.address().replace('\n', ', ')
                email = fake.email()
                phone = fake.phone_number()
                # Write the values to a JSON file
                f.write("  {\n")
                f.write(f'    "lname": "{lname}",\n')
                f.write(f'    "fname": "{fname}",\n')
                f.write(f'    "street_address": "{address}",\n')
                f.write(f'    "email": "{email}",\n')
                f.write(f'    "phone": "{phone}"\n')
                if _ == num - 1:
                    f.write("  }\n")
                else:
                    f.write("  },\n")
            f.write("]\n")
    else:
        print("Invalid data type specified. Please use 'csv' or 'json'.")


def mock_companies(num: int, output_loc: str):
    """
    Generate mock company data and save to a file.

    Args:
        num (int): Number of mock companies to generate.
        output_loc (str): File path to save the generated data.
    """
    with open(output_loc, 'w') as f:
        for _ in range(num):
            cname = fake.company()
            address = fake.address().replace('\n', ', ')
            email = fake.company_email()
            phone = fake.phone_number()
            # Create a CSV header 
            if _ == 0:
                f.write("cname,street_address,email,phone\n")
            # Write the values to a CSV  file
            f.write(f"{cname},{address},{email},{phone}\n")


def mock_geo(num: int, output_loc: str):
    """
    Generate mock geographical data and save to a file.

    Args:
        num (int): Number of mock geographical entries to generate.
        output_loc (str): File path to save the generated data.
    """
    with open(output_loc, 'w') as f:
        for _ in range(num):
            city = fake.city()
            state = fake.state()
            country = fake.country()
            lat = fake.latitude()
            lon = fake.longitude()
            # Create a CSV header 
            if _ == 0:
                f.write("city,statecode,country,lat,lon\n")
            # Write the values to a CSV  file
            f.write(f"{city},{state},{country},{lat},{lon}\n")


def mock_users(num: int, output_loc: str):
    """
    Generate mock user data and save to a file.

    Args:
        num (int): Number of mock users to generate.
        output_loc (str): File path to save the generated data.
    """
    with open(output_loc, 'w') as f:
        for _ in range(num):
            uname = fake.user_name()
            fname = fake.first_name()
            lname = fake.last_name()
            email = fake.email()
            password = f"{fake.word() + fake.word() + random.randint(1940,2010).__str__()}"
            # password = fake.password(length=12)
            # Hash the password using SHA-256 and convert to uppercase
            password_hash = hashlib.sha256(password.encode()).hexdigest()
            # password_hash = password_hash.upper()
            # Create a CSV header 
            if _ == 0:
                f.write("uname,fname,lname,email,userpass\n")
            # Write the values to a CSV  file
            f.write(f"{uname},{fname},{lname},{email},{password_hash}\n")


def mock_main():

    for key, val in choices.items():

        print(key, val)

    print() # Blank line for readability

    u_choice = int(input('Enter a choice, based on the above values: '))

    if u_choice == 0:
        pass
    elif u_choice == 1:
        n = int(input('How many mock people to generate? '))
        loc = input('Enter a file path to save the data (e.g., C:/path/to/file.csv): ')
        dtype = input("Enter data type ('csv' or 'json'): ").strip().lower()
        mock_people(n, loc, dtype=dtype)
        print(f'Mock people data saved to {loc}')
    elif u_choice == 2:
        n = int(input('How many mock companies to generate? '))
        loc = input('Enter a file path to save the data (e.g., C:/path/to/file.csv): ')
        mock_companies(n, loc)
        print(f'Mock company data saved to {loc}')
    elif u_choice == 3:
        n = int(input('How many mock geographical entries to generate? '))
        loc = input('Enter a file path to save the data (e.g., C:/path/to/file.csv): ')
        mock_geo(n, loc)
        print(f'Mock geographical data saved to {loc}')
    elif u_choice == 4:
        n = int(input('How many mock users to generate? '))
        loc = input('Enter a file path to save the data (e.g., C:/path/to/file.csv): ')
        mock_users(n, loc)
        print(f'Mock user data saved to {loc}')
    else:
        print()
        print('***Invalid value entered.***')
        print()
        mock_main()