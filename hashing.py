"""
Methods for hash and/or salting strings.
"""
from hashlib import sha256, sha512, sha1, sha3_256, md5, pbkdf2_hmac
from getpass import getpass
from binascii import hexlify
from secrets import randbits


choices = {
    '1': 'Produce a hash digest from stdin.',
    '2': 'Compare two hashes, to see if they match.',
    '3': 'Generate a salted hash.'
}


def getHash(msg):

    hash_options = {
        1: 'MD5',
        2: 'SHA1',
        3: 'SHA256',
        4: 'SHA512',
        5: 'SHA3_256',
    }

    # Show the user their hashing options
    for key, val in hash_options.items():

        print(key, val)

    print() # Blank line for readability

    hash_choice = int(input("Enter an int to choose a hashing algorithm from above (If you seriously choose MD5, then you should be ashamed of yourself): "))

    print()

    if hash_choice == 1:
        hasher = md5
        digest = md5(msg.encode('utf-8'))
    elif hash_choice == 2:
        hasher = sha1
        digest = sha1(msg.encode('utf-8'))
    elif hash_choice == 3:
        hasher = sha256
        digest = sha256(msg.encode('utf-8'))
    elif hash_choice == 4:
        hasher = sha512
        digest = sha512(msg.encode('utf-8'))
    elif hash_choice == 5:
        hasher = sha3_256
        digest = sha3_256(msg.encode('utf-8'))
    else:
        print("Invalid value entered.")

    print("Hash Digest:", digest.hexdigest().upper()) # Output the digest


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
        u_msg = input('Input a string to hash: ')
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

   