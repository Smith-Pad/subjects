import os 
import sys
from ollama import generate
import platform


## This allows the ability to open the file
f = open("demofile2.txt", "a")
f.write("")
f.close()