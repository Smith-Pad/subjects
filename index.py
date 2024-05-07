from flask import Flask, redirect,url_for,render_template                       ## Import the flask library
import os                                                                       ## Import the standard OS library
import json                                                                     ## Import the json library

from topic_routes import routingsystem


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



@app.route('/game_ui_test_begin')
def game_ui_test_begin():
        return render_template('template-new-refreshed/begin.html')



@app.route('/game_ui_test_01')
def game_ui_test_01():
        route_1_home = "/game_ui_test"
        route_1_back = "/game_ui_test_begin"
        route_1_next = "/game_ui_test_02"
        return render_template('template-new-refreshed/01.html', route_1_home=route_1_home, route_1_back=route_1_back, route_1_next=route_1_next)



@app.route('/game_ui_test_02')
def game_ui_test_02():
        route_2_home = "/game_ui_test"
        route_2_back = "/game_ui_test_01"
        route_2_next = "/game_ui_test_03"
        return render_template('template-new-refreshed/02.html', route_2_home=route_2_home, route_2_back=route_2_back, route_2_next=route_2_next)




@app.route('/game_ui_test_03')
def game_ui_test_03():
        route_3_home = "/game_ui_test"
        route_3_back = "/game_ui_test_02"
        route_3_next = "/game_ui_test_04"
        return render_template('template-new-refreshed/03.html', route_3_home=route_3_home, route_3_back=route_3_back, route_3_next=route_3_next)



@app.route('/game_ui_test_04')
def game_ui_test_04():
        route_4_home = "/game_ui_test"
        route_4_back = "/game_ui_test_03"
        route_4_next = "/game_ui_test_05"
        return render_template('template-new-refreshed/04.html', route_4_home=route_4_home, route_4_back=route_4_back, route_4_next=route_4_next)



@app.route('/game_ui_test_05')
def game_ui_test_05():
        route_5_home = "/game_ui_test"
        route_5_back = "/game_ui_test_04"
        route_5_next = "/game_ui_test_06"
        return render_template('template-new-refreshed/05.html', route_5_home=route_5_home, route_5_back=route_5_back, route_5_next=route_4_next)





if __name__ == '__main__':
        app.run(debug=True)
