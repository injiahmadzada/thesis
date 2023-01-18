#implementaion of machine learning to decrypt the caesar cipher 
#the program should analyse all brute force results and find the logical one to output



import sys
import subprocess

message = input("Enter the encrypted text:  ")
offset = 0

#brute force attack
while offset < 26:
    decrypt = ""
    for char in message:
            if not char.isalpha():  
                decrypt = decrypt + char

            elif char.isupper():
                decrypt = decrypt + chr((ord(char) - offset - 65) % 26 + 65)  # -65 +65 for uppercase Z

            else:
                decrypt = decrypt + chr((ord(char) - offset - 97) % 26 + 97)  # -97 +97 for lowercase z
        
    offset = offset + 1
    print( offset, decrypt)

#saves output to a file

with open("output.txt", "w+") as output:
    output.write(decrypt)
    
"""  
    output = open('thesis/library/output.txt', 'w')
    sys.stdout = output

#compares the newly created file with the existing library "commonwords.txt"
    file=open("thesis/library/commonwords.txt", 'r')
    lines=file.readlines()
#prints the logical output
    for output in output:
        for line in lines:
            if  output  in  line:
                 print(decrypt)
            else:
                 print("Could not decrypt")
   

             
    subprocess.call(["caesar cipher/output.txt", "caesar cipher/commonwords.txt"])

#Removes the output file after finish each decryption 


#EXample: "I am a student"  "J bn b tuvefou"  shift by 1
"""