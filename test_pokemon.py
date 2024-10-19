from pokemon import *
import pytest

#Khaled Esmail,cs302,Karla Fant

#black box testing suite


def test_Avatar_insert():
    _Avatar = Avatar("Ash", "Born in Palet town" ,4, "Charmander")
    assert _Avatar._name == "Ash"
    assert _Avatar._history == "Born in Palet town"
    assert _Avatar._GymBadges == 4
    assert _Avatar._starter == "Charmander"


def test_Pokemon_insert():
    _Pokemon = Pokemon("Charmander", "A fire mouse", 4, "route 42")
    assert _Pokemon._name == "Charmander"
    assert _Pokemon._history == "A fire mouse"
    assert _Pokemon._level == 4
    assert _Pokemon._location == "route 42"

def test_Champion_insert():
    _Champion = Champion("Drake","A dragon master" ,"Dragonite", "Johto")
    assert _Champion._name == "Drake"
    assert _Champion._history == "A dragon master"
    assert _Champion._ace == "Dragonite"
    assert _Champion._region == "Johto"


# def test_Avatar_display():
#     with pytest.raises(ValueError):
#         _Avatar = Avatar("", "Born in Palet town" ,4, "Charmander")


# def test_Pokemon_display():
#     with pytest.raises(ValueError):
#         _Pokemon = Pokemon("", "A fire mouse",4, "route 42")

# def test_Champion_display():
#     with pytest.raises(ValueError):
#         _Champion = Champion("", "A dragon master" ,"Dragonite", "Johto")