from flask import Flask, redirect,url_for,render_template                       ## Import the flask library
import os                                                                       ## Import the standard OS library
import json                                                                     ## Import the json library

from topic_routes import routingsystem 


app = Flask(__name__)

###############################################################################
#
#
#
#
#
#
#
#
#
###############################################################################
#           Splash Screen View 
###############################################################################
@app.route("/")
def index():
        return render_template('index.html')
###############################################################################
#           Main Menu Screen  
###############################################################################
@app.route("/main_menu")
def main_menu():
        return render_template('main_menu.html')












"""
Sample Lessons are here
"""

@app.route("/sample_lesson_001")
def sample_lesson_001():
        return render_template('_Lesson-Template_/index.html')


@app.route("/sample_lesson_002")
def sample_lesson_002():
        return render_template('_Lesson-Template_/game_menu.html')



@app.route("/sample_lesson_003")
def sample_lesson_003():
        return render_template('_Lesson-Template_/introduction.html')



@app.route("/sample_lesson_004")
def sample_lesson_004():
        return render_template('_Lesson-Template_/01.html')



@app.route("/sample_lesson_005")
def sample_lesson_005():
        return render_template('_Lesson-Template_/02.html')



@app.route("/sample_lesson_006")
def sample_lesson_006():
        return render_template('_Lesson-Template_/03.html')



app.register_blueprint(routingsystem)


if __name__ == '__main__':
        app.run(debug=True)
