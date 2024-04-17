'''
topic_routes_testing.py
'''


from flask import Blueprint, render_template

routinguitests = Blueprint('routinguitests', __name__, template_folder='template')



@routinguitests.route('/hellosdfljlsdkfdjf')
def hellosdfljlsdkfdjf():
        return render_template('02.html')