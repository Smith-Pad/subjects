## Generate Topics



import os 
import shutil
from ollama import generate

## Create dir

os.system("cp -R templates/template-new-refreshed templates/abouttorename")
lesson_title = input("Enter the topic name: ")
lesson_title = lesson_title.replace(" ", "_")
os.system(f"mv templates/abouttorename templates/{lesson_title}")


response = generate('gemma', 'Why is the sky blue? in a short sentence')['response']
print(response)

os.system(f"perl -pi -e 's/content generation starts here/{response}/g' templates/{lesson_title}/01.html")
