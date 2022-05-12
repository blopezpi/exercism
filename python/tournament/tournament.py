import re
from typing import List, Any, Dict


def tally(rows: List[str]) -> List[str]:
    teams = {}
    for row in rows:
        team1, team2, result = row.split(';')
        if team1 not in teams:
            teams[team1] = {"MP":0, "W": 0, "L": 0, "D": 0, "P": 0}
        if team2 not in teams:
            teams[team2] = {"MP":0, "W": 0, "L": 0, "D": 0, "P": 0}
        teams[team1]["MP"] += 1
        teams[team2]["MP"] += 1
        if result == "draw":
            teams[team1]["D"] += 1
            teams[team2]["D"] += 1
            teams[team1]["P"] += 1
            teams[team2]["P"] += 1
        elif result == "win":
            teams[team1]["W"] += 1
            teams[team1]["P"] += 3
            teams[team2]["L"] += 1
        else:
            teams[team1]["L"] += 1
            teams[team2]["P"] += 3
            teams[team2]["W"] += 1
    
    return print_table(ordered_teams(teams))


def ordered_teams(teams: dict) -> Dict[str, Dict[str, int]]:
    team_order = sorted(teams.keys(), key=lambda k: (-teams[k]["P"], k))
    print(team_order)
    ordered_team = {}
    for team in team_order:
        ordered_team[team] = teams[team]
    return ordered_team


def print_table(teams: dict) -> List[str]:
    table = []
    table.append("Team                           | MP |  W |  D |  L |  P")
    for team in teams:
        table.append(f"{team:30} | {teams[team]['MP']:2} | {teams[team]['W']:2} | {teams[team]['D']:2} | {teams[team]['L']:2} | {teams[team]['P']:2}")
    return table