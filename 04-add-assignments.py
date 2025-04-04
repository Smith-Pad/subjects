## add-assignments.py

## This is where you are able to import the required libraries
import os
import sys
import json
import ollama


os.system("touch routes.py")



GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE = "templates/latest-assignments-cards.html"
GENERATION_ROUTES_ROUTING = "routes.py"
TITLE_OF_LESSON = input("Create the title of the lesson:        ")
TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES = TITLE_OF_LESSON.replace(" ", "_")
DESCRIPTION_OF_LESSON = input("Create the description of the lesson:         ")