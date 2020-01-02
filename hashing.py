"""
Methods for hash and/or salting strings.
"""
from hashlib import sha256, sha1, pbkdf2_hmac
from getpass import getpass
from binascii import hexlify
from secrets import randbits


choices = {
    '1': 'Produce a SHA256 digest from stdin.',
    '2': 'Compare two hashes, to see if they match.',
    '3': 'Generate a salted hash.'
}


def getHash(msg):
    
    # Hash the input w/ SHA-256, and encode w/ UTF-8
    digest = sha256(msg.encode('utf-8'))

    print("SHA256 Digest:", digest.hexdigest().upper()) # Output the digest


# Compare two hashes (or any two strings, really) to ensure they match
def compare_hashes(hash1, hash2):

    if hash1 == hash2:
        print('The hashes match.')
        print()
        print("Hash 1: ", hash1)
        print("Hash 2: ", hash2)
    else:
        print('The hashes do NOT match.')
        print()
        print("Hash 1: ", hash1)
        print("Hash 2: ", hash2)


# Produce a salted hash of a user's password
def salted_hash(u_pass):

    s_hash = pbkdf2_hmac('sha256', b'u_pass', b'1*&#6^%787^*%&*!#^@29%**^523^@4@$', 120000)

    return hexlify(s_hash)


def hashing_main():

    for key, val in choices.items():

        print(key, val)

    print() # Blank line for readability

    u_choice = int(input('Enter a choice, based on the above values: '))

    if u_choice == 1:
        u_msg = input('Input a string to hash it w/ SHA256: ')
        getHash(u_msg)
    elif u_choice == 2:
        first_hash = input('Input the first digest: ')
        second_hash = input('Input the second digest: ')
        print()
        compare_hashes(first_hash, second_hash)
    elif u_choice == 3:
        user_pass = getpass('Enter a password to produce a salted hash: ')
        print(f'Your salted PBKDF2 hash is', salted_hash(user_pass).upper())
    else:
        input('Invalid value entered. Press enter to exit.')

   