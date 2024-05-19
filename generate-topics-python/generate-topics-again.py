import ollama
import os
import shutil

# Prompt user to input lesson title. This generates to the UI Widget Menu in the Main Menu of Subjects
lesson_title = input("Input a Lesson Title Here: ")

# Model type for widget generation
model_type = "gemma"

# Chat with Ollama using specified model type
widget_menu_response = ollama.chat(model=model_type, messages=[{'role': 'user','content': "Can you give me a summary sentence on the " + lesson_title + "? Explain like I'm a five year old learning how to." },])
topic_screen_response = ollama.chat(model=model_type, messages=[{'role': 'user','content': "Can you give me an introductional sentence on anything" },])


# Extract HTML content from widget menu response
widget_menu_response_output = widget_menu_response['message']['content']
topic_screen_response_output = topic_screen_response['message']['content']

# Update HTML file with lesson title and content
os.system("perl -pi -e 's{generate starts here}{<div class=\"widget-boxes-init\"><div class=\"widget-boxes-header-title\"><h1>" + lesson_title + "</h1><div class=\"widget-boxes-header-description\">" + str(widget_menu_response_output)  + "<h2> Blah blah blah </h2> <button class=''osui-button''>lesson title</button></div></div></div> \n\n generate starts here}g' templates/main_menu.html")



os.system("perl -pi -e 's{content generation starts here}{hello words}g' templates/01.html")

# Copy template directory and rename it with lesson title
template_dir = "templates/template-new-refreshed"
new_dir = "templates/" + lesson_title
shutil.copytree(template_dir, new_dir)
os.rename(new_dir, "templates/" + lesson_title)
