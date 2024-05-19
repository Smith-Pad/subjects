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



MAIN_MENU_WIDGET_BUTTON_DESCRIPTION_QUESTION = "Can you give me an summary sentence on the "
LEVEL_1 = "Explain like I'm a five year old learning how to" + MAIN_MENU_WIDGET_BUTTON_DESCRIPTION_QUESTION


response = ollama.chat(model=MODEL_TYPE, messages=[
  {
    'role': 'user',
    'content': MAIN_MENU_WIDGET_BUTTON_DESCRIPTION_QUESTION + lesson_title + LEVEL_1,
  },
])

output_html = response['message']['content']

## This generates a widget button for the main_menu.html for the topic
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