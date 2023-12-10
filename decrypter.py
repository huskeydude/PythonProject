##Created by John Vasko
import base64 #Function for converting to base64
import hashlib #Function to hash the string
from cryptography.fernet import Fernet #Cryptography library

class EncDec: #lets create the class we will be using
    '''
    Encrypts a message using a key to a specified file.
    '''
    def __init__(self, key, save_file):
        hash = hashlib.sha256(key.encode()).digest() #hash with sha256
        fernet_key = base64.urlsafe_b64encode(hash) #convert that hashed string to base64 (Fernet needs base64)
        self.key = fernet_key #Save the hashed converted string
        self.save_file = save_file #Save that string into the class

    def save_msg(self, message):
        with open(self.save_file, 'w') as file: #open the file as write.
            cipher = Fernet(self.key) #Create a cypher instance and give it the key
            encrypted_msg = cipher.encrypt(message.encode()) #encrypts the message using the cipher
            file.write(encrypted_msg.decode()) #write the encrypted message to the file, but convert base64 -> string

    def decrypt(self):
        try: #Use a try so that we catch the file error
            with open(self.save_file, 'r') as file: #Open the save file
                encrypted_msg = file.read() #read the encrypted message from the file and save it
                cipher = Fernet(self.key) #Create a cypher instance and give it the key
                try: #Error catching
                    decrypted_msg = cipher.decrypt(encrypted_msg).decode() #Use the cypher to deconde the message. Then convert out of base64
                except:
                    decrypted_msg = "Key is incorrect or message is corrupted." #Error for if the kery provided is not correct.
                return decrypted_msg
        except: #If file doesnt exist tell the user
            return "File does not exist."