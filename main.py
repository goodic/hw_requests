import requests

TOKEN = '2619421814940190'
url = 'https://superheroapi.com/api/' + TOKEN
heroes = ['Hulk', 'Captain America', 'Thanos']


class Hero:
    def __init__(self, name, intelligense):
        self.name = name
        self.intelligense = intelligense

    def __lt__(self, other):
        if not isinstance(other, Hero):
            print("Error")
        else:
            return self.intelligense < other.intelligense


def get_hero_id(hero):
    resp = requests.get(url + '/search/' + hero).json()['results']
    for res in resp:
        if hero == res['name']:
            return res['id']
        else:
            return None


def get_hero_intell(name):
    hero_id = get_hero_id(name)
    intelligence = requests.get(url + '/' + hero_id + '/powerstats').json()['intelligence']
    return intelligence


def get_most_intell(heroes):
    heroes_intell = []
    for hero in heroes:
        heroes_intell.append(Hero(hero, get_hero_intell(hero)))
    heroes_intell.sort()
    return heroes_intell[-1]


print(get_most_intell(heroes).name)