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
        return render_template('_________SPLASHSCREEN_______________/index.html')
###############################################################################
#           Main Menu Screen  
###############################################################################
@app.route("/main_menu")
def main_menu():
        return render_template('main_menu.html')












"""
Sample Lessons are here

This is used for debugging purposes. 
"""

@app.route("/sample_lesson_001")
def sample_lesson_001():
        return render_template('_________NEW_TEMPLATE_______________/_________NEW_TEMPLATE_ONE___________/index.html')


@app.route("/sample_lesson_002")
def sample_lesson_002():
        return render_template('_________NEW_TEMPLATE_______________/_________NEW_TEMPLATE_ONE___________/game_menu.html')



@app.route("/sample_lesson_003")
def sample_lesson_003():
        return render_template('_________NEW_TEMPLATE_______________/_________NEW_TEMPLATE_ONE___________/introduction.html')



@app.route("/sample_lesson_004")
def sample_lesson_004():
        return render_template('_________NEW_TEMPLATE_______________/_________NEW_TEMPLATE_ONE___________/01.html')



@app.route("/sample_lesson_005")
def sample_lesson_005():
        return render_template('_________NEW_TEMPLATE_______________/_________NEW_TEMPLATE_ONE___________/02.html')



@app.route("/sample_lesson_006")
def sample_lesson_006():
        return render_template('_________NEW_TEMPLATE_______________/_________NEW_TEMPLATE_ONE___________/03.html')







@app.route("/sample_lesson_0001")
def sample_lesson_0001():
        return render_template('_________NEW_TEMPLATE_______________/_________NEW_TEMPLATE_TWO___________/index.html')


@app.route("/sample_lesson_0002")
def sample_lesson_0002():
        return render_template('_________NEW_TEMPLATE_______________/_________NEW_TEMPLATE_TWO___________/game_menu.html')



@app.route("/sample_lesson_0003")
def sample_lesson_0003():
        return render_template('_________NEW_TEMPLATE_______________/_________NEW_TEMPLATE_TWO___________/introduction.html')



@app.route("/sample_lesson_0004")
def sample_lesson_0004():
        return render_template('_________NEW_TEMPLATE_______________/_________NEW_TEMPLATE_TWO___________/01.html')



@app.route("/sample_lesson_0005")
def sample_lesson_0005():
        return render_template('_________NEW_TEMPLATE_______________/_________NEW_TEMPLATE_TWO___________/02.html')



@app.route("/sample_lesson_0006")
def sample_lesson_0006():
        return render_template('_________NEW_TEMPLATE_______________/_________NEW_TEMPLATE_TWO___________/03.html')









# @app.route("/sample_lesson_0001")
# def sample_lesson_0001():
#         return render_template('_Lesson-Template_/index.html')


# @app.route("/sample_lesson_0002")
# def sample_lesson_0002():
#         return render_template('_Lesson-Template_/game_menu.html')



# @app.route("/sample_lesson_0003")
# def sample_lesson_0003():
#         return render_template('_Lesson-Template_/introduction.html')



# @app.route("/sample_lesson_0004")
# def sample_lesson_0004():
#         return render_template('_Lesson-Template_/01.html')



# @app.route("/sample_lesson_0005")
# def sample_lesson_0005():
#         return render_template('_Lesson-Template_/02.html')



# @app.route("/sample_lesson_0006")
# def sample_lesson_0006():
#         return render_template('_Lesson-Template_/03.html')



app.register_blueprint(routingsystem)


if __name__ == '__main__':
        app.run(debug=True)
