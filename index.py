from flask import Flask, redirect,url_for,render_template                       ## Import the flask library
import os                                                                       ## Import the standard OS library
import json                                                                     ## Import the json library

from topic_routes import routingsystem


app = Flask(__name__)

@app.route("/")
def index():
        return render_template('SPLASHSCREEN/index.html')


@app.route("/main_menu")
def main_menu():
        return render_template('main_menu.html')


@app.route('/game_ui_test')
def game_ui_test():
        return render_template('template-new-refreshed/index.html')



@app.route('/game_ui_test_begin')
def game_ui_test_begin():
        return render_template('template-new-refreshed/begin.html')

if __name__ == '__main__':
        app.run(debug=True)
