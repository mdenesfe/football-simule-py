import csv
from factors import get_form_factor, get_age_factor

def read_players_data(file_name):
    players = []
    with open(file_name, newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["attack"] = float(row["attack"])
            row["defense"] = float(row["defense"])
            row["midfield"] = float(row["midfield"])
            players.append(row)
    return players

def get_team_players(players, team_name):
    return [p for p in players if p['team'] == team_name]

def calculate_team_ratings(players, positions):
    team_attack = 0
    team_defense = 0
    team_midfield = 0

    for player in players:
        form_factor = get_form_factor()
        age_factor = get_age_factor(player["age"])
        player["attack"] *= form_factor * age_factor
        player["defense"] *= form_factor * age_factor
        player["midfield"] *= form_factor * age_factor
        team_attack += player[positions["forward"]]
        team_defense += player[positions["defender"]]
        team_midfield += player[positions["midfielder"]]
    
    return (team_attack, team_defense, team_midfield)
