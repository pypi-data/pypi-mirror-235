from dataclasses import dataclass
from functools import cached_property
from ..data.hero import all_heroes_json


@dataclass
class Hero(object):
    id: int
    sysname: str
    fullname: str
    name: str

    def __hash__(self) -> int:
        return self.id


_all_heroes_map = {}
_all_heroes_list = []
for hero_json in all_heroes_json:
    hero = Hero(**hero_json)
    _all_heroes_list.append(hero)
    for attr in vars(hero).values():
        _all_heroes_map[attr] = hero
del hero_json
del attr


class HeroSet(object):
    def __init__(self, heroes: list[Hero]) -> None:
        self._heroes = heroes

    def get_heroes_fields(self, field_name: str):
        return [getattr(hero, field_name) for hero in self._heroes]

    def find(self, value):
        return _all_heroes_map.get(value, None)

    @property
    def heroes(self):
        return self._heroes
    
    @cached_property
    def ids(self):
        return self.get_heroes_fields("id")
    
    @cached_property
    def sysnames(self):
        return self.get_heroes_fields("sysname")
    
    @cached_property
    def fullnames(self):
        return self.get_heroes_fields("fullname")
    
    @cached_property
    def names(self):
        return self.get_heroes_fields("name")
    
    def __iter__(self):
        return iter(self._heroes)

    def __add__(self, heroset: "HeroSet"):
        heroes = self._heroes + heroset.heroes
        return HeroSet(heroes)


all_heroes = HeroSet(_all_heroes_list)
find_hero = all_heroes.find