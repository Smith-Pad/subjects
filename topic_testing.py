'''
topic_testing.py

This particular implementation is used to create topic user interfaces for testing purposes.
'''


from flask import Blueprint, render_template


## Initialize the routing system blueprint for the subjects route
routingsystem = Blueprint('routingsystem', __name__, template_folder='lesson-topics')




'''
This is where the routes will dynamically be generated here. For now, 
for the Pliot II, this will be manually generated. 

'''
@routingsystem.route('/hello')
def hello():
    return render_template('hello.html')