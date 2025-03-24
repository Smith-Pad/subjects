## activate-routes.sh

## This is a required script allowing the ability to activate the routing
## system for subjects.



touch routes.py


echo """
from flask import Blueprint, render_template


main_routes = Blueprint('main', __name__)

# @main_routes.route("/uiui")
# def uiui():
#     return render_template('uiui.html')


""" >> routes.py
