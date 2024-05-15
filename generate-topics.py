## generate-topics.py
import ollama
import os
import shutil



lesson_title = input("Input a Lesson Title Here: ")

# template_dir = "templates/template-new-refreshed"
# new_dir = "templates/" + lesson_title
# shutil.copytree(template_dir, new_dir)
# os.rename(new_dir, "templates/" + lesson_title)









# os.system("sed -i '' \"s/<p align='center'>hello<\/p>/<p align='center'>" + lesson_title_file + "<\/p>/g\" testing.html")



################################################################
##        This is used to update the main_menu.html content
################################################################




########################################################################
#                   Training Methods
#
#           
########################################################################


########################################################################
# Subject Generation Levels           
########################################################################

# LEVEL_1 = "true"
# LEVEL_2 = "true"
# LEVEL_3 = "true"
# LEVEL_4 = "true"
# LEVEL_5 = "true"


################################################################
##   GLOBAL TRAINING VARIABLES
################################################################

MODEL_TYPE = "gemma"
MAIN_MENU_WIDGET_BUTTON_DESCRIPTION_QUESTION = "Can you give me an summary sentence on the "
LEVEL_1 = "Explain like I'm a five year old learning how to" + MAIN_MENU_WIDGET_BUTTON_DESCRIPTION_QUESTION


response = ollama.chat(model=MODEL_TYPE, messages=[
  {
    'role': 'user',
    'content': MAIN_MENU_WIDGET_BUTTON_DESCRIPTION_QUESTION + lesson_title + LEVEL_1,
  },
])

output_html = response['message']['content']

## This generates a widget button for the main_menu.html for the topic
os.system("perl -pi -e 's{generate starts here}{<div class=\"widget-boxes-init\"><div class=\"widget-boxes-header-title\"><h1>" + lesson_title + "</h1><div class=\"widget-boxes-header-description\">" + str(output_html)  + "<h2> Blah blah blah </h2></div></div></div> \n\n generate starts here}g' templates/main_menu.html")











################################################################
##              NOT NEEDED
################################################################



# lesson_title_file = input("Enter the title of lesson file\n\n")
# os.system("sed -i '' 's/<h1>hello<\/h1>/" + "<h1>" + lesson_title_file + "<\/h1>/g' testing.html")



# MODEL_TYPE = "gemma"

# response = ollama.chat(model=MODEL_TYPE, messages=[
#   {
#     'role': 'user',
#     'content': 'Can you give me an summary sentence on the ' + lesson_title + '',
#   },
# ])

# output_html = print(response['message']['content']) 
# print(output_html)
# os.system("touch hello.txt")
# os.system("echo '" + output_html + "' >> hello.txt")
# os.system("sed -i '' \"s/generate starts here./generate starts now/g\" templates/main_menu.html")



################################################################
##              This is for the topic route
################################################################



# with open('topic_routes.py', 'a') as file:
#     file.write('\n')  
#     file.write('@app.route("/' + lesson_title + '")\n')
#     file.write('def index():\n')
#     file.write('\treturn render_template("hello.html")\n')
#     file.write('\n')
