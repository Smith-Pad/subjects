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





with open(GENERATION_ROUTES_ROUTING, 'a') as fd:
    fd.write(f'''
# routes.py

from flask import Blueprint


main_routes = Blueprint('main', __name__)


@main_routes.route("/{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}")
def {TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}():
    return '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="Refresh" content="5; url=\\'./02.html\\'"><title>Splash Screen</title><style>body{{margin:0;padding:0;display:flex;justify-content:center;align-items:center;min-height:100vh;background:#303030;font-family:Arial,sans-serif;color:#fff;overflow:hidden}}.splash-screen{{position:relative;text-align:center;animation:fadeOut 4s forwards 6s}}.logo{{font-size:4rem;font-weight:bold;margin-bottom:1rem;animation:blob-morph 6s infinite ease-in-out}}.tagline{{font-size:1.5rem;opacity:0.8;animation:fadeIn 3s ease-in-out 2s forwards;opacity:0}}.background-blobs{{position:absolute;top:50%;left:50%;width:100vw;height:100vh;z-index:-1;overflow:hidden;transform:translate(-50%,-50%)}}.blob{{position:absolute;width:400px;height:400px;border-radius:50%;filter:blur(100px);animation:moveBlobs 20s infinite ease-in-out}}.blob-red{{background:linear-gradient(135deg,#ff7eb3,#ff758c);top:15%;left:20%;animation-delay:0s}}.blob-blue{{background:linear-gradient(135deg,#7eafff,#758cff);top:50%;left:80%;animation-delay:6s}}.blob-yellow{{background:linear-gradient(135deg,#ffc77e,#ffba75);top:70%;left:30%;animation-delay:12s}}@keyframes moveBlobs{{0%,100%{{transform:translate(0,0) scale(1)}}25%{{transform:translate(-20px,-30px) scale(1.1)}}50%{{transform:translate(30px,20px) scale(0.9)}}75%{{transform:translate(-15px,25px) scale(1.05)}}}}@keyframes fadeIn{{0%{{opacity:0}}100%{{opacity:1}}}}@keyframes fadeOut{{0%{{opacity:1}}100%{{opacity:0;pointer-events:none}}</style></head><body><div class="splash-screen"><div class="logo">Smith-Pad</div><div class="tagline">Presents</div></div><div class="background-blobs"><div class="blob blob-red"></div><div class="blob blob-blue"></div><div class="blob blob-yellow"></div></div></body></html>'
    ''')



## Create the generations directory
os.system("mkdir -pv templates/GENERATIONS")

## copies templates to lesson title underscore
os.system("cp -R Subjects-VA-1.0.2-prototype " + TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES)

## move lesson title underscroe to templates/ folder. (Make another folder for .gitignore to be recognized.)
os.system("mv " + TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES + " templates/GENERATIONS")


with open(GENERATION_ROUTES_ROUTING, 'a') as fd:
    fd.write(f'''
# routes.py

from flask import Blueprint


main_routes = Blueprint('main', __name__)


@main_routes.route("/{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}")
def {TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}():
    return render_template("sdf.html", message=message)
    ''')