import ollama
import os
import shutil

def get_summary():
    """
    Function to get summary sentence from Ollama chat.
    """
    lesson_title = input("Input a Lesson Title Here: ")
    
    # Model type for Ollama
    MODEL_TYPE = "gemma"
    
    response = ollama.chat(model=MODEL_TYPE, messages=[
        {
            'role': 'user',
            'content': f"Can you give me a summary sentence on the {lesson_title} Explain like I'm a five year old learning how to"
        },
    ])
    
    return lesson_title, response['message']['content']

def generate_widget(lesson_title, output_html):
    """
    Function to generate widget button for main_menu.html.
    """
    widget_code = f"<div class=\"widget-boxes-init\"><div class=\"widget-boxes-header-title\"><h1>{lesson_title}</h1><div class=\"widget-boxes-header-description\">{output_html}<h2> Blah blah blah </h2> <button class=''osui-button''>{lesson_title}</button></div></div></div> \n\n generate starts here"
    os.system(f"perl -pi -e 's{{generate starts here}}{{{widget_code}}}g' templates/main_menu.html")

def copy_template(lesson_title):
    """
    Function to copy template directory for the specified subject generation.
    """
    template_dir = "templates/template-new-refreshed"
    new_dir = f"templates/{lesson_title}"
    shutil.copytree(template_dir, new_dir)
    os.rename(new_dir, f"templates/{lesson_title}")

# Main program
if __name__ == "__main__":
    lesson_title, output_html = get_summary()
    generate_widget(lesson_title, output_html)
    copy_template(lesson_title)
