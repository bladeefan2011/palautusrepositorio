import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2024-25/players"
    response = requests.get(url).json()

    print("JSON-muotoinen vastaus:")
    print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Oliot:")

    print("PLAYERS FROM FINLAND")
    lista = []
    for player in players:
        #lol = f"{player} {player.goals} + {player.assists} = {omg}"
        if player.nationality == "FIN":
            lista.append(player)
    sorted_players = sorted(lista, key= lambda x: x.assists + x.goals, reverse=True)

    for player in sorted_players:
        pojot = player.goals + player.assists
        print(f"{player.name:20} {player.team:15}  {player.goals:2} + {player.assists:2} = {pojot:3}")







if __name__ == "__main__":
    main()
