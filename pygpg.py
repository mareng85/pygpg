#!/usr/bin/env python
import os
import gnupg
import sys
from os.path import expanduser
from Help import Help
import tarfile

def parse_arguments():
    noOfArguments = len(sys.argv)

    home_is_set = False
    enc = False
    dec = False

    if noOfArguments == 1:
        print_help()
    else:
        for arg in range(0, noOfArguments):
            if sys.argv[arg] == '-gpghome':
                home = sys.argv[arg + 1]
                set_gnupg_home(home)
                home_is_set = True

            if sys.argv[arg] == '-encrypt':
                typearg = sys.argv[arg + 1]
                if typearg != '-type':
                    print "Expecting -type argument! E.g -encrypt -type folder <foldername>"
                else:
                    type = sys.argv[arg + 2]
                    target = sys.argv[arg + 3]
                    if len(sys.argv) > arg + 4:
                        if sys.argv[arg + 4]  == '-output':
                            output = sys.argv[arg + 5]
                        else:
                            raise Exception("Expecting output file!")
                    else:
                        output = None
                    enc = True

            if sys.argv[arg] == '-decrypt':
                target = sys.argv[arg + 1]
                if len(sys.argv) > arg + 2:
                    if sys.argv[arg + 2]  == '-output':
                        output = sys.argv[arg + 3]
                    else:
                        raise Exception("Expecting output file!")
                else:
                    output = None
                dec = True


    if not home_is_set:
        home = None
        set_gnupg_home(home)

    public_keys = gpg.list_keys()
    if len(public_keys) == 0:
        print "Could not find any keyrings. Make sure you have set a correct gpghome value!"
        exit(0)

    if enc and dec:
        raise Exception("You cannot both encrypt and decrypt a file at the same time!")
    elif enc:
        encrypt(type, target, output)
    elif dec:
        decrypt(target, output)

def decrypt(target, output):
    print "Decrypting..."

    encrypted_data = open(target, "rb")

    if output != None:
        gpg.decrypt_file(encrypted_data, output=output)
        print "Decrypted data is saved to",output
    else:
        print "\nThe decrypted message:\n"
        decrypted_data = gpg.decrypt_file(encrypted_data)
        print decrypted_data

def encrypt(type, target, output):
    if type == 'folder':
        print "Encrypting folder..."
        tar = tarfile.open(target+'/contents.tar.gz', "w:gz")
        tar.add(target, arcname=os.path.basename(target))
        tar.close()

        print_public_keys()
        uid = input("\nSelect recipient: ")
        recipient = get_recipient_fingerprint(uid)

        data = open(target+'/contents.tar.gz', "rb")

        if output != None:
            gpg.encrypt_file(data, [recipient], output=output)
            print "Encrypted data is saved to",output
        else:
            print "\nThe encrypted message:\n"
            encrypted_ascii_data = gpg.encrypt_file(data, [recipient])
            print encrypted_ascii_data

        os.remove(target+'/contents.tar.gz')

    elif type == 'file':
        print "Encrypting file..."
        print_public_keys()
        uid = input("\nSelect recipient: ")
        recipient = get_recipient_fingerprint(uid)

        data = open(target, "rb")

        if output != None:
            gpg.encrypt_file(data, [recipient], output=output)
            print "Encrypted data is saved to",output
        else:
            print "\nThe encrypted message:\n"
            encrypted_ascii_data = gpg.encrypt_file(data, [recipient])
            print encrypted_ascii_data
    else:
        raise Exception("Type must be 'folder' or 'file'!")

def set_gnupg_home(home):
    if home is None:
        home = expanduser("~")+'/.gnupg'

    global gpg
    gpg = gnupg.GPG(gnupghome=home)

def get_recipient_fingerprint(uid):
    public_keys = gpg.list_keys()
    return public_keys[uid]['fingerprint']

def main():
    parse_arguments()

def print_help():
    h = Help()
    print h.help_message()

def print_public_keys():
    public_keys = gpg.list_keys()
    print "\nRecipients:"
    for pub in range(0, len(public_keys)):
        print str(pub)+':', public_keys[pub]['uids'], public_keys[pub]['fingerprint']

if __name__ == "__main__":
    main()
