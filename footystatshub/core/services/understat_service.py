# core/services/understat_service.py
import requests

BASE_URL = 'https://understat.com/'

def get_player_stats(player_id):
    """
    Fetch stats for a specific player from the Understat API.
    
    :param player_id: The ID of the player
    :return: JSON response containing player stats
    """
    url = f"{BASE_URL}player/{player_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # Return the response in JSON format
    else:
        return None

def get_team_stats(team_id):
    """
    Fetch stats for a specific team from the Understat API.
    
    :param team_id: The ID of the team
    :return: JSON response containing team stats
    """
    url = f"{BASE_URL}team/{team_id}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None
