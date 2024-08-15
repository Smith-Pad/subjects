'''
  ____            _ _   _           ____           _ 
 / ___| _ __ ___ (_) |_| |__       |  _ \ __ _  __| |
 \___ \| '_ ` _ \| | __| '_ \ _____| |_) / _` |/ _` |
  ___) | | | | | | | |_| | | |_____|  __/ (_| | (_| |
 |____/|_| |_| |_|_|\__|_| |_|     |_|   \__,_|\__,_|
                                            test.py
'''



import os                                                       ## import the standard 
import subprocess                                               ## import the standard
from ollama import generate                                     ## import ollama
import platform                                                 ## import platform




## This is used for compatibility usages
create_file = platform.system()                                  ## Used for create files within cross platform





# if create_file == 'Windows':
    # os.system('powershell New-Item -Path "..\\templates\\_subjects_generation_txt_backend_\\hello.txt" -ItemType File')
    # os.system('powershell New-Item -Path "..\\templates\\_subjects_generation_txt_backend_\\anotherhello.txt" -ItemType File')


os.remove("../templates/_subjects_generation_txt_backend_/hello.txt")
os.remove("../templates/_subjects_generation_txt_backend_/anotherhello.txt")



firstOne = generate('0ssamaak0/xtuner-llava:llama3-8b-v1.1-int4', 'Make an introduction of algebra that is designed for high schooler.')['response']
print(firstOne + "\n\n\n")

secondOne = generate('0ssamaak0/xtuner-llava:llama3-8b-v1.1-int4', 'Make steps on how to solve basic algebra for a high schooler. You need to be like a teacher and instructor for the students.')['response']
print(firstOne + "\n\n\n")



with open('../templates/_subjects_generation_txt_backend_/hello.txt', 'a') as file:
    file.write(f'{firstOne}\n\n\n')
    
    
with open('../templates/_subjects_generation_txt_backend_/anotherhello.txt', 'a') as file:
    file.write(f'{secondOne}\n\n\n')    















'''
OTHER NOTES RIGHT HERE
'''
############################################################################################################################################
# high_school_prompt = "Can you give me a favor? I want to make an introduction of algebra that is designed for high schooler."
# middle_school_prompt = "Can you give me a favor? I want to make an introduction of algebra that is designed for middle schooler."
# elementary_school_prompt = "Can you give me a favor? I want to make an introduction of algebra that is designed for elementary schooler."
############################################################################################################################################
