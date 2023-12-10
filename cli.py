##Created by John Vasko
import argparse #Import Argparser
from decrypter import EncDec #Import the fuction we need from Decrypter

parser = argparse.ArgumentParser(
    description="Encrypts a message using a key to a specified file.",
    prefix_chars="-"
)

parser.add_argument('-m',
                    help='Message to encrypt.',
                    nargs='?')

parser.add_argument('-key',
                    required=True,
                    help='Key to encrypt message.',
                    nargs='?')

parser.add_argument('-file',
                    required=True,
                    help='File to save encrypted message.',
                    nargs='?')

args = parser.parse_args() 

encdec = EncDec(args.key, args.file)

if args.message: #Instead of using a field for decrypt and encrypt i figured some logic might be nice. If the user doesnt supply a message then they arent trying to encrypt a message, therfore decrypt.
    encdec.save_msg(args.message) #Save the message to the file.
else:
    print(encdec.decrypt()) #Decrypt the file