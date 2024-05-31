## Generate Topics



import os 
import shutil
import json
from ollama import generate

# print('''
# # ██╗░░██╗
# # ██║░░██║
# # ███████║
# # ██╔══██║
# # ██║░░██║
# # ╚═╝░░╚═╝
# ''')

# os.system("sleep 1")
# os.system("clear")


# print(''')
# ██╗░░██╗███████╗
# ██║░░██║██╔════╝
# ███████║█████╗░░
# ██╔══██║██╔══╝░░
# ██║░░██║███████╗
# ╚═╝░░╚═╝╚══════╝
# ''')

# os.system("sleep 0.4")
# os.system("clear")

# print(''')
# ██╗░░██╗███████╗██╗░░░░░
# ██║░░██║██╔════╝██║░░░░░
# ███████║█████╗░░██║░░░░░
# ██╔══██║██╔══╝░░██║░░░░░
# ██║░░██║███████╗███████╗
# ╚═╝░░╚═╝╚══════╝╚══════╝
# ''')

# os.system("sleep 0.3")
# os.system("clear")



# print(''')
# ██╗░░██╗███████╗██╗░░░░░██╗░░░░░
# ██║░░██║██╔════╝██║░░░░░██║░░░░░
# ███████║█████╗░░██║░░░░░██║░░░░░
# ██╔══██║██╔══╝░░██║░░░░░██║░░░░░
# ██║░░██║███████╗███████╗███████╗
# ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝
# ''')

# os.system("sleep 0.2")
# os.system("clear")

# print(''')
# ██╗░░██╗███████╗██╗░░░░░██╗░░░░░░█████╗░
# ██║░░██║██╔════╝██║░░░░░██║░░░░░██╔══██╗
# ███████║█████╗░░██║░░░░░██║░░░░░██║░░██║
# ██╔══██║██╔══╝░░██║░░░░░██║░░░░░██║░░██║
# ██║░░██║███████╗███████╗███████╗╚█████╔╝
# ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░╚════╝░
# ''')

# os.system("sleep 5")
# os.system("clear")

# os.system("cp -R templates/template-new-refreshed templates/abouttorename")

# lesson_title = input('''
# # ███████╗███╗░░██╗████████╗███████╗██████╗░  ████████╗██╗████████╗██╗░░░░░███████╗
# # ██╔════╝████╗░██║╚══██╔══╝██╔════╝██╔══██╗  ╚══██╔══╝██║╚══██╔══╝██║░░░░░██╔════╝
# # █████╗░░██╔██╗██║░░░██║░░░█████╗░░██████╔╝  ░░░██║░░░██║░░░██║░░░██║░░░░░█████╗░░
# # ██╔══╝░░██║╚████║░░░██║░░░██╔══╝░░██╔══██╗  ░░░██║░░░██║░░░██║░░░██║░░░░░██╔══╝░░
# # ███████╗██║░╚███║░░░██║░░░███████╗██║░░██║  ░░░██║░░░██║░░░██║░░░███████╗███████╗
# # ╚══════╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░░░╚═╝░░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝

# # ██╗░░██╗███████╗██████╗░███████╗
# # ██║░░██║██╔════╝██╔══██╗██╔════╝
# # ███████║█████╗░░██████╔╝█████╗░░
# # ██╔══██║██╔══╝░░██╔══██╗██╔══╝░░
# # ██║░░██║███████╗██║░░██║███████╗
# # ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚══════╝
# ''')


# lesson_title = lesson_title.replace(" ", "_")


# os.system(f"mv templates/abouttorename templates/{lesson_title}")


# os.system(f"perl -pi -e 's/<!-- generate starts here -->/<button class=\"FOIL-button-regular color-is-blue\">" + lesson_title + "<\/button>\\n\\n\\n <!-- generate starts here -->/g' templates/main_menu.html")


# firstOne = generate('gemma', 'Can you summarize the alphabet song for kids under 5 sentences?')['response']
# print(firstOne + "\n\n\n")








def makeDir():
        os.system("mkdir templates/new-topic")




def createSysFile():
        os.system("touch templates/new-topic/index.html")
        os.system("touch templates/new-topic/introduction.html")
        os.system("touch templates/new-topic/01.html")
        os.system("touch templates/new-topic/02.html")
        os.system("touch templates/new-topic/03.html")
        os.system("touch templates/new-topic/04.html")




makeDir()
createSysFile()