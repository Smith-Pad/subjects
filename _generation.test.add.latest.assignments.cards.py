import os


GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE = "./templates/_latest.assignments.cards.html"
GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_CARD_TITLE = "Hello world"







with open(GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE, 'a') as fd:
    fd.write(f'\n\n\n\n\n')


with open(GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_SOURCE, 'a') as fd:
    fd.write(f'''
      <div class="col s12 m3">
        <div class="card blue-grey darken-1">
          <div class="card-content white-text">
            <span class="card-title">{GENERATION_TEST_ADD_LATEST_ASSIGNMENTS_CARDS_CARD_TITLE}</span>
            <p></p>
          </div>
          <div class="card-action">
              <md-filled-button>Ready Fredy</md-filled-button>
          </div>
        </div>
      </div>
    
    ''')