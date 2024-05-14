## generate-topics.py
import ollama
import os
import shutil



# lesson_title = input("Input a Lesson Title Here: ")

# template_dir = "templates/template-new-refreshed"


# new_dir = "templates/" + lesson_title


# shutil.copytree(template_dir, new_dir)


# os.rename(new_dir, "templates/" + lesson_title)




# lesson_title_file = input("Enter the title of lesson file\n\n")
# os.system("sed -i '' 's/<h1>hello<\/h1>/" + "<h1>" + lesson_title_file + "<\/h1>/g' testing.html")





# os.system("sed -i '' \"s/<p align='center'>hello<\/p>/<p align='center'>" + lesson_title_file + "<\/p>/g\" testing.html")



################################################################
##              This used to find and replace the files
################################################################



os.system("sed -i '' \"s/hello/world/g\" testout.txt")


################################################################
##              This is for the topic route
################################################################

# with open('topic_routes.py', 'a') as file:
#     file.write('\n')  
#     file.write('@app.route("/' + lesson_title + '")\n')
#     file.write('def index():\n')
#     file.write('\treturn render_template("hello.html")\n')
#     file.write('\n')



# response = ollama.chat(model=MODEL_TYPE, messages=[
#   {
#     'role': 'user',
#     'content': 'Can you give me an introductionary sentence about ' + lesson_title + '',
#   },
# ])


# print(response['message']['content']) 