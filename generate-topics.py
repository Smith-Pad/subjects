## generate-topics.py
import ollama
import os

print('''

                                                                                                                          
$$$$$$$$\ $$\   $$\     $$\                                                                                               
\__$$  __|\__|  $$ |    $$ |                                                                                              
   $$ |   $$\ $$$$$$\   $$ | $$$$$$\                                                                                      
   $$ |   $$ |\_$$  _|  $$ |$$  __$$\                                                                                     
   $$ |   $$ |  $$ |    $$ |$$$$$$$$ |                                                                                    
   $$ |   $$ |  $$ |$$\ $$ |$$   ____|                                                                                    
   $$ |   $$ |  \$$$$  |$$ |\$$$$$$$\                                                                                     
   \__|   \__|   \____/ \__| \_______|                                                                                    
                                                                                                                          
                                                                                                                          
''')

lesson_title = input("Input a Lesson Title Here\n\n\n---\n\n----\t\t")


with open('topic_routes.py', 'a') as file:
    file.write('\n')  
    file.write('@app.route("/")\n')
    file.write('@app.route(')')
    file.write('def index():\n')
    file.write('\t\treturn render_template("hello world")')
    file.write('\n\n\n')