#!/usr/bin/env python3

import random

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)

noun = (random_line('nouns.txt'))
adjective = (random_line('adjectives.txt'))

fullname = adjective + ' ' + noun
fonts = {
    'Iceland': 'https://fonts.googleapis.com/css2?family=Iceland&display=swap',
    'Eater': 'https://fonts.googleapis.com/css2?family=Eater&display=swap',
    'Metal Mania': 'https://fonts.googleapis.com/css2?family=Metal+Mania&display=swap',
    'Jolly Lodger': 'https://fonts.googleapis.com/css2?family=Jolly+Lodger&display=swap',
    'Pirata One': 'https://fonts.googleapis.com/css2?family=Pirata+One&display=swap',
    'UnifrakturCook': 'https://fonts.googleapis.com/css2?family=UnifrakturCook:wght@700&display=swap',
    'New Rocker': 'https://fonts.googleapis.com/css2?family=New+Rocker&display=swap',
    'Creepster': 'https://fonts.googleapis.com/css2?family=Creepster&display=swap',
    'Trade Winds': 'https://fonts.googleapis.com/css2?family=Trade+Winds&display=swap',
    'Nosifer': 'https://fonts.googleapis.com/css2?family=Nosifer&display=swap',
    'Special Elite': 'https://fonts.googleapis.com/css2?family=Special+Elite&display=swap',
    'Bangers': 'https://fonts.googleapis.com/css2?family=Bangers&display=swap',
    'UnifrakturMaguntia': 'https://fonts.googleapis.com/css2?family=UnifrakturMaguntia&display=swap'
    }
fontchoice = random.choice(list(fonts))
fonturl = fonts[fontchoice]

colors = [
    '#a44',
    '#4a4',
    '#fff',
    '#d60',
    '#6d0',
    ]
colorchoice = random.choice(colors)

print('Content-type:text/html\r\n\r\n')
print('<!DOCTYPE html>')
print('<html>')
print('<head>')
print('<title>Metal name generator</title>')
print('<link rel="stylesheet" href="style.css">')
print('<link href="' + fonturl + '" rel="stylesheet">')
print('<style>\n')
print('.x{font-family:' + fontchoice + ';color:' + colorchoice + ';}')
print('.z{color:black;background-color:white;border:1px solid white;}')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('</style>')
print('</head>')
print('<body>')
print('<h1></h1>')
print('<p>Your name is:</p>')
print('<h3 class="x">' + fullname + '</h3>')
print('<a class ="z" href="http://localhost/namegenerator/fontslist.py">Give me another!</a>')
print('</body>')
print('</html>')
