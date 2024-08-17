'''
generate-file-generation-manipulation-test.py
'''

import os
import sys
from ollama import generate
import platform


FILE_MANIPULATION_OS_COMPAT = platform.system()


if FILE_MANIPULATION_OS_COMPAT == "Windows":
    print("Currently Using Windows for File Manipulation")


if FILE_MANIPULATION_OS_COMPAT == "Darwin":
    print("Currently Using macOS for File Manipulation")



if FILE_MANIPULATION_OS_COMPAT == "Linux":
    print("Currently Using Linux for File Manipulation")