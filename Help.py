class Help:
    def help_message(self):
        help_string = '-gpghome\t\tThe gpg home folder containing the public and private keyrings\n' \
                      '-type\t\t\tThe target type. Must be either "file" or "folder". E.g: [-type file /tmp/myfile.txt] or [-type folder /tmp/myfolder]\n' \
                      '-output\t\t\tThe output file\n' \
                      '-encrypt\t\tThe file to be encrypted\n' \
                      '-decrypt\t\tThe file to be decrypted\n' \
                      '\n\n\n' \
                      'Examples:\n' \
                      'Encrypt a file: ./pygpg -gpghome ~/.gnupg -encrypt -type file /tmp/myfile.txt -output /tmp/myfile.txt.pgp\n' \
                      'Encrypt a folder: ./pygpg -gpghome ~/.gnupg -encrypt -type folder /tmp/myfolder -output /tmp/myfolder.pgp\n' \
                      'Decrypt a file or folder: ./pygpg -gpghome ~/.gnupg -decrypt /tmp/myfile.txt.pgp -output /tmp/myfile.txt\n' \

        return help_string
