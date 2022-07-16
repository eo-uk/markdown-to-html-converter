import os
import sys
import json
import requests
from dotenv import load_dotenv


load_dotenv()

try:
    path = sys.argv[1]
except IndexError:
    path = input('Path to .md file:\n')

with open(path, 'r') as file:
    md_text = file.read()

TOKEN = os.getenv('TOKEN')
URL = 'https://api.github.com/markdown'
HEADERS = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'token {TOKEN}'
}
body = {
    'text': md_text
}
response = requests.post(URL, data=json.dumps(body), headers=HEADERS)

if response.ok:
    print(response.text)

    path_dest = path.replace('.md', '.html')
    if os.path.exists(path_dest):
        while True:
            answer = input(
                'An HTML file with that name already exists, '
                'do you wish to overwrite this file? (y/n)'
            ).strip().lower()
            if answer in ('n', 'no'):
                print('\n---File was not written.')
                input('Press any key to close')
                sys.exit()
            elif answer in ('y', 'yes'):
                break
            
    with open(path_dest, 'w+') as file:
        file.write(response.text)
        
    print('\n---Operation successful')
else:
    print('Something went wrong')
    
input('Press any key to close')
