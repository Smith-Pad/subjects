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
        file.write('<!DOCTYPE html>')
        file.write('<html lang="en">')

        file.write('<head>')
        file.write('<meta charset="UTF-8">')
        file.write('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
        file.write('<meta http-equiv="refresh" content="10; url=/#" />')
        file.write('<link rel="stylesheet" href="" type="text/css">')
        file.write('<style>')
        file.write('body {')
        file.write('margin: 0;')
        file.write('padding: 0;')
        file.write('display: flex;')
        file.write('justify-content: center;')
        file.write('align-items: center;')
        file.write('min-height: 100vh;')
        file.write('background-color:' + GLOBAL_BACKGROUND_COLOR + ';')
        file.write('font-family:' + GLOBAL_FONT_FAMILY + ';')
        file.write('color: #fff;')
        file.write('}')

        file.write('.splash-screen {')
        file.write('text-align: center;')
        file.write('animation-name: splashscreen;')
        file.write('animation-duration: 4s;')
        file.write('}')

        file.write('.logo {')
        file.write('font-size: 4rem;')
        file.write('font-weight: bold;')
        file.write('margin-bottom: 1rem;')
        file.write('animation-name: logoanimate;')
        file.write('animation-duration: 5s;')
        file.write('}')

        file.write('.tagline {')
        file.write('font-size: 1.5rem;')
        file.write('opacity: 0.7;')
        file.write('}')

        file.write('@keyframes splashscreen {')
        file.write('from {')
        file.write('padding: 100px;')
        file.write('transform: scale(50);')
        file.write('background-color: rgb(255, 255, 255);')
        file.write('}')

        file.write('to {')
        file.write('background-color: #1a1a1a;')
        file.write('}')
        file.write('}')

        file.write('@keyframes logoanimate {')
        file.write('from {')
        file.write('transform: scale(40);')
        file.write('opacity: 1;')
        file.write('color: #fff;')
        file.write('}')

        file.write('to {')
        file.write('transform: scale(1);')
        file.write('opacity: 1;')
        file.write('color: #fff;')
        file.write('box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);')
        file.write('}')
        file.write('}')
        file.write('</style>')
        file.write('<title>Splash Screen</title>')
        file.write('</head>')

        file.write('<body>')
        file.write('<div class="splash-screen">')
        file.write('<div class="logo">Smith-Pad</div>')
        file.write('<div class="tagline"></div>')
        file.write('</div>')
        file.write('</body>')
        file.write('</html>')



'''
@docs 

This is for the first page

'''


with open('templates/new-topic/01.html', 'w') as file:
        file.write("<div class=\"bar\">")
        file.write("<a href=\"{{route_1_home}}\" class=\"osui-button\">Home &#9750;</a>")
        file.write("<a href=\"{{route_1_back}}\" class=\"osui-button\">Back &#9750;</a>")
        file.write("<a href=\"{{route_1_next}}\" class=\"osui-button\">Next &rArr; </a>")
        file.write("<a href=\"#\" class=\"osui-button\" onClick=\"Calculator=window.open( '../../../../APPS/calculator.html','Calculator', 'width=600,height=1000'); return false;\">Launch Calculator</a>")
        file.write("</div>")


        introduction_1 = generate('gemma', 'Hey, ' + 'could you provide a concise summary tailored for kids? About the' + lesson_title + 'Keep it under five sentences, and please ensure its appropriate for their age group. ' + 'Thanks!')['response']
        print(introduction_1 + "\n\n\n")


        introduction_2_ask = generate('gemma', 'Can you ask that are you ready to learn for kids under 3 sentences?')['response']
        print(introduction_2_ask + "\n\n\n")


        file.write("<div class=\"bar\">")
        file.write(introduction_1)
        file.write('<ul></ul>')
        file.write(introduction_2_ask)
        file.write('<ul></ul>')
        file.write("</div>")







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


        file.write("<div class=\"bar\">")
        file.write(introduction_1)
        file.write('<ul></ul>')
        file.write(introduction_2_ask)
        file.write('<ul></ul>')
        file.write("</div>")








