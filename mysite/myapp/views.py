from django.shortcuts import render
from understatapi import UnderstatClient
import asyncio
import aiohttp
import json

async def get_team_fixtures(league_name, season, team_id):
    async with aiohttp.ClientSession() as session:
        understat = UnderstatClient(session)
        fixtures = await understat.get_league_fixtures(
            league_name,
            season,
            options={"h": {"id": team_id}}
        )
        return fixtures

async def fetch_data():
    league_name = "epl"
    season = 2018
    team_id = "89"  # Manchester United's ID
    fixtures = await get_team_fixtures(league_name, season, team_id)
    return fixtures

def match_rosters(request):
    # Run the async function synchronously using asyncio.run
    fixtures = asyncio.run(fetch_data())

    # Pass the fetched data to the roster template
    context = {
        'fixtures': fixtures[:1],
    }


def match_rosters(request):
    # Use the UnderstatClient within a context manager to ensure proper resource management
    with UnderstatClient() as understat:
        # Fetch league player data for the English Premier League (EPL) season 2019
        league_player_data = understat.league(league="EPL").get_player_data(season="2019")
        
        # Fetch shot data for a specific player (player ID: 2371)
        player_shot_data = understat.player(player="2371").get_shot_data()
        
        # Fetch match data for the team Manchester United for the season 2019
        team_match_data = understat.team(team="Manchester_United").get_match_data(season="2019")
        
        # Fetch roster data for a specific match (match ID: 14711)
        roster_data = understat.match(match="14711").get_roster_data()

    # Parse JSON data into Python dictionaries or lists
    league_player_data = json.loads(league_player_data)
    player_shot_data = json.loads(player_shot_data)
    team_match_data = json.loads(team_match_data)
    roster_data = json.loads(roster_data)

    # Pass the fetched data to the roster template
    context = {
        'league_player_data': league_player_data,
        'player_shot_data': player_shot_data,
        'team_match_data': team_match_data,
        'roster_data': roster_data,
    }

    return render(request, 'roster.html', context , context)
