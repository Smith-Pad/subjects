## add-assignments.py
# In this sub-repository, this is used to generate a subject generation.
# However, this is separated to avoid conflicts in general.



import os
import json
import random
import math
import ollama


os.system("touch routes.py")
os.system("mkdir templates/ && cd templates/ && touch latest-assignments-cards.html")


TITLE_OF_LESSON                                 = 0                                                                                                     ## variable for title of lesson variable
TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES        = 0                                                                                                     ## translate to underscores to get flask to be recognized
DESCRIPTION_OF_LESSON                           = 0                                                                                                     ## allow the ability to add description of lesson 


TITLE_OF_LESSON = input("Create the title of the lesson: ")
TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES = TITLE_OF_LESSON.replace(" ", "_")
DESCRIPTION_OF_LESSON = input("Create the description of the lesson: ")


LESSON_TITLE_VIEW_READY_FOR_INTERACTIVE_GAME_CONFIRM =  TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES + "_READY_FOR_INTERACTIVE_GAME_CONFIRM"






####################################################################################################################################

with open("templates/latest-assignments-cards.html", 'a') as fd:
    fd.write(f'<div style="background-color: red;">{TITLE_OF_LESSON}</div>\n\n\n')
    fd.write(f'<div style="background-color: yellow;">{DESCRIPTION_OF_LESSON}</div>\n\n\n')


####################################################################################################################################

with open("routes.py", 'a') as fd:
    fd.write(f'''
@main_routes.route("/firstpage_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}")
def firstpage_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}():
    return '<h1> Game Menu </h1>'
    ''')

####################################################################################################################################