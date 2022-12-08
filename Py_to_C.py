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
cFile = open("test.c", "a+")       #opening the test.c file to append and read in it 
cFile.truncate(0)   #Erasing the file data 
print("INSTRICTIONS - \n1. After Pressing Enter key you will not be able to edit previous line.\n2. Type 'exit' when you are done programming.\nLet's Code Together:D \n\n")

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
    subprocess.call(["gcc", "test.c","-o","a"])   #executing the statement to compile the C file 
    subprocess.call("./a.exe")      #Executing the C file