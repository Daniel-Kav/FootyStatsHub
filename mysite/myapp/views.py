from django.shortcuts import render
from understatapi import UnderstatClient

def match_rosters(request):
     # Use the UnderstatClient within a context manager to ensure proper resource management
    with UnderstatClient() as understat:
        # Fetch league player data for the English Premier League (EPL) season 2019
        league_player_data = understat.league(league="EPL").get_player_data(season="2019",limit= 2)
        
        # Fetch shot data for a specific player (player ID: 2371)
        player_shot_data = understat.player(player="2371").get_shot_data(limit= 2)
        
        # Fetch match data for the team Manchester United for the season 2019
        team_match_data = understat.team(team="Manchester_United").get_match_data(season="2019",limit= 2)
        
        # Fetch roster data for a specific match (match ID: 14711)
        roster_data = understat.match(match="14711").get_roster_data(limit= 2)

    
    # Pass the fetched data to the template
    context = {
        'league_player_data': league_player_data,
        'player_shot_data': player_shot_data,
        'team_match_data': team_match_data,
        'roster_data': roster_data,
    }

    return render(request, 'roster.html', context )
