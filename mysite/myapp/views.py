from django.shortcuts import render
from understatapi import UnderstatClient

def match_rosters(request):
    understat = UnderstatClient()
    team_match_data = understat.team(team="Manchester_United").get_match_data(season="2019")
    match_id = team_match_data[0]["id"]
    roster_data = understat.match(match=match_id).get_roster_data()

    context = {
        'home_team': roster_data['home'],
        'away_team': roster_data['away'],
    }

    return render(request, 'roster.html', context)
