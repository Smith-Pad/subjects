from flask import Flask, redirect,url_for,render_template                       ## Import the flask library
import os                                                                       ## Import the standard OS library
import json                                                                     ## Import the json library


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


## generate starts here


if __name__ == '__main__':
        app.run(debug=True)
