## test out
import os 
import shutil
import json
from ollama import generate


class RouteConfig:
    def __init__(self):
        self.lesson_title = True
        self.route_search_text = True
        self.route_replace_text = True
        self.route_replacer = True

    def enable_status(self):
        print("it is enabled") if self.lesson_title else print("It is not enabled")
        print("it is enabled") if self.route_search_text else print("It is not enabled")
        print("it is enabled") if self.route_replace_text else print("It is not enabled")
        print("it is enabled") if self.route_replacer else print("It is not enabled")

    def configure_routes(self):
        self.lesson_title = input("Input title: ")
        self.lesson_title = self.lesson_title.replace(" ", "_")

        self.route_search_text = "## generate starts here"

        self.route_replace_text = (
                f"""

## Splash Screen Generated

@app.route('/{self.lesson_title}')
def {self.lesson_title}():
        return "1"



@app.route('/{self.lesson_title}_begin')
def {self.lesson_title}_begin():
        return "begin"




@app.route('/{self.lesson_title}_01')
def {self.lesson_title}_01():
        return "01"

@app.route('/{self.lesson_title}_02')
def {self.lesson_title}_02():
        return "021"


@app.route('/{self.lesson_title}_03')
def {self.lesson_title}_03():
        return "2341"



@app.route('/{self.lesson_title}_04')
def {self.lesson_title}_04():
        return "231"



@app.route('/{self.lesson_title}_05')
def {self.lesson_title}_05():
        return "1"
                
                """                
                f"\n\n\n\n## generate starts here"
        )




        with open('index.py', 'r+') as file:
            content = file.read().replace(self.route_search_text, self.route_replace_text)
            file.seek(0)  
            file.write(content)



route_config = RouteConfig()
route_config.enable_status()
route_config.configure_routes()
