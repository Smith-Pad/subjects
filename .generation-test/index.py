
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
        return 'Subjects Main'


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
