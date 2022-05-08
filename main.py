import requests
from logger import parametrized_logger

TOKEN = ''
url = 'https://superheroapi.com/api/' + TOKEN
heroes = ['Hulk', 'Captain America', 'Thanos']
log_path = './log.txt'

class Hero:
    def __init__(self, name, intelligense):
        self.name = name
        self.intelligense = intelligense

    def __lt__(self, other):
        if not isinstance(other, Hero):
            print("Error")
        else:
            return self.intelligense < other.intelligense


@parametrized_logger(log_path)
def get_hero_id(hero):
    resp = requests.get(url + '/search/' + hero).json()['results']
    for res in resp:
        if hero == res['name']:
            return res['id']
        else:
            return None


@parametrized_logger(log_path)
def get_hero_intell(name):
    hero_id = get_hero_id(name)
    intelligence = requests.get(url + '/' + hero_id + '/powerstats').json()['intelligence']
    return intelligence


@parametrized_logger(log_path)
def get_most_intell(heroes):
    heroes_intell = []
    for hero in heroes:
        heroes_intell.append(Hero(hero, get_hero_intell(hero)))
    heroes_intell.sort()
    return heroes_intell[-1]


print(get_most_intell(heroes).name)