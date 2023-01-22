"""
Coursework for 667V0033 1CWK50
Student name: Chibuzo Daniel Obi-okoli
Student ID: 22554053
This application was developed using code samples from:
10% Lecturer provided base for encrytion.py
70% https://pycryptodome.readthedocs.io/en/latest/src/examples.html#
20% Is done Me
All comments are original
"""
from secrets import token_bytes
from Cryptodome.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import gzip
import shutil
import os

class Encryption:

    def file_encrypt(self, filename, file_path):
        file_name = filename
        basename = os.path.basename(file_name)
        encfile_name = 'Encrypted_' + basename

        os.makedirs(file_path, exist_ok=True)
        # Read the contents of the file into a variable
        with open(file_name, "rb") as f:
            data = f.read()
        # Prompt user for the name or path of the public key in PEM format
        key_name = input("Enter the name or path of the public key in PEM format: ")
        # Read the public key using RSA.import_key
        with open(key_name, "rb") as f:
            public_key = RSA.import_key(f.read())
        # Generate a random 16-byte session key
        session_key = get_random_bytes(16)
        # Encrypt the session key using the RSA key
        cipher_rsa = PKCS1_OAEP.new(public_key)
        enc_session_key = cipher_rsa.encrypt(session_key)
        # Create an AES cipher object in EAX mode
        cipher = AES.new(session_key, AES.MODE_EAX)
        # Encrypt the data and create a tag
        ciphertext, tag = cipher.encrypt_and_digest(data)
        # Create a new file called 'encrypted_file'
        with open(os.path.join(file_path,encfile_name), "wb") as f:
            # Write the encrypted session key, the nonce, the tag, and the ciphertext to the file
            [f.write(x) for x in (enc_session_key, cipher.nonce, tag, ciphertext)]

        print("  *** File is Encrypted successfully ***  ")
        

    def Folder_encrypt(self):

        dir_path = input("Where do you like to save the encrypted folder: ")
        filedd = input("Enter the name of the folder or the folder path to be encrypted: ")

        #Create a backup of the folder
        backup_folder = filedd + "_backup"
        shutil.copytree(filedd, backup_folder)

        # Compress each file in the backup folder
        for file_name in os.listdir(backup_folder):
            with open(os.path.join(backup_folder,file_name), 'rb') as f_in, gzip.open(os.path.join(backup_folder,file_name+".gz"), 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
            os.remove(os.path.join(backup_folder,file_name))

        print("Each file in the folder has been compressed")

        # Encrypt the backup folder
        public_key = input("Enter the public key name or path(in Pem formart): ")
        recipient_key = RSA.import_key(open(public_key).read())
        os.makedirs(dir_path, exist_ok=True)
        for file_name in os.listdir(backup_folder):
            filee = open(os.path.join(backup_folder,file_name), 'rb')
            # read the file content
            data = filee.read()

            # Genearate the aes key
            session_key = get_random_bytes(16)
            # To save the new ecrypted files in a new file with prefix "Encrypted"
            new_file = 'Encrypted ' + file_name
            # To save the ecrypted files in a new folder of any chosen name
            file_out = open(os.path.join(dir_path,new_file), "wb")

            # Encrypt the aes_key with the public RSA key
            cipher_rsa = PKCS1_OAEP.new(recipient_key)
            enc_session_key = cipher_rsa.encrypt(session_key)

            # Encrypt the data with the AES session key
            cipher_aes = AES.new(session_key, AES.MODE_EAX)
            ciphertext, tag = cipher_aes.encrypt_and_digest(data)
            encrypted_data = ciphertext + tag
            [file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]

            with open(os.path.join(backup_folder, file_name), 'wb') as f:
                f.write(encrypted_data)

        #delete the backup
        shutil.rmtree(backup_folder)
        print(" ** Folder Encrypted and compressed backup deleted successfully ** ")
