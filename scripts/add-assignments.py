'''
CLI VERSION

'''


import os

## Variables for adding the Assignment Cards that are considered as latest assignments on the home
GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE = "../templates/_latest.assignments.cards.html"




TITLE_OF_LESSON = input("Create the title of the lesson:        ")
DESCRIPTION_OF_LESSON = input("Create the description of the lesson:        ")

'''
Right now, this is commented for now until this is activated again...
'''

# with open(GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE, 'a') as fd:
#     fd.write(f'\n\n\n\n\n')


# with open(GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE, 'a') as fd:
#     fd.write(f'''
#       <div class="col s12 m3">
#         <div class="card blue-grey darken-1">
#           <div class="card-content white-text">
#             <span class="card-title">{TITLE_OF_LESSON}</span>
#             <p>{DESCRIPTION_OF_LESSON}</p>
#           </div>
#           <div class="card-action">
#               <md-filled-button>Ready Fredy</md-filled-button>
#           </div>
#         </div>
#       </div>
    
#     ''')




'''
In this section, this is where we are able to create the lessons using Ollama.

Make sure you have Ollama already. 
'''

## The first thing to do is to create a generation for the lesson
os.system(f'cd ../templates/ && mkdir "{TITLE_OF_LESSON}"')



## The second thing is to create the routing schemes on the lesson
os.system(f'cd ../templates/ && mkdir "{TITLE_OF_LESSON}"')


## Then create some files in that generation
os.system(f'cd ../templates/ && cd "{TITLE_OF_LESSON}" && touch index.html')
os.system(f'cd ../templates/ && cd "{TITLE_OF_LESSON}" && touch main_menu.html')
os.system(f'cd ../templates/ && cd "{TITLE_OF_LESSON}" && touch 01.html')
os.system(f'cd ../templates/ && cd "{TITLE_OF_LESSON}" && touch 02.html')
os.system(f'cd ../templates/ && cd "{TITLE_OF_LESSON}" && touch 03.html')
os.system(f'cd ../templates/ && cd "{TITLE_OF_LESSON}" && touch 04.html')
os.system(f'cd ../templates/ && cd "{TITLE_OF_LESSON}" && touch 05.html')
os.system(f'cd ../templates/ && cd "{TITLE_OF_LESSON}" && touch 06.html')
os.system(f'cd ../templates/ && cd "{TITLE_OF_LESSON}" && touch 07.html')
os.system(f'cd ../templates/ && cd "{TITLE_OF_LESSON}" && touch 08.html')
os.system(f'cd ../templates/ && cd "{TITLE_OF_LESSON}" && touch 09.html')
os.system(f'cd ../templates/ && cd "{TITLE_OF_LESSON}" && touch 10.html')
os.system(f'cd ../templates/ && cd "{TITLE_OF_LESSON}" && touch pop11.html')