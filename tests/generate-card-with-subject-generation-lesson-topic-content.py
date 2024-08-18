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



## This is where we are able to create the backend content here
BACKEND_CONTENT_SOURCE_DIR = "../templates/_generation_backend_txt_content"

## This is where we create the directory of the backend content 
## txt source
os.mkdir(BACKEND_CONTENT_SOURCE_DIR)




## This is where we are able to create the txt files for the subject
## generation backend content txt files
BACKEND_CONTENT_SOURCE_FILE_INTRODUCTION = "../templates/_generation_backend_txt_content/introduction.txt"
BACKEND_CONTENT_SOURCE_FILE_CHAPTER_1 = "../templates/_generation_backend_txt_content/chapter1.txt"
BACKEND_CONTENT_SOURCE_FILE_CHAPTER_2 = "../templates/_generation_backend_txt_content/chapter2.txt"
BACKEND_CONTENT_SOURCE_FILE_CHAPTER_3 = "../templates/_generation_backend_txt_content/chapter3.txt"




## This is where we are able to create the files with the with statement
with open('GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE_FILE_INTRODUCTION', 'a') as fd:
    fd.write(f'hello world ')