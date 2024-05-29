## test-new-dir
## This generator allows the ability to generate subject content 
## generation on Smith-Pad 

## 2024 RA FOIL 


import os
import sys
import json


'''
@docs right here, this allows the ability to create the directory
'''
def makeDir():
        os.system("mkdir new-subjects")


def createSysFile():
        os.system("touch new-subjects/index.html")
        os.system("touch new-subjects/introduction.html")
        os.system("touch new-subjects/01.html")
        os.system("touch new-subjects/02.html")
        os.system("touch new-subjects/03.html")
        os.system("touch new-subjects/04.html")
        os.system("touch new-subjects/04.html")


def createContent():
        ## Variables here

        def splashScreen():
                GLOBAL_BACKGROUND_COLOR = "red"
                GLOBAL_FONT_FAMILY = "Arial, sans-serif"
                GLOBAL_FONT_COLOR  = "#fff"



                with open('new-subjects/index.html', 'w') as file:
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


        splashScreen()

        
        def introductionScreen():
                with open('new-subjects/01.html', 'w') as file:
                        file.write("<div class=\"bar\">")
                        file.write("<a href=\"{{route_1_home}}\" class=\"osui-button\">Home &#9750;</a>")
                        file.write("<a href=\"{{route_1_back}}\" class=\"osui-button\">Back &#9750;</a>")
                        file.write("<a href=\"{{route_1_next}}\" class=\"osui-button\">Next &rArr; </a>")
                        file.write("<a href=\"#\" class=\"osui-button\" onClick=\"Calculator=window.open( '../../../../APPS/calculator.html','Calculator', 'width=600,height=1000'); return false;\">Launch Calculator</a>")
                        file.write("</div>")



        introductionScreen()



        def firstPage():

                with open('new-subjects/02.html', 'w') as file:
                        # file.write("<a href=\"/d\">Link Text</a>")
                        file.write("<div class=\"bar\">")
                        file.write("<a href=\"{{route_2_home}}\" class=\"osui-button\">Home &#9750;</a>")
                        file.write("<a href=\"{{route_2_back}}\" class=\"osui-button\">Back &#9750;</a>")
                        file.write("<a href=\"{{route_2_next}}\" class=\"osui-button\">Next &rArr; </a>")
                        file.write("<a href=\"#\" class=\"osui-button\" onClick=\"Calculator=window.open( '../../../../APPS/calculator.html','Calculator', 'width=600,height=1000'); return false;\">Launch Calculator</a>")
                        file.write("</div>")



        firstPage()



        def secondPage():

                with open('new-subjects/03.html', 'w') as file:
                        # file.write("<a href=\"/d\">Link Text</a>")
                        file.write("<div class=\"bar\">")
                        file.write("<a href=\"{{route_3_home}}\" class=\"osui-button\">Home &#9750;</a>")
                        file.write("<a href=\"{{route_3_back}}\" class=\"osui-button\">Back &#9750;</a>")
                        file.write("<a href=\"{{route_3_next}}\" class=\"osui-button\">Next &rArr; </a>")
                        file.write("<a href=\"#\" class=\"osui-button\" onClick=\"Calculator=window.open( '../../../../APPS/calculator.html','Calculator', 'width=600,height=1000'); return false;\">Launch Calculator</a>")
                        file.write("</div>")



        secondPage()




        def thirdPage():

                with open('new-subjects/04.html', 'w') as file:
                        # file.write("<a href=\"/d\">Link Text</a>")
                        file.write("<div class=\"bar\">")
                        file.write("<a href=\"{{route_4_home}}\" class=\"osui-button\">Home &#9750;</a>")
                        file.write("<a href=\"{{route_4_back}}\" class=\"osui-button\">Back &#9750;</a>")
                        file.write("<a href=\"{{route_4_next}}\" class=\"osui-button\">Next &rArr; </a>")
                        file.write("<a href=\"#\" class=\"osui-button\" onClick=\"Calculator=window.open( '../../../../APPS/calculator.html','Calculator', 'width=600,height=1000'); return false;\">Launch Calculator</a>")
                        file.write("</div>")



        thirdPage()



        def fourthPage():

                with open('new-subjects/05.html', 'w') as file:
                        # file.write("<a href=\"/d\">Link Text</a>")
                        file.write("<div class=\"bar\">")
                        file.write("<a href=\"{{route_5_home}}\" class=\"osui-button\">Home &#9750;</a>")
                        file.write("<a href=\"{{route_5_back}}\" class=\"osui-button\">Back &#9750;</a>")
                        file.write("<a href=\"{{route_5_next}}\" class=\"osui-button\">Next &rArr; </a>")
                        file.write("<a href=\"#\" class=\"osui-button\" onClick=\"Calculator=window.open( '../../../../APPS/calculator.html','Calculator', 'width=600,height=1000'); return false;\">Launch Calculator</a>")
                        file.write("</div>")



        fourthPage()




makeDir()
createSysFile()
createContent()
