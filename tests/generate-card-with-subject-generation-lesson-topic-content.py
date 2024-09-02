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



'''
Now, this is where we need to remove the directory, which is used to 
prevent any conflicts.

'''
os.system("cd ../templates && rm -rf _generation_backend_txt_content_")


'''
Now, this is where we need to create a directory inside the 
[]../templates/] directory so that the backend components, such as 
the text components can be recognized. Later, on there will be an 
if statement for which native OS it is using. 

Now, we need to create a subdirectory inside the  _generation_backend_txt_content_ 
based on the lesson title that the teacher/paraprofessional has prompted.

'''


os.system("cd ../templates && mkdir _generation_backend_txt_content_ && cd _generation_backend_txt_content_ && mkdir helloworld")

