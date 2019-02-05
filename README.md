# Grand Débile

Code du BOT alimentant de compte twitter @GrandDebile

Ce BOT est juste humoristique, à prendre bien sûr au second degré.

Dépendances:
- (markovify)[https://github.com/jsvine/markovify] : module python de génération de texte basé sur les chaînes de markov
- twitter : module python pour interragir avec l'API twitter

Les données textuelles utilisées proviennent du site granddebat.fr qui ont été publiées par Code For France sur https://frama.link/opendebat

Seuls les titres des propositions sont utilisés, et extraits à l'aide jq :

`jq .titre democratie.json -r > democratie-titres.txt`
