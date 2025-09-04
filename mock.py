"""
UDFs for generating mock data using the Faker library.
"""
from faker import Faker


fake = Faker()


def mock_people(num: int, output_loc: str):
    """
    Generate mock people data and save to a file.

    Args:
        num (int): Number of mock people to generate.
        output_loc (str): File path to save the generated data.
    """
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
            # Write the values to a CSV  file
            f.write(f"{cname},{address},{email},{phone}\n")
