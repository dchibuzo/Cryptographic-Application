"""Coursework for 667V0033 1CWK50
Student name: Chibuzo Daniel Obi-okoli
Student ID: 22554053
This application was developed using code samples from:
30% https://www.youtube.com/watch?v=63nw00JqHo0&ab_channel=AndyDolinski
70% Is done by Me
All comments are original
"""

from secrets import token_bytes
from encryption import Encryption
from decryption import Decryption
from rsa import Rsa
import sys

while True:
    print()
    print('** MENU **')
    print("1 Generate Rsa")
    print("2 Encrypt single file")
    print("3 Encrypt folder")
    print("4 Decrypt single file")
    print("5 Decrypt folder")
    print("6 exit")

    option = int(input('Enter an Option: '))
    if option == 1:
        # To call the Rsa class function
        a = Rsa()
        # To call the characteristics of the rsa class 
        a.rsa()
    elif option == 2:
        file_name= input ('Enter name/path of file: ')
        file_path= input ("Where do you like to save the encrypted file: ")
        b = Encryption()
        b.file_encrypt(file_name, file_path)
    elif option == 3:
        c = Encryption()
        c.Folder_encrypt()
    elif option == 4:
        d = Decryption()
        d.file_decryption()
    elif option == 5:
        e = Decryption()
        e.Folder_decryption()
    elif option == 6:
        sys.exit()
    else:
        print("Select another option")


