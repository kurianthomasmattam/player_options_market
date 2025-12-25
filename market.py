import math
import random

players_data = [
    {"name": "Lamine Yamal", "club": "Barcelona", "value": 200.0, "sigma": 0.225},
    {"name": "Erling Haaland", "club": "Manchester City", "value": 200.0, "sigma": 0.213},
    {"name": "Kylian Mbappé", "club": "Real Madrid", "value": 200.0, "sigma": 0.221},
    {"name": "Jude Bellingham", "club": "Real Madrid", "value": 160.0, "sigma": 0.155},
    {"name": "Vinícius Júnior", "club": "Real Madrid", "value": 150.0, "sigma": 0.155},
    {"name": "Pedri", "club": "Barcelona", "value": 140.0, "sigma": 0.128},
    {"name": "Jamal Musiala", "club": "Bayern Munich", "value": 130.0, "sigma": 0.203},
    {"name": "Michael Olise", "club": "Bayern Munich", "value": 130.0, "sigma": 0.160},
    {"name": "Bukayo Saka", "club": "Arsenal", "value": 130.0, "sigma": 0.215},
    {"name": "Cole Palmer", "club": "Chelsea", "value": 120.0, "sigma": 0.229},
    {"name": "Federico Valverde", "club": "Real Madrid", "value": 120.0, "sigma": 0.144},
    {"name": "Declan Rice", "club": "Arsenal", "value": 120.0, "sigma": 0.152},
    {"name": "Alexander Isak", "club": "Newcastle United", "value": 120.0, "sigma": 0.257},
    {"name": "Moisés Caicedo", "club": "Chelsea", "value": 110.0, "sigma": 0.158},
    {"name": "João Neves", "club": "Paris Saint-Germain", "value": 110.0, "sigma": 0.216},

    {"name": "Florian Wirtz", "club": "Liverpool", "value": 110.0, "sigma": 0.213},
    {"name": "Vitinha", "club": "Paris Saint-Germain", "value": 110.0, "sigma": 0.106},
    {"name": "Julián Álvarez", "club": "Atlético Madrid", "value": 100.0, "sigma": 0.161},
    {"name": "Ousmane Dembélé", "club": "Paris Saint-Germain", "value": 100.0, "sigma": 0.297},
    {"name": "Désiré Doué", "club": "Paris Saint-Germain", "value": 90.0, "sigma": 0.193},
    {"name": "Arda Güler", "club": "Real Madrid", "value": 90.0, "sigma": 0.123},
    {"name": "Khvicha Kvaratskhelia", "club": "Paris Saint-Germain", "value": 90.0, "sigma": 0.233},
    {"name": "William Saliba", "club": "Arsenal", "value": 90.0, "sigma": 0.118},
    {"name": "Ryan Gravenberch", "club": "Liverpool", "value": 90.0, "sigma": 0.167},
    {"name": "Hugo Ekitiké", "club": "Liverpool", "value": 85.0, "sigma": 0.182},
]

def make_player(name,club,value,sigma):
    'Creates a player object (dictionary) with the given information'
    return {"name": str(name),
        "club": str(club),
        "value": float(value),
        "sigma": float(sigma),}

def build_default_players():
    "Builds a list of default players"
    players = []
    for player in players_data:
        players.append(
            make_player(player["name"], player["club"], player["value"], player["sigma"])
        )
    return players

def find_player(players,name):
    'Finds the player with the given name from the list of players'
    for player in players:
        if player["name"] == name:
            return player
    return None

def list_players(players):
    'Function that displays everything cleanly'
    print ('Players:')
    for player in players:
        print (player["name"], "|", player["club"], "| value:", round(player["value"], 2), "| sigma:", round(player["sigma"], 3))


# Coming to the simulation part!#

def simulate_value_day(player):
    'Function that simulates the day for the specific player'
    sigma_yearly=player["sigma"]
    sigma_daily=sigma_yearly/math.sqrt(365)

    shock=random.gauss(0,sigma_daily)
    new_value=player["value"]*(1+shock)

    #To deal with the special case where value ends up being negative#
    if new_value<0:
        new_value=0

    player['value']=new_value

def simulate_value_days(days:int,players):
    for n in range(0,days):
        for player in players:
            simulate_value_day(player)

















