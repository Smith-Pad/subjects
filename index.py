from flask import Flask, redirect,url_for,render_template                                                                                                               ## Import the flask library
import os                                                                                                                                                               ## Import the standard OS library
import json                                                                                                                                                             ## Import the json library



app = Flask(__name__)



@app.route("/")
def index():
        return render_template('index.html')


if __name__ == '__main__':
        app.run(debug=True)
