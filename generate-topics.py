## generate-topics.py
import ollama
import os

MODEL_TYPE = "gemma"


lesson_title = input("Input a Lesson Title Here:")

with open('topic_routes.py', 'a') as file:
    file.write('\n')  
    file.write('@app.route("/' + lesson_title + '")\n')
    file.write('def index():\n')
    file.write('\treturn render_template("hello.html")\n')
    file.write('\n')




response = ollama.chat(model=MODEL_TYPE, messages=[
  {
    'role': 'user',
    'content': 'Can you give me an introductionary sentence about ' + lesson_title + '',
  },
])


print(response['message']['content']) 

