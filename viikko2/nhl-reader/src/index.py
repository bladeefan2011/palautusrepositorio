import requests
from player import Player
from playerreader import PlayerReader
from playerstats import PlayerStats
from rich.console import Console
from rich.table import Table


def main():
    season = input("Season [2018-19/.../2024-25] (2024-25): ")
    if not season:
        season = "2024-25"

    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)

    nationality = input("Nationality [USA/FIN/SWE/...] (): ")
    players = stats.top_scorers_by_nationality(nationality)

    if not players:
        print(f"No players found from {nationality}.")
        return

    table = Table(title=f"Season 2024-25 players from {nationality}")
    
    table.add_column("Released", justify="left", style="cyan", no_wrap=True)
    table.add_column("teams", justify="center", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")

    for player in players:
        table.add_row(
            player.name, 
            player.team, 
            str(player.goals), 
            str(player.assists), 
            str(player.goals + player.assists)
        )

    console = Console()
    console.print(table)



if __name__ == "__main__":
    main()
