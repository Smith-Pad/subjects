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




os.system("clear")
TITLE_OF_LESSON = input('''
--------------------------------------------------------------
                Enter the title of lesson
--------------------------------------------------------------

>> ''')





TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES = TITLE_OF_LESSON.replace(" ", "_")



os.system("clear")
DESCRIPTION_OF_LESSON = input('''
--------------------------------------------------------------
                Enter the description of lesson
--------------------------------------------------------------

>> ''')

# with open('./templates/latest-assignments-cards.html', 'a') as fd:
# fd.write(f'''\n\n\n\n\n
# <div class="widget">
#         <h1> {TITLE_OF_LESSON} </h1>
#         <ul></ul>
#         {TITLE_OF_LESSON}
# </div>
#         ''')




with open('./templates/latest-assignments-cards.html', 'a') as fd:fd.write(f'''\n\n\n\n\n<div class="widget"><h1> {TITLE_OF_LESSON} </h1><ul></ul>{TITLE_OF_LESSON}</div>''')








# with open('routes.py', 'a') as fd:
#         fd.write(f''' 
# @main_routes.route("/{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}")
# def {TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}():
#     return render_template ('{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}/index.html')
#         ''')



## Generate SplashScreen Route

# with open('routes.py', 'a') as fd:
#         fd.write(f''' 
# @main_routes.route("/{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}")
# def {TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}():
#     return render_template ('{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}/index.html')
#         ''')




# with open('routes.py', 'a') as fd:fd.write(f'\n\n')


# ## Generate Game Menu Route

# with open('routes.py', 'a') as fd:
#         fd.write(f''' 
# @main_routes.route("/{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}")
# def {TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}():
#     return render_template ('{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}/game-menu.html')
#         ''')




# with open('routes.py', 'a') as fd:fd.write(f'\n\n')


# os.system(f"cp -R Lesson-Topic-Testing  {TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}")
# os.system(f"mv {TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES} templates/")
