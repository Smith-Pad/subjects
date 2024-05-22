## Generate Topics



import os 
import shutil
from ollama import generate




os.system("cp -R templates/template-new-refreshed templates/abouttorename")
lesson_title = input("Enter the topic name: ")
lesson_title = lesson_title.replace(" ", "_")
os.system(f"mv templates/abouttorename templates/{lesson_title}")



firstOne = generate('gemma', 'Can you summarize the alphabet song for kids under 5 sentences?')['response']
print(firstOne + "\n\n\n")




os.system(f"perl -pi -e 's/content generation starts here/{response}/g' templates/{lesson_title}/01.html")