'''
topic_routes.py

This particular implementation of routes for the subjects topic section 
of the Subjects feature of Smith-Pad
'''


from flask import Blueprint, render_template


## Initialize the routing system blueprint for the subjects route
routingsystem = Blueprint('routingsystem', __name__, template_folder='lesson-topics')