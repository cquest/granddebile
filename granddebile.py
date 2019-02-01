import sys
import random

import markovify
from twitter import *

themes = [
    {'court': 'democratie', 'long': 'Démocratie et citoyenneté'},
    {'court': 'ecologie', 'long': 'Transition écologique'},
    {'court': 'fiscalite', 'long': 'Fiscalité et dépense publique'},
    {'court': 'services', 'long': 'Org. État et services publics'},
]

fins = ['na !','et voilà !','okayyy ?',"et pis c'est tout !","et paf !",'facile...',
        'simple !','pas mal !','et ouste !','circulez !','next ?', 'pour sûr !',
        'non mais !','nananère...','-<:)','🤣','🙃','😁','🤔','🙄','😎','😕']

# sélectionne un thème
theme = themes[random.randrange(len(themes))]

# constitution du modèle
text_model = markovify.Text(open(theme['court']+'-titres.txt').read())

# Print three randomly-generated sentences of no more than 140 characters
t = ''
if random.randrange(10) > 8:
    t = '#GrandDebatNational '
t = t + theme['long'] + ' ?\\n\\n'
t = t + text_model.make_short_sentence(130-len(t))
fin = fins[random.randrange(len(fins))]
if len(t+fin) < 136:
    t = t + '\\n\\n'+fin
print(t)
