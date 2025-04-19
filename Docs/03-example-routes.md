# Example Routes


In this documentation, here are the examples of how `routes.py` works.

For the `hello` use this reference as a reference point where generations
routes go. 



In the `04-add--assignments.py` file, 



```` py

from flask import Blueprint, render_template

main_routes = Blueprint('main', __name__)

@main_routes.route("/hello")
def hello():
    return render_template('hello/index.html')




@main_routes.route("/hello_game_menu")
def hello_game_menu():
    title = "MENU HERE"
    return render_template('hello/game-menu.html', title=title)





@main_routes.route("/hello_01")
def hello_01():
    text = ""
    return render_template('hello/01.html')
````