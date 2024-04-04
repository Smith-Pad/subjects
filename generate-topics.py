## generate-topics.py


import os                                                                                           ## import os module




'''
Global Variables
----------------
'''

lesson_title                            = 0
lesson_title_file                       = 0

lesson_title_find                       = 0
lesson_title_replace                    = 0




'''
Inner Variables 
----------------
'''

lesson_title_find    = ""
lesson_title_replace = ""


os.system("clear")
lesson_title = input("Enter the title of the lesson:\n\n")
os.system("echo '" + lesson_title  + "'")
os.system("sed -i '' 's/hello/" + lesson_title + "/g' testing.html")



os.system("clear")
lesson_title_file = input("Enter the title of lesson file\n\n")
os.system("sed -i '' 's/hello/" + lesson_title_file + "/g' testing.html")
