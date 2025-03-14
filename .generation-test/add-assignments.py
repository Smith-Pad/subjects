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


TITLE_OF_LESSON = input("Create the title of the lesson: ")                                                                                             ## get the user to enter the title of the lesson
TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES = TITLE_OF_LESSON.replace(" ", "_")                                                                            ## translate spaces into underscores
DESCRIPTION_OF_LESSON = input("Create the description of the lesson: ")                                                                                 ## get the user to enter the description of the lesson


LESSON_TITLE_VIEW_READY_FOR_INTERACTIVE_GAME_CONFIRM =  TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES + "_READY_FOR_INTERACTIVE_GAME_CONFIRM"

## HTML PART PREVIEW PART PREVIEW 
# <h1> Game Menu </h1><ul></ul><a href="introduction_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES} ">introduction</a>
# <h1> Introduction </h1><ul></ul><a href="1_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES} ">1</a>
# <h1> 1 </h1><ul></ul><a href="2_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES} ">Next</a>
# <h1> 2 </h1><ul></ul><a href="3_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES} ">Next</a>
# <h1> 3 </h1><ul></ul><a href="4_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES} ">Next</a>
# <h1> 4 </h1><ul></ul><a href="5_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES} ">Next</a>
# <h1> 5 </h1><ul></ul><a href="6_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES} ">Next</a>
# <h1>options</h1><button> Enable</button><button> Disable</button>







with open("templates/latest-assignments-cards.html", 'a') as fd:
    fd.write(f'<div style="background-color: red;">{TITLE_OF_LESSON}</div>\n\n\n')
    fd.write(f'<div style="background-color: yellow;">{DESCRIPTION_OF_LESSON}</div>\n\n\n')


with open("routes.py", 'a') as fd:
    fd.write(f'''
@main_routes.route("/gamemenu_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}")
def gamemenu_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}():
    return '<h1> Game Menu </h1><ul></ul><a href="introduction_{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}">introduction</a>'
    ''')