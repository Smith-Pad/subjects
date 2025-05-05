####################################################################################
##                          Add-Assignments
####################################################################################


import os                                                                                       
import sys
import json
import ollama

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



#
# @access
# This allows the ability to make use of TITLE_OF_LESSON variable
# and add it as a Card that is categorized to the Latest Assignments
# section.
#

with open('./templates/latest-assignments-cards.html', 'a') as fd:
fd.write(f'''\n\n\n\n\n
<div class="widget">
        <h1> {TITLE_OF_LESSON} </h1>
        <ul></ul>
        {DESCRIPTION_OF_LESSON}
</div>
        ''')