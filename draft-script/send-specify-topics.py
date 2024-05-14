## send-specify-topics.py



import os 
import sys

'''
@doc 
-----
These are the global variables which are declared on the top 
for efficient and maintainability purposes. 

'''

variable        = 0
fold_variable   = 0



fold_variable = input("Please specify the subject generation to send to the generation template path [[[[- = space]]]]")
os.system(f"cp -R {fold_variable} /templates/")
