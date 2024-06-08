import requests
from dataclasses import dataclass
import json
import os


repos = list()
TOKEN = os.environ['GITHUB_SONOMA_TOKEN']

@dataclass
class Rep:
    name: str
    description: str | None
    url: str
    preview: str | None
    stars: int
    lang: str

def repinfo(z):
    stars = len(requests.get(f'https://api.github.com/repos/sonoma-org/{z["name"]}/stargazers', headers={"Authorization":f"Bearer {TOKEN}"}).json())
    lang_request = requests.get(f'https://api.github.com/repos/sonoma-org/{z["name"]}/languages', headers={"Authorization":f"Bearer {TOKEN}"}).json()
    lang = next(map(lambda x: x[0], sorted(lang_request.items(), key=lambda x: x[1], reverse=True)), "Unknown")


    return Rep(name=z['name'], description=z['description'], url=z['html_url'], preview=None, stars=stars, lang=lang)


def get_reps():
    js = requests.get('https://api.github.com/orgs/sonoma-org/repos', headers={"Authorization":f"Bearer {TOKEN}"}).json()
    print(js)
    l = list(map(repinfo, js))

    global repos 
    repos = l


def get_json_names():
    return list(map(lambda x: x.name, repos))



def get_rep(name: str):
    for i in repos:
        if i.name == name:
            return i
    else:
        return None
        
        
