## specify topics


## What is the reason for this script? Well, since the lesson topics are all going to be 
## in the templates generation path

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



'''
@doc 
-----
Prompt the user to specify the subject generation path name. 

The requirement for the user to do when specifying the path name is 
the dash as a space instead of a space. 


EG: 
    template-new-refreshed



'''
fold_variable = input("Please specify the subject generation [[[[- = space]]]]")
os.system(f"ln -sf templates/{fold_variable} .")
os.system(f"echo '{fold_variable}' >> .gitignore")
