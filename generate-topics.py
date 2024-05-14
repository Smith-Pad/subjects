## generate-topics.py
import ollama
import os

'''
---------------------------
VARIABLE CONFIGURATIONS
---------------------------
'''
MODEL_TYPE = "gemma"                     ## This is where you are able to set the model 


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



'''
-----
@docs
-----
'''

lesson_title = input("Input a Lesson Title Here\n\n\n---\n\n----\t\t")

'''
------
@docs
------
'''


with open('topic_routes.py', 'a') as file:
    file.write('\n')  
    file.write('@app.route("/' + lesson_title + '")\n')
    file.write('def index():\n')
    file.write('\treturn render_template("hello.html")\n')
    file.write('\n')


'''
------
@docs
------
In this section, this allows the ability to dynamically ask LLM's 

'''

response = ollama.chat(model=MODEL_TYPE, messages=[
  {
    'role': 'user',
    'content': 'Can you give me an introductionary sentence about ' + lesson_title + '',
  },
])


'''
------
@docs
------
'''



print(response['message']['content']) 

