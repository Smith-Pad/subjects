import ollama
import shutil
import subprocess

# Input lesson title
lesson_title = input("Input a Lesson Title Here: ")

# Prompt for a summary sentence
summary_prompt = f"Can you give me a summary sentence on the {lesson_title}? Explain like I'm a five year old learning how to"
widget_menu_response = ollama.chat(model="gemma", messages=[{"role": "user", "content": summary_prompt}])
output_html = widget_menu_response['message']['content']

# Update HTML template
html_template = f'''
<div class="widget-boxes-init">
    <div class="widget-boxes-header-title">
        <h1>{lesson_title}</h1>
        <div class="widget-boxes-header-description">
            {output_html}
            <h2> Blah blah blah </h2>
            <button class="osui-button">{lesson_title}</button>
        </div>
    </div>
</div>
'''
template_file = "templates/main_menu.html"
with open(template_file, "r+") as f:
    content = f.read()
    f.seek(0, 0)
    f.write(html_template + "\n\n" + content)

# Copy template directory
template_dir = "templates/template-new-refreshed"
new_dir = f"templates/{lesson_title}"
try:
    shutil.copytree(template_dir, new_dir)
    os.rename(new_dir, f"templates/{lesson_title}")
except Exception as e:
    print("Error:", e)
