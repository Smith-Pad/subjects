## add-assignments.py
# In this sub-repository, this is used to generate a subject generation.
# However, this is separated to avoid conflicts in general.



import os
import json
import random
import math
from ollama import chat
from ollama import ChatResponse


os.system("touch routes.py")
os.system("mkdir templates/ && cd templates/ && touch latest-assignments-cards.html")


TITLE_OF_LESSON                                 = 0                                                                                                     ## variable for title of lesson variable
TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES        = 0                                                                                                     ## translate to underscores to get flask to be recognized
DESCRIPTION_OF_LESSON                           = 0                                                                                                     ## allow the ability to add description of lesson 


TITLE_OF_LESSON = input("Create the title of the lesson: ")                                                                                             ## get the user to enter the title of the lesson
TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES = TITLE_OF_LESSON.replace(" ", "_")                                                                            ## translate spaces into underscores
DESCRIPTION_OF_LESSON = input("Create the description of the lesson: ")                                                                                 ## get the user to enter the description of the lesson


LESSON_TITLE_VIEW_READY_FOR_INTERACTIVE_GAME_CONFIRM =  TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES + "_READY_FOR_INTERACTIVE_GAME_CONFIRM"







with open("templates/latest-assignments-cards.html", 'a') as fd:
    fd.write(f'<div style="background-color: red;">{TITLE_OF_LESSON}</div>\n\n\n')
    fd.write(f'<div style="background-color: yellow;">{DESCRIPTION_OF_LESSON}</div>\n\n\n')


## 1. Route     = ("/a_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}")
## 2. Define    = def a_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}():
## 3. Button    = <a href="a_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}">introduction</a>


routingthings = TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES
print(routingthings)




with open("routes.py", 'a') as fd:
    fd.write(f'''




@main_routes.route("/a_{routingthings}")
def a_{routingthings}():
    return '<h1> A </h1><ul></ul><a href="/b_{routingthings}"> -> B</a>'





@main_routes.route("/b_{routingthings}")
def b_{routingthings}():
    return '<h1> B </h1><ul></ul><a href="/c_{routingthings}"> -> C</a>'




@main_routes.route("/c_{routingthings}")
def c_{routingthings}():
    return '<h1> B </h1><ul></ul><a href="/d_{routingthings}"> -> D</a>'





''')

