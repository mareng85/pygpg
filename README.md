# pygpg
A simple tool for encryping and decrypting files and folders using GnuPG.

This tool requires python-gnupg. You can install it using:

    pip install python-gnupg
    
## Arguments

    -gpghome  The gpg home folder containing the public and private keyrings
    -type     The target type. Must be either "file" or "folder". E.g: [-type file /tmp/myfile.txt] or [-type folder /tmp/myfolder]
    -output   The output file
    -encrypt  The file to be encrypted
    -decrypt  The file to be decrypted
    
## Use

    Encrypt a file: 
      ./pygpg -pgphome ~/.gnupg -encrypt -type file /tmp/myfile.txt -output /tmp/myfile.txt.pgp
    Encrypt a folder: 
      ./pygpg -pgphome ~/.gnupg -encrypt -type folder /tmp/myfolder -output /tmp/myfolder.pgp
    Decrypt a file or folder: 
      ./pygpg -pgphome ~/.gnupg -decrypt /tmp/myfile.txt.pgp -output /tmp/myfile.txt
