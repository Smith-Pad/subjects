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
@app.route('/{llm_generation}')
def {llm_generation}():
    return '''
    <link rel="stylesheet" href="/static/GENERATE.css">
    <h1> {llm_generation} </h1>
    <h2> {llm_generation} </h2>
    <h3> {llm_generation} </h3>
    <h4> {llm_generation} </h4>
    <h5> {llm_generation} </h5>
    '''


## Begin
@app.route('/{llm_generation}_begin')
def {llm_generation}_begin():
    return '''
    <link rel="stylesheet" href="/static/GENERATE.css">
    <h1> {llm_generation} </h1>
    <h2> {llm_generation} </h2>
    <h3> {llm_generation} </h3>
    <h4> {llm_generation} </h4>
    <h5> {llm_generation} </h5>
    '''



## View 1
@app.route('/{llm_generation}_01')
def {llm_generation}_01():
    return '''
    <link rel="stylesheet" href="/static/GENERATE.css">
    <h1> {llm_generation} </h1>
    <h2> {llm_generation} </h2>
    <h3> {llm_generation} </h3>
    <h4> {llm_generation} </h4>
    <h5> hello world </h5>
    '''


## View 2
@app.route('/{llm_generation}_02')
def {llm_generation}_02():
    return '''
    <link rel="stylesheet" href="/static/GENERATE.css">
    <h1> {llm_generation} </h1>
    <h2> {llm_generation} </h2>
    <h3> {llm_generation} </h3>
    <h4> {llm_generation} </h4>
    <h5> {llm_generation} </h5>
    '''

## View 3
@app.route('/{llm_generation}_03')
def {llm_generation}_03():
    return "2341"


## View 4
@app.route('/{llm_generation}_04')
def {llm_generation}_04():
    return "231"


## View 5
@app.route('/{llm_generation}_05')
def {llm_generation}_05():
    return "1"
            
""" + "\n\n\n\n## generate starts here"

with open('index.py', 'r+') as file:
    content = file.read().replace(route_search_text, route_replace_text)
    file.seek(0)  
    file.write(content)