## add-assignments.py

## This is where you are able to import the required libraries
import os
import sys
import json


## Initial creation
os.system("touch routes.py")


## This is where you are able to target the source to create the assignments to
GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE = "templates/latest-assignments-cards.html"


GENERATION_ROUTES_ROUTING = "routes.py"


## This is where the para is prompted to enter the title of the lesson
TITLE_OF_LESSON = input("Create the title of the lesson:        ")


TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES = TITLE_OF_LESSON.replace(" ", "_")


## This is the where the para is prompted to enter the description of the lesson
DESCRIPTION_OF_LESSON = input("Create the description of the lesson:         ")


with open(GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE, 'a') as fd:
    fd.write(f'')



with open(GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE, 'a') as fd:
    fd.write(f'''

        <!-- Materialize CSS -->
        <link href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css" rel="stylesheet">
        <!-- Materialize JavaScript -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/js/materialize.min.js"></script>
        <!-- jQuery (required by Materialize) -->
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

      <div class="col s12 m3">
        <div class="card blue-grey darken-1">
          <div class="card-content white-text">
            <span class="card-title">{TITLE_OF_LESSON}</span>
            <p>{DESCRIPTION_OF_LESSON}</p>
          </div>
          <div class="card-action">
              <md-filled-button onclick="location.href='/{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}'">Ready Fredy</md-filled-button>
          </div>
        </div>
      </div>
    ''')




'''
This will include the libraries for the things
'''
with open(GENERATION_ROUTES_ROUTING, 'a') as fd:
    fd.write(f'''
# routes.py

from flask import Blueprint, render_template


main_routes = Blueprint('main', __name__)


    ''')




## This will make a new line for the routes.py file
with open(GENERATION_ROUTES_ROUTING, 'a') as fd:
    fd.write(f'''

        \n\n\n\n\n\n\n\n\n\n\n

    ''')