'''
generate-subject-generation-compat-checker.py

'''




import os
import sys
from ollama import generate
import platform





## This is where we initialize platform.system to manipulate files 
## based on the operating system that is using currently using 
## in the backend. 
FILE_MANIPULATION_OS_COMPAT = platform.system()



## This is where we initialize platform.system to manipulate dirs
## based on the operating system that is currently using in the 
## backend
DIR_MANIPULATION_OS_COMPAT  = platform.system()

## This is where we are able to create if statements to detect
## which operating system is using currently to manipulate generation
## files. 

if FILE_MANIPULATION_OS_COMPAT == "Windows":
    print("do an action")


if FILE_MANIPULATION_OS_COMPAT == "Darwin":
    print("do an action")



if FILE_MANIPULATION_OS_COMPAT == "Linux":
    print("do an action")
