#! /usr/bin/python3

import sys
import random

import markovify

themes = [
    {'court': 'democratie', 'long': 'Démocratie et citoyenneté'},
    {'court': 'ecologie', 'long': 'Transition écologique'},
    {'court': 'fiscalite', 'long': 'Fiscalité et dépense publique'},
    {'court': 'services', 'long': 'Org. État et services publics'},
]

fins = ['na !','et voilà !','okayyy ?',"et pis c'est tout !","et paf !",'facile...',
        'simple !','pas mal !','et ouste !','circulez !','next ?', 'pour sûr !', 'ou pas...',
        'non mais !','nananère...','-<:)','🤣','🙃','😁','🤔','🙄','😎','😕']

# sélectionne un thème
theme = themes[random.randrange(len(themes))]

# constitution du modèle
text_model = markovify.Text(open(theme['court']+'-titres.txt').read(), state_size=3)

# composition du tweet
t = theme['long'] + ' ?\\n\\n'
t = t + text_model.make_short_sentence(200-len(t))
t = t + '\\n\\n' + fins[random.randrange(len(fins))]
print(t)
