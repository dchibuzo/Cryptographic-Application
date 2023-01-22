"""
Coursework for 667V0033 1CWK50
Student name: Chibuzo Daniel Obi-okoli
Student ID: 22554053
This application was developed using code samples from:
50% https://nitratine.net/blog/post/python-encryption-and-decryption-with-pycryptodome/#eax-example_1
40% Is done by me
All comments are original
"""
from secrets import token_bytes
from Cryptodome.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP
import shutil
import gzip
import os



class Decryption:
    def file_decryption(self):
        encrypted_file = input("Enter the encrypted file: ")
        file_in = open(encrypted_file, "rb")

        private_key = input("Enter the private key name or path: ")
        private_key = RSA.import_key(open(private_key).read())
        

        enc_session_key, nonce, tag, ciphertext = [ file_in.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

        # Decrypting the aes_key with the private RSA key
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # Decrypting the data with the aes_key
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)

        
        # To save the decrypted file in a new file called "decrypted_file"
        file_out = open("decrypted_file", "wb")
        file_out.write(data)
        file_out.close()

        print(" ** File decrypted successfully ** ")


    def Folder_decryption(self):

        # This is where the encrypted folder is located
        enc_folder = input("Enter the name of the folder or the folder path to be decrypted: ")

        # This is where you want to save the decrypted folder
        dec_folder = input("Where do you like to save the decrypted folder: ")

        # Get the private key for decryption
        private_key = input("Enter the private key name or path(in Pem formart): ")
        private_key = RSA.import_key(open(private_key).read())

        # Check if the decryption folder already exists, if not create it
        os.makedirs(dec_folder, exist_ok=True)

        # Decrypt each file in the encrypted folder
        for file_name in os.listdir(enc_folder):
            with open(os.path.join(enc_folder,file_name), 'rb') as f:
                enc_session_key, nonce, tag, ciphertext = [ f.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1) ]

            # Decrypt the session key with the private RSA key
            cipher_rsa = PKCS1_OAEP.new(private_key)
            session_key = cipher_rsa.decrypt(enc_session_key)

            # Decrypt the data with the AES session key
            cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
            data = cipher_aes.decrypt_and_verify(ciphertext, tag)
            with open(os.path.join(dec_folder, file_name), 'wb') as f:
                f.write(data)

            for file_name in os.listdir(dec_folder):
                if file_name.endswith(".gz"):
                 with gzip.open(os.path.join(dec_folder,file_name), 'rb') as f_in, open(os.path.join(dec_folder,file_name.split(".gz")[0]), 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(os.path.join(dec_folder,file_name))

        print(" ** Folder decrypted successfully ** ")

