## add-assignments.py
# In this sub-repository, this is used to generate a subject generation.
# However, this is separated to avoid conflicts in general.



import os
import json
import random
import math
import ollama


os.system("touch routes.py")
os.system("mkdir templates/ && cd templates/ && touch latest-assignments-cards.html")


TITLE_OF_LESSON = input("Create the title of the lesson: ")
TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES = TITLE_OF_LESSON.replace(" ", "_")
DESCRIPTION_OF_LESSON = input("Create the description of the lesson: ")



LESSON_TITLE_VIEW_INTRO =  TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES + "_INTRO"

LESSON_TITLE_VIEW_2 =  TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES + "_2"
LESSON_TITLE_VIEW_3 =  TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES + "_3"
LESSON_TITLE_VIEW_4 =  TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES + "_4"
LESSON_TITLE_VIEW_5 =  TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES + "_5"
LESSON_TITLE_VIEW_6 =  TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES + "_6"
LESSON_TITLE_VIEW_7 =  TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES + "_7"

## Used for Game Confirmation before going to a interactive game.
LESSON_TITLE_VIEW_READY_FOR_INTERACTIVE_GAME_CONFIRM =  TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES + "_READY_FOR_INTERACTIVE_GAME_CONFIRM"

################################################################################################
## @DOCS
## Allows the ability to show the latest lessons and notifies the latest assignments via D-Bus 
## daemon or other daemon in other OSs.
##
## @EG:
##      [Manual Command]
##      notify-send("⚠️Latest Assignment: {TITLE_OF_LESSON} is ready")
##
##
##
################################################################################################

with open("templates/latest-assignments-cards.html", 'a') as fd:
    fd.write(f'<div style="background-color: red;">{TITLE_OF_LESSON}</div>\n\n\n')
    fd.write(f'<div style="background-color: yellow;">{DESCRIPTION_OF_LESSON}</div>\n\n\n')

################################################################################################
## @DOCS
## This is for the splashscreen. Later on, you are able to use the sound version of the Splashscreen
################################################################################################

with open("routes.py", 'a') as fd:
    fd.write(f'''
# Splashscreen

@main_routes.route("/{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}")
def {TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}():
    return '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="Refresh" content="5; url=\\'./{LESSON_TITLE_VIEW_INTRO}\\'"><title>Splash Screen</title><style>body{{margin:0;padding:0;display:flex;justify-content:center; align-items:center;min-height:100vh;background:#303030;font-family:Arial,sans-serif;color:#fff;overflow:hidden}}.splash-screen{{position:relative;text-align:center;animation:fadeOut 4s forwards 6s}}.logo{{font-size:4rem;font-weight:bold;margin-bottom:1rem;animation:blob-morph 6s infinite ease-in-out}}.tagline{{font-size:1.5rem;opacity:0.8;animation:fadeIn 3s ease-in-out 2s forwards;opacity:0}}.background-blobs{{position:absolute;top:50%;left:50%;width:100vw;height:100vh;z-index:-1;overflow:hidden;transform:translate(-50%,-50%)}}.blob{{position:absolute;width:400px;height:400px;border-radius:50%;filter:blur(100px);animation:moveBlobs 20s infinite ease-in-out}}.blob-red{{background:linear-gradient(135deg,#ff7eb3,#ff758c);top:15%;left:20%;animation-delay:0s}}.blob-blue{{background:linear-gradient(135deg,#7eafff,#758cff);top:50%;left:80%;animation-delay:6s}}.blob-yellow{{background:linear-gradient(135deg,#ffc77e,#ffba75);top:70%;left:30%;animation-delay:12s}}@keyframes moveBlobs{{0%,100%{{transform:translate(0,0) scale(1)}}25%{{transform:translate(-20px,-30px) scale(1.1)}}50%{{transform:translate(30px,20px) scale(0.9)}}75%{{transform:translate(-15px,25px) scale(1.05)}}}}@keyframes fadeIn{{0%{{opacity:0}}100%{{opacity:1}}}}@keyframes fadeOut{{0%{{opacity:1}}100%{{opacity:0;pointer-events:none}}</style></head><body><div class="splash-screen"><div class="logo">Smith-Pad</div><div class="tagline">Presents</div></div><div class="background-blobs"><div class="blob blob-red"></div><div class="blob blob-blue"></div><div class="blob blob-yellow"></div></div></body></html>'
    ''')



'''
This is where ollama talks in general
'''




# with open(GENERATION_ROUTES_ROUTING, 'a') as fd:
#     fd.write(f'''
# # routes.py

# from flask import Blueprint


# main_routes = Blueprint('main', __name__)


# @main_routes.route("/{TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}")
# def {TRANSLATE_TITLE_OF_LESSON_TO_UNDERSCORES}():
#     return '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta http-equiv="Refresh" content="5; url=\\'./02.html\\'"><title>Splash Screen</title><style>body{{margin:0;padding:0;display:flex;justify-content:center;align-items:center;min-height:100vh;background:#303030;font-family:Arial,sans-serif;color:#fff;overflow:hidden}}.splash-screen{{position:relative;text-align:center;animation:fadeOut 4s forwards 6s}}.logo{{font-size:4rem;font-weight:bold;margin-bottom:1rem;animation:blob-morph 6s infinite ease-in-out}}.tagline{{font-size:1.5rem;opacity:0.8;animation:fadeIn 3s ease-in-out 2s forwards;opacity:0}}.background-blobs{{position:absolute;top:50%;left:50%;width:100vw;height:100vh;z-index:-1;overflow:hidden;transform:translate(-50%,-50%)}}.blob{{position:absolute;width:400px;height:400px;border-radius:50%;filter:blur(100px);animation:moveBlobs 20s infinite ease-in-out}}.blob-red{{background:linear-gradient(135deg,#ff7eb3,#ff758c);top:15%;left:20%;animation-delay:0s}}.blob-blue{{background:linear-gradient(135deg,#7eafff,#758cff);top:50%;left:80%;animation-delay:6s}}.blob-yellow{{background:linear-gradient(135deg,#ffc77e,#ffba75);top:70%;left:30%;animation-delay:12s}}@keyframes moveBlobs{{0%,100%{{transform:translate(0,0) scale(1)}}25%{{transform:translate(-20px,-30px) scale(1.1)}}50%{{transform:translate(30px,20px) scale(0.9)}}75%{{transform:translate(-15px,25px) scale(1.05)}}}}@keyframes fadeIn{{0%{{opacity:0}}100%{{opacity:1}}}}@keyframes fadeOut{{0%{{opacity:1}}100%{{opacity:0;pointer-events:none}}</style></head><body><div class="splash-screen"><div class="logo">Smith-Pad</div><div class="tagline">Presents</div></div><div class="background-blobs"><div class="blob blob-red"></div><div class="blob blob-blue"></div><div class="blob blob-yellow"></div></div></body></html>'
#     ''')