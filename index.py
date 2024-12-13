
'''
This is where we import the modules
'''

from flask import Flask, redirect,url_for,render_template                       ## Import the flask library
import os                                                                       ## Import the standard OS library
import json                                                                     ## Import the json library

app = Flask(__name__)



'''
This is where we initialize the routes via subjects generation
via routes.py
'''
from routes import main_routes
app.register_blueprint(main_routes)





@app.route("/")
def index():
        return render_template('SPLASHSCREEN/index.html')


@app.route("/main_menu")
def main_menu():
        return render_template('main_menu.html')


@app.route("/settings_menu")
def settings_menu():
        return render_template('settings.html')

if __name__ == "__main__":
    app.run(debug=True)
