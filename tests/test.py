
'''
Import the standard libraries
'''

import os                                                       ## import the standard 
import subprocess                                               ## import the standard
from ollama import generate                                     ## import ollama


# for i in range(2):





firstOne = generate('gemma', 'Summarize the alphabet song for kids in under 5 sentences')['response']
print(firstOne + "\n\n\n")                                      



# subprocess.run(
#         f"perl -pi -e \"s/<!-- generate starts here -->/<div>{firstOne}<\\/div>\\n\\n\\n\\n <!-- generate starts here -->/g\" test-content.html",
#         shell=True
# )
