import requests

url = "https://understat.com/league/Ligue_1"



response = requests.get(url)

print(response.json())