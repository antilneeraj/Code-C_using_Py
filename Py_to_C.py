'''
Python Program to write a C program and Execute it
Author : Neeraj
Date : December 6, 2022
'''

import os
import subprocess

os.system("cls")    #clearing the terminal
flag = 0
i = 1
validate = False
validateF = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

while validate is not True:
    Fname = input("Enter a valid C File Name : ").strip().replace(" ", "").lower()
    if not (Fname[0] in validateF) and str(Fname.find(".")) in validateF:
        print("Invalid File Name")
    else:
        validate = True   

cFile = open("{}.c".format(Fname), "a+")       #opening the test.c file to append and read in it 
cFile.truncate(0)   #Erasing the file data 

print("INSTRUCTIONS - \n1. To Run A C file Mingw Should be installed on your system.\n2. After Pressing Enter key you will not be able to edit previous line.\n3. Type 'exit' when you are done programming.\nLet's Code Together:D \n\n")

while i>0:
    inp = input("> ")   #taking input in inp
    if inp == 'exit':         #comparing the value to exit
        break #exiting from while loop
    else:
        cFile.write(inp + "\n")     #appending the code in the file
        flag = 1
cFile.close()

if flag == 1:
    print("\n\nExecuting...\n")
    subprocess.call(["gcc", "{}.c".format(Fname),"-o","a"])   #executing the statement to compile the C file 
    subprocess.call("./a.exe")      #Executing the C file