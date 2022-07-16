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
body = {
    'text': md_text
}
HEADERS = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'token {TOKEN}'
}
response = requests.post(URL, data=json.dumps(body), headers=HEADERS)

with open(path.replace('.md', '.html'), 'w+') as file:
    file.write(response.text)

if response.ok:
    print(response.text)
    print('\n---Operation successful')
else:
    print('Something went wrong')
input('Press any key to close')
