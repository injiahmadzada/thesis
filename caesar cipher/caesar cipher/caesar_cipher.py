#implementaion of machine learning to decrypt the caesar cipher 
 #the program should analyse all brute force results and find the logical one to output


 #brute force attack
import sys
import subprocess

message = input("Enter a message: ")  # user inputs message
offset = 0


  
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
 
    output="caesar cipher/output.txt"      
    sys.stdout=open(output, 'w')

    file=open("caesar cipher/commonwords.txt", 'r')
    lines=file.readlines()

    for output in output:
        for line in lines:
            if  output  in  line:
                 print(decrypt)
            else:
                 print("Could not decrypt")
   

             
    subprocess.call(["caesar cipher/output.txt", "caesar cipher/commonwords.txt"])



#"I am a student"  "J bn b tuvefou"  shift by 1