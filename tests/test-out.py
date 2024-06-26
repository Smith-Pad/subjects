import os 
import shutil
import json
from ollama import generate

lesson_title_enabled = True
route_search_text_enabled = True
route_replace_text_enabled = True
route_replacer_enabled = True
llm_generation = True





lesson_title = input("Input title: ")
lesson_title = lesson_title.replace(" ", "_")
llm_generation = generate('gemma', 'Hey, ' + 'could you provide a concise summary tailored for kids? About the' + lesson_title + 'Keep it under five sentences, and please ensure its appropriate for their age group. ' + 'Thanks!')['response']
print(llm_generation + "\n\n\n")
route_search_text = "## generate starts here"


route_replace_text = f"""
## Splash Screen Generated
@app.route('/{lesson_title}')
def {lesson_title}():
    return '''
    <link rel="stylesheet" href="/static/GENERATE.css">
    <h1> {llm_generation} </h1>
    <h2> {llm_generation} </h2>
    <h3> {llm_generation} </h3>
    <h4> {llm_generation} </h4>
    <h5> {llm_generation} </h5>
    '''


## Begin
@app.route('/{lesson_title}_begin')
def {lesson_title}_begin():
    return '''
    <link rel="stylesheet" href="/static/GENERATE.css">
    <h1> {llm_generation} </h1>
    <h2> {llm_generation} </h2>
    <h3> {llm_generation} </h3>
    <h4> {llm_generation} </h4>
    <h5> {llm_generation} </h5>
    '''



## View 1
@app.route('/{lesson_title}_01')
def {lesson_title}_01():
    return '''
    <link rel="stylesheet" href="/static/GENERATE.css">
    <h1> {llm_generation} </h1>
    <h2> {llm_generation} </h2>
    <h3> {llm_generation} </h3>
    <h4> {llm_generation} </h4>
    <h5> hello world </h5>
    '''


## View 2
@app.route('/{lesson_title}_02')
def {lesson_title}_02():
    return '''
    <link rel="stylesheet" href="/static/GENERATE.css">
    <h1> {llm_generation} </h1>
    <h2> {llm_generation} </h2>
    <h3> {llm_generation} </h3>
    <h4> {llm_generation} </h4>
    <h5> {llm_generation} </h5>
    '''

## View 3
@app.route('/{lesson_title}_03')
def {lesson_title}_03():
    return "2341"


## View 4
@app.route('/{lesson_title}_04')
def {lesson_title}_04():
    return "231"


## View 5
@app.route('/{lesson_title}_05')
def {lesson_title}_05():
    return "1"
            
""" + "\n\n\n\n## generate starts here"

with open('index.py', 'r+') as file:
    content = file.read().replace(route_search_text, route_replace_text)
    file.seek(0)  
    file.write(content)