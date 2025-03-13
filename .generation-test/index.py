
'''
This is where we import the modules
'''

from flask import Flask, redirect,url_for,render_template                       ## Import the flask library
import os                                                                       ## Import the standard OS library
import json                                                                     ## Import the json library
import getpass                                                                  ## Import the getpass library
import time                                                                     ## Import the time library
import pytest                                                                   ## Import the pytest library

app = Flask(__name__)


'''
This is where we initialize the routes via subjects generation
via routes.py
'''
from routes import main_routes
app.register_blueprint(main_routes)



## Get the current username from the OS
username = getpass.getuser()



'''
@docs
This is where the client will able to see the splashscreen of Smith-Pad.
'''

@app.route("/")
def index():
        return render_template('SPLASHSCREEN/index.html')


'''
@docs
In the main menu, this is where the client will able to select the two buttons
which is latest-assignments and past assignments.
'''

@app.route("/main_menu")
def main_menu():
        username = getpass.getuser()
        return render_template('main_menu.html' , username=username)


'''
@docs
In the latest-assignments view, this is where all the assignments will be
assigned
'''
@app.route("/latest_assignments_list")
def latest_assignments_list():
        return render_template('latest-assignments-list.html')

'''
@docs
In the past assignments view, this is where all the assignments will be moved
once the assignments has been completed.
'''

@app.route("/past_assignments_list")
def past_assignments_list():
        return render_template('past-assignments-list.html')


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
