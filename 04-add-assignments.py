## add-assignments.py

## This is where you are able to import the required libraries
import os                                                                                       ## Import os
import sys                                                                                      ## Import standard library
import json                                                                                     ## Import standard library
import ollama                                                                                   ## Import the ollama library

os.system("touch routes.py")



GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE = "templates/latest-assignments-cards.html"
GENERATION_ROUTES_ROUTING = "routes.py"


#############################################################################
## Make the user create the title of the lesson
#############################################################################

os.system("clear")
TITLE_OF_LESSON = input('''
--------------------------------------------------------------
                Enter the title of lesson
--------------------------------------------------------------

>> ''')



TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES = TITLE_OF_LESSON.replace(" ", "_")

#############################################################################
## Make the user create the description of the lesson
#############################################################################

os.system("clear")
DESCRIPTION_OF_LESSON = input('''
--------------------------------------------------------------
                Enter the description of lesson
--------------------------------------------------------------

>> ''')


#############################################################################
## This is where we are able to create routes in general
#############################################################################


with open('routes.py', 'a') as fd:
        fd.write(f''' 
@main_routes.route("/{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}")
def {TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}():
    return render_template('{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}.html')
        ''')




with open('routes.py', 'a') as fd:fd.write(f'\n\n')                                        ## Make new line
