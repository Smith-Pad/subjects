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
    file.write('@app.route("/' + lesson_title + '")\n')
    file.write('def index():\n')
    file.write('\treturn render_template("hello.html")\n')
    file.write('\n')

# variable1 = "hello worlds"


#with open('topic_routes.py', 'a') as file: 
#    file.write('\n')
#    file.write('hello' + variable1)
