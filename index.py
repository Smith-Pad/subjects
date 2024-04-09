from flask import Flask, redirect,url_for,render_template                       ## Import the flask library
import os                                                                       ## Import the standard OS library
import json                                                                     ## Import the json library

from topic_routes import routingsystem 
from topic_routes_testing import routingsystemtesting


app = Flask(__name__)

@app.route("/")
def index():
        return render_template('SPLASHSCREEN/index.html')


@app.route("/main_menu")
def main_menu():
        return render_template('main_menu.html')



"""
Sample Lessons are here

This is used for debugging purposes. 
"""

@app.route("/sample_lesson_001")
def sample_lesson_001():
        return render_template('_________NEW_TEMPLATE_ONE___________/index.html')


@app.route("/sample_lesson_002")
def sample_lesson_002():
        return render_template('_________NEW_TEMPLATE_ONE___________/game_menu.html')



@app.route("/sample_lesson_003")
def sample_lesson_003():
        return render_template('_________NEW_TEMPLATE_ONE___________/introduction.html')



@app.route("/sample_lesson_004")
def sample_lesson_004():
        return render_template('_________NEW_TEMPLATE_ONE___________/01.html')



@app.route("/sample_lesson_005")
def sample_lesson_005():
        return render_template('_________NEW_TEMPLATE_ONE___________/02.html')



@app.route("/sample_lesson_006")
def sample_lesson_006():
        return render_template('_________NEW_TEMPLATE_ONE___________/03.html')



app.register_blueprint(routingsystem)
app.register_blueprint(routingsystemtesting)


if __name__ == '__main__':
        app.run(debug=True)
