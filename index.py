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



@app.route('/game_ui_test_01')
def game_ui_test_01():
        return render_template('template-new-refreshed/01.html')



@app.route('/game_ui_test_02')
def game_ui_test_02():
        return render_template('template-new-refreshed/02.html')




@app.route('/game_ui_test_03')
def game_ui_test_03():
        return render_template('template-new-refreshed/03.html')



@app.route('/game_ui_test_04')
def game_ui_test_04():
        return render_template('template-new-refreshed/04.html')



@app.route('/game_ui_test_05')
def game_ui_test_05():
        return render_template('template-new-refreshed/05.html')



@app.route('/game_ui_test_06')
def game_ui_test_06():
        return render_template('template-new-refreshed/06.html')



@app.route('/game_ui_test_07')
def game_ui_test_07():
        return render_template('template-new-refreshed/07.html')



if __name__ == '__main__':
        app.run(debug=True)
