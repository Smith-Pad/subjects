## generate-topics.py
import ollama
import os
import shutil



lesson_title = input("Input a Lesson Title Here: ")

'''
------
@docs
------

This is where you are able to change the type of model here. 
'''

MODEL_TYPE = "gemma"


widget_menu_response = ollama.chat(model=MODEL_TYPE, messages=[
  {
    'role': 'user',
    'content': "Can you give me a summary sentence on the" + lesson_title +  "Explain like I'm a five year old learning how to"
  },
])

output_html = widget_menu_response['message']['content']


os.system("perl -pi -e 's{generate starts here}{<div class=\"widget-boxes-init\"><div class=\"widget-boxes-header-title\"><h1>" + lesson_title + "</h1><div class=\"widget-boxes-header-description\">" + str(output_html)  + "<h2> Blah blah blah </h2> <button class=''osui-button''>lesson title</button></div></div></div> \n\n generate starts here}g' templates/main_menu.html")

'''
@docs 
-------
This allows the ability to copy the template-new-refreshed to the 
specified subject generation. 
'''

template_dir = "templates/template-new-refreshed"
new_dir = "templates/" + lesson_title
shutil.copytree(template_dir, new_dir)
os.rename(new_dir, "templates/" + lesson_title)