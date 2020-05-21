import nltk
import random
import urllib

words = nltk.corpus.gutenberg.words('shakespeare-macbeth.txt')

print(f'Got {len(words)} words in total. Writing them to the readme...')

colors = [
    'brightgreen',
    'green',
    'yellowgreen',
    'yellow',
    'orange',
    'red',
    'blue',
    'blueviolet',
    'ff69b4'
]

with open('README.md', 'w') as f:
    for i, word in enumerate(words):
        if not word:
            continue
        color = random.choice(colors)
        url_params = urllib.parse.urlencode({
            'label': i,
            'message': word,
            'color': color
        })
        f.write(f'![](https://img.shields.io/static/v1?{url_params}) ')
