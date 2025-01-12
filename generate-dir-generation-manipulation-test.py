'''
generate-file-generation-manipulation-test.py
'''

import os
import sys
from ollama import generate
import platform


DIR_MANIPULATION_OS_COMPAT = platform.system()


if DIR_MANIPULATION_OS_COMPAT == "Windows":
    print("Currently Using Windows for Dir Manipulation")


if DIR_MANIPULATION_OS_COMPAT == "Darwin":
    print("Currently Using macOS for Dir Manipulation")



if DIR_MANIPULATION_OS_COMPAT == "Linux":
    print("Currently Using Linux for Dir Manipulation")