## Generate Topics



import os 
import shutil
import json
from ollama import generate




'''
@docs
------
In this section this is where we are able to make global variables 
here which has boolean statements to disable and enable functions
in the code for maintainability and efficiency


'''

global_variable_checking        = True
lesson_title                    = True
create_new_gen_dir              = True
create_new_gen_views            = True                                  




'''
@docs
------

In this section this allows the ability to make if statements to make sure  

'''




if global_variable_checking:
        if lesson_title:
                print("The Lesson Title Checking is Enabled ")
        else: 
                print("The Lesson Title Checking is Disabled")


else:
        print("Global Variable Checking is disabled")








lesson_title = input("Please input a lesson title")


print(lesson_title)



'''
@docs   
Once the user enters the title of the lesson_title, then it will use perl to find the "generate starts here"
comment and replace into a button.
'''
# os.system(f"perl -pi -e 's/<!-- generate starts here -->/<button class=\"FOIL-button-regular color-is-blue\">" + lesson_title + "<\/button>\\n\\n\\n <!-- generate starts here -->/g' templates/main_menu.html")

'''
@docs
Once the user enters the title of the lesson_title, then it will use perl to find the "generate starts here"
comment and generates the routing.
'''

os.system(f"perl -pi -e 's/## generate starts here/ he is here\n\n\n\n ## generate starts here/g' index.py") 




## Allows the ability to create a dir new generation
create_new_gen_dir = os.system("mkdir templates/new-topic")

## Allows the ability to create a file new generation
create_new_gen_views = os.system("touch templates/new-topic/index.html") + os.system("touch templates/new-topic/introduction.html") + os.system("touch templates/new-topic/01.html") + os.system("touch templates/new-topic/02.html") + os.system("touch templates/new-topic/03.html") + os.system("touch templates/new-topic/04.html")











'''
@docs
-----

This is for the splashscreen

'''


with open('templates/new-topic/index.html', 'w') as file:
        GLOBAL_BACKGROUND_COLOR = "red"
        GLOBAL_FONT_FAMILY = "Arial, sans-serif"
        GLOBAL_FONT_COLOR  = "#fff"

        file.write('''<!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="refresh" content="10; url=/#" />
        <link rel="stylesheet" href="" type="text/css">
        <style>
                body {
                margin: 0;
                padding: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                background-color:''' + GLOBAL_BACKGROUND_COLOR + ''';
                font-family:''' + GLOBAL_FONT_FAMILY + ''';
                color: #fff;
                }

                .splash-screen {
                text-align: center;
                animation-name: splashscreen;
                animation-duration: 4s;
                }

                .logo {
                font-size: 4rem;
                font-weight: bold;
                margin-bottom: 1rem;
                animation-name: logoanimate;
                animation-duration: 5s;
                }

                .tagline {
                font-size: 1.5rem;
                opacity: 0.7;
                }

                @keyframes splashscreen {
                from {
                        padding: 100px;
                        transform: scale(50);
                        background-color: rgb(255, 255, 255);
                }

                to {
                        background-color: #1a1a1a;
                }
                }

                @keyframes logoanimate {
                from {
                        transform: scale(40);
                        opacity: 1;
                        color: #fff;
                }

                to {
                        transform: scale(1);
                        opacity: 1;
                        color: #fff;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
                }
                }
        </style>
        <title>Splash Screen</title>
        </head>
        <body>
        <div class="splash-screen">
                <div class="logo">Smith-Pad</div>
                <div class="tagline"></div>
        </div>
        </body>
        </html>''')




'''
@docs 

This is for the first page

'''


with open('templates/new-topic/01.html', 'w') as file:

     

        file.write('''
        {% include './System_Files/system.global.ui.include.ui.html' %}
        {% include 'template-new-refreshed/gradient-config/begin.html' %}  
        ''')




        file.write('''

        <div class="bar">
        <a href="{{}}" class="osui-button">Home &#9750;</a>
        <a href="{{}}" class="osui-button">Back &#9750;</a>
        <a href="{{}}" class="osui-button">Next &rArr; </a>
        <a href="#" class="osui-button" onClick="Calculator=window.open( '../../../../APPS/calculator.html','Calculator', 'width=600,height=1000'); return false;">Launch Calculator</a>
        </div>
        
        ''')


        introduction_1 = generate('gemma', 'Hey, ' + 'could you provide a concise summary tailored for kids? About the' + lesson_title + 'Keep it under five sentences, and please ensure its appropriate for their age group. ' + 'Thanks!')['response']
        print(introduction_1 + "\n\n\n")


        introduction_2_ask = generate('gemma', 'Can you ask that are you ready to learn for kids under 3 sentences?')['response']
        print(introduction_2_ask + "\n\n\n")


        # file.write('''<div class="bar">''' + introduction_1 + '''<ul></ul>''' + introduction_2_ask + '''<ul></ul> </div>''')








'''
@docs 

This is for the 2nd page

'''



with open('templates/new-topic/02.html', 'w') as file:

        file.write('''
        {% include './System_Files/system.global.ui.include.ui.html' %}
        {% include 'template-new-refreshed/gradient-config/begin.html' %}  
        ''')




        file.write('''

        # <div class="bar">
        # <a href="{{}}" class="osui-button">Home &#9750;</a>
        # <a href="{{}}" class="osui-button">Back &#9750;</a>
        # <a href="{{}}" class="osui-button">Next &rArr; </a>
        # <a href="#" class="osui-button" onClick="Calculator=window.open( '../../../../APPS/calculator.html','Calculator', 'width=600,height=1000'); return false;">Launch Calculator</a>
        # </div>        
        
        ''')



        file.write('''

        <div class="bar">
        <a href="{{}}" class="osui-button">Home &#9750;</a>
        <a href="{{}}" class="osui-button">Back &#9750;</a>
        <a href="{{}}" class="osui-button">Next &rArr; </a>
        <a href="#" class="osui-button" onClick="Calculator=window.open( '../../../../APPS/calculator.html','Calculator', 'width=600,height=1000'); return false;">Launch Calculator</a>
        </div>
        
        ''')


        introduction_1 = generate('gemma', 'Hey, ' + 'could you provide a concise summary tailored for kids? About the' + lesson_title + 'Keep it under five sentences, and please ensure its appropriate for their age group. ' + 'Thanks!')['response']
        print(introduction_1 + "\n\n\n")


        introduction_2_ask = generate('gemma', 'Can you ask that are you ready to learn for kids under 3 sentences?')['response']
        print(introduction_2_ask + "\n\n\n")


        # file.write('''<div class="bar">''' + introduction_1 + '''<ul></ul>''' + introduction_2_ask + '''<ul></ul> </div>''')








