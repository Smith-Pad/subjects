####################################################################################
##                          Add-Assignments
####################################################################################

## This is where you are able to import the required libraries
import os                                                                                       ## Import os
import sys                                                                                      ## Import standard library
import json                                                                                     ## Import standard library
import ollama                                                                                   ## Import the ollama library

os.system("touch routes.py")



GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE = "templates/latest-assignments-cards.html"
GENERATION_ROUTES_ROUTING = "routes.py"


#############################################################################
# -----
# Docs:
# ------
## Make the user create the title of the lesson
#############################################################################

os.system("clear")
TITLE_OF_LESSON = input('''
--------------------------------------------------------------
                Enter the title of lesson
--------------------------------------------------------------

>> ''')


#############################################################################
# -----
# Docs:
# ------
## Using the TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES, this allows the ability
## to translate from spaces to underscores for flask to understand in general
#############################################################################


TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES = TITLE_OF_LESSON.replace(" ", "_")

#############################################################################
# -----
# Docs:
# ------
## Make the user create the description of the lesson
#############################################################################

os.system("clear")
DESCRIPTION_OF_LESSON = input('''
--------------------------------------------------------------
                Enter the description of lesson
--------------------------------------------------------------

>> ''')


#############################################################################
# -----
# Docs:
# ------
## This is where we are able to create routes in general which is located in
## routes.py file
#############################################################################


with open('routes.py', 'a') as fd:
        fd.write(f''' 
@main_routes.route("/{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}")
def {TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}():
    return render_template('{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}.html')
        ''')




with open('routes.py', 'a') as fd:fd.write(f'\n\n')                                        ## Make new line
