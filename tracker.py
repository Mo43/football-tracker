import requests
import time

API_KEY = "6ba343f6e21eb21e6466e6c9c6f46bce"

url = "https://v3.football.api-sports.io/fixtures?live=all"

headers = {
    "x-apisports-key": API_KEY
}

while True:
    response = requests.get(url, headers = headers)
    data = response.json()

    print("\nLIVE MATCHES\n")
    matches = data["response"]
    
    if not matches:
        print("No live matches")

    for match in matches:
        home = match["teams"]["home"]["name"]
        away = match["teams"]["away"]["name"]

        home_goals = match["goals"]["home"]
        away_goals = match["goals"]["away"]

        minute = match["fixture"]["status"]["elapsed"]

        print(f"{home} {home_goals} - {away_goals} {away}")
        print(f"{minute}'")
        print("-" * 30)

    time.sleep(30)
          

