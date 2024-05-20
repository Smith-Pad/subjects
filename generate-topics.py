## Generate Topics



import os 
import shutil


os.system("cp -R templates/template-new-refreshed templates/abouttorename")

lesson_title = input("Enter the topic name: ")
lesson_title = lesson_title.replace(" ", "_")

os.system(f"mv templates/abouttorename templates/{lesson_title}")

os.system(f"perl -pi -e 's/content generation starts here/hello words/g' templates/{lesson_title}/01.html")
