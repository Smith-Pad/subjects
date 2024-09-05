'''
generate-card-with-subject-generation-lesson-topic-content.py

'''


import os
import sys
from ollama import generate
import platform


'''
------------------------------------------------
ENTER THE LESSON TITLE OF THE LESSON
------------------------------------------------
'''


# Prompt the user to enter the lesson title of the lesson
print("Input the Lesson Title\n\n\n")

## Listens to the input
lesson_title = input("")


'''
------------------------------------------------
ENTER THE LESSON DESCRIPTION OF THE LESSON
------------------------------------------------
'''

# Prompt the user to enter the Lesson Description
print("Input the Lesson Description\n\n\n")

## Listens to the description input
lesson_description = input("")


## Convert the lesson title spaces to underscores
lesson_title_underscore_convert = lesson_title.replace(' ', '_')




'''
------------------------------------------------
GENERATE THE LATEST ASSIGNMENT CARDS
------------------------------------------------
'''


## This is where you need to retrieve the local source
GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE = "../templates/_latest.assignments.cards.html"



## This is where it takes a new line space in the latest assignment add cards source
with open(GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE, 'a') as fd:
    fd.write(f'\n\n\n\n\n')


## This is where we are able to create a latest assignment cards based on the keystroke
## from the teacher/paraprofessional
with open(GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE, 'a') as fd:
    fd.write(f'''
      <div class="col s12 m3">
        <div class="card blue-grey darken-1">
          <div class="card-content white-text">
            <span class="card-title">{lesson_title}</span>
            <p>{lesson_description}</p>
          </div>
          <div class="card-action">
              <md-filled-button>Ready Fredy</md-filled-button>
          </div>
        </div>
      </div>
    
    ''')



## This is where we are able to create the components directly from the lesson_title_underscore_convert variable

## Create introduction.txt
os.system("touch " + lesson_title_underscore_convert + "_generate_" + "introduction" + ".txt")


## Create what-is-it.txt
os.system("touch " + lesson_title_underscore_convert + "_generate_" + "what-is-it" + ".txt")


## Create view-1.txt
os.system("touch " + lesson_title_underscore_convert + "_generate_" + "view-1" + ".txt")



## Create view-2.txt
os.system("touch " + lesson_title_underscore_convert + "_generate_" + "view-2" + ".txt")



## Create view-3.txt
os.system("touch " + lesson_title_underscore_convert + "_generate_" + "view-3" + ".txt")


## Create view-4.txt
os.system("touch " + lesson_title_underscore_convert + "_generate_" + "view-4" + ".txt")



## Create view-5.txt
os.system("touch " + lesson_title_underscore_convert + "_generate_" + "view-5" + ".txt")