## Generate Topics



import os 
import shutil
import json
from ollama import generate

# print('''
# # ██╗░░██╗
# # ██║░░██║
# # ███████║
# # ██╔══██║
# # ██║░░██║
# # ╚═╝░░╚═╝
# ''')

# os.system("sleep 1")
# os.system("clear")


# print(''')
# ██╗░░██╗███████╗
# ██║░░██║██╔════╝
# ███████║█████╗░░
# ██╔══██║██╔══╝░░
# ██║░░██║███████╗
# ╚═╝░░╚═╝╚══════╝
# ''')

# os.system("sleep 0.4")
# os.system("clear")

# print(''')
# ██╗░░██╗███████╗██╗░░░░░
# ██║░░██║██╔════╝██║░░░░░
# ███████║█████╗░░██║░░░░░
# ██╔══██║██╔══╝░░██║░░░░░
# ██║░░██║███████╗███████╗
# ╚═╝░░╚═╝╚══════╝╚══════╝
# ''')

# os.system("sleep 0.3")
# os.system("clear")



# print(''')
# ██╗░░██╗███████╗██╗░░░░░██╗░░░░░
# ██║░░██║██╔════╝██║░░░░░██║░░░░░
# ███████║█████╗░░██║░░░░░██║░░░░░
# ██╔══██║██╔══╝░░██║░░░░░██║░░░░░
# ██║░░██║███████╗███████╗███████╗
# ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝
# ''')

# os.system("sleep 0.2")
# os.system("clear")

# print(''')
# ██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░
# ██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗
# ███████║█████╗░░██║░░░░░██║░░░░░██║░░██║
# ██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║
# ██║░░██║███████╗███████╗███████╗╚█████╔╝
# ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░
# ''')

# os.system("sleep 5")
# os.system("clear")

# os.system("cp -R templates/template-new-refreshed templates/abouttorename")

# lesson_title = input('''
# # ███████╗███╗░░██╗████████╗███████╗██████╗░  ████████╗██╗████████╗██╗░░░░░███████╗
# # ██╔════╝████╗░██║╚══██╔══╝██╔════╝██╔══██╗  ╚══██╔══╝██║╚══██╔══╝██║░░░░░██╔════╝
# # █████╗░░██╔██╗██║░░░██║░░░█████╗░░██████╔╝  ░░░██║░░░██║░░░██║░░░██║░░░░░█████╗░░
# # ██╔══╝░░██║╚████║░░░██║░░░██╔══╝░░██╔══██╗  ░░░██║░░░██║░░░██║░░░██║░░░░░██╔══╝░░
# # ███████╗██║░╚███║░░░██║░░░███████╗██║░░██║  ░░░██║░░░██║░░░██║░░░███████╗███████╗
# # ╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝

# # ██╗░░██╗███████╗██████╗░███████╗
# # ██║░░██║██╔════╝██╔══██╗██╔════╝
# # ███████║█████╗░░██████╔╝█████╗░░
# # ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
# # ██║░░██║███████╗██║░░██║███████╗
# # ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝
# ''')


# lesson_title = lesson_title.replace(" ", "_")


# os.system(f"mv templates/abouttorename templates/{lesson_title}")




# firstOne = generate('gemma', 'Can you summarize the alphabet song for kids under 5 sentences?')['response']
# print(firstOne + "\n\n\n")




lesson_title = input("Please input a lesson title")


print(lesson_title)

# os.system(f"perl -pi -e 's/<!-- generate starts here -->/<button class=\"FOIL-button-regular color-is-blue\">" + lesson_title + "<\/button>\\n\\n\\n <!-- generate starts here -->/g' templates/main_menu.html")






os.system("mkdir templates/new-topic")


os.system("touch templates/new-topic/index.html")
os.system("touch templates/new-topic/introduction.html")
os.system("touch templates/new-topic/01.html")
os.system("touch templates/new-topic/02.html")
os.system("touch templates/new-topic/03.html")
os.system("touch templates/new-topic/04.html")







GLOBAL_BACKGROUND_COLOR = "red"
GLOBAL_FONT_FAMILY = "Arial, sans-serif"
GLOBAL_FONT_COLOR  = "#fff"



'''
@docs
-----

This is for the splashscreen

'''


with open('templates/new-topic/index.html', 'w') as file:
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

        <div class="bar">
        <a href="{{route_1_home}}" class="osui-button">Home &#9750;</a>
        <a href="{{route_1_back}}" class="osui-button">Back &#9750;</a>
        <a href="{{route_1_next}}" class="osui-button">Next &rArr; </a>
        <a href="#" class="osui-button" onClick="Calculator=window.open( '../../../../APPS/calculator.html','Calculator', 'width=600,height=1000'); return false;">Launch Calculator</a>
        </div>
        
        ''')


        introduction_1 = generate('gemma', 'Hey, ' + 'could you provide a concise summary tailored for kids? About the' + lesson_title + 'Keep it under five sentences, and please ensure its appropriate for their age group. ' + 'Thanks!')['response']
        print(introduction_1 + "\n\n\n")


        introduction_2_ask = generate('gemma', 'Can you ask that are you ready to learn for kids under 3 sentences?')['response']
        print(introduction_2_ask + "\n\n\n")


        file.write('''<div class="bar">''' + introduction_1 + '''<ul></ul>''' + introduction_2_ask + '''<ul></ul> </div>''')








'''
@docs 

This is for the 2nd page

'''



with open('templates/new-topic/02.html', 'w') as file:
        file.write("<div class=\"bar\">")
        file.write("<a href=\"{{route_2_home}}\" class=\"osui-button\">Home &#9750;</a>")
        file.write("<a href=\"{{route_2_back}}\" class=\"osui-button\">Back &#9750;</a>")
        file.write("<a href=\"{{route_2_next}}\" class=\"osui-button\">Next &rArr; </a>")
        file.write("<a href=\"#\" class=\"osui-button\" onClick=\"Calculator=window.open( '../../../../APPS/calculator.html','Calculator', 'width=600,height=1000'); return false;\">Launch Calculator</a>")
        file.write("</div>")


        introduction_1 = generate('gemma', 'Hey, ' + 'could you provide a concise summary tailored for kids? About the' + lesson_title + 'Keep it under five sentences, and please ensure its appropriate for their age group. ' + 'Thanks!')['response']
        print(introduction_1 + "\n\n\n")


        introduction_2_ask = generate('gemma', 'Can you ask that are you ready to learn for kids under 3 sentences?')['response']
        print(introduction_2_ask + "\n\n\n")


        file.write('''<div class="bar">''' + introduction_1 + '''<ul></ul>''' + introduction_2_ask + '''<ul></ul> </div>''')








