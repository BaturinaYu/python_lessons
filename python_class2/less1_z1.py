import requests
import json

username = 'BaturinaYu'
url = f'https://api.github.com/users/{username}/repos'

get_from_git = requests.get(url)
repos_dict = get_from_git.json()
print(f'Репозитории пользователя {username} на github.com:')
for i, el in enumerate(repos_dict):
    print(i+1, el['name'])

with open('data.json', 'w') as outfile:
    json.dump(repos_dict, outfile, indent=4)
