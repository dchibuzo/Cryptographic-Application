"""
Coursework for 667V0033 1CWK50
Student name: Chibuzo Daniel Obi-okoli
Student ID: 22554053
This application was developed using code samples from:
100% https://pycryptodome.readthedocs.io/en/latest/src/examples.html#generate-public-key-and-private-key

All comments are original
"""
# To import the RSA module from the Crypto.PublicKey library
from Crypto.PublicKey import RSA

# To define class Rsa
class Rsa:
    def rsa(self):
        key = RSA.generate(2048)
        private_key = key.export_key()
        # To open a file named private.pem 
        file_out = open("private.pem", "wb")
        print(private_key)
        # To save the private key
        file_out.write(private_key)
        file_out.close()

        public_key = key.publickey().export_key()
        # To open a file named public.pem
        file_out = open("public.pem", "wb")
        print(public_key)
        # To save the the public key
        file_out.write(public_key)
        file_out.close()
