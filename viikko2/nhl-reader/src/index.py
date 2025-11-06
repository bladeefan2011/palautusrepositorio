"""
Pääohjelma NHL-tilastojen interaktiiviseen hakuun.
"""

from rich.console import Console
from rich.table import Table

from playerreader import PlayerReader
from playerstats import PlayerStats

def setup_services(season):
    """
    Alustaa ja palauttaa PlayerStats-olion
    (Erotettu main-funktiosta R0915-säännön takia).
    """
    url = f"https://studies.cs.helsinki.fi/nhlstats/{season}/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    return stats

def create_table(nationality, season):
    """
    Luo ja palauttaa alustetun rich-taulukon
    (Erotettu R0915-säännön takia).
    """
    table = Table(title=f"Season {season} players from {nationality}")
    table.add_column("Released", justify="left", style="cyan", no_wrap=True)
    table.add_column("teams", justify="center", style="magenta")
    table.add_column("goals", justify="right", style="green")
    table.add_column("assists", justify="right", style="green")
    table.add_column("points", justify="right", style="green")
    return table

def print_player_table(console, players, nationality, season):
    """
    Tulostaa pelaajadatan siistinä rich-taulukkona.
    Tämä on nyt alle 10 lausetta.
    """
    if not players:
        console.print(f"No players found from {nationality}.")
        return

    table = create_table(nationality, season)

    for player in players:
        table.add_row(
            player.name,
            player.team,
            str(player.goals),
            str(player.assists),
            # KORJAUS: Käytetään player.points-ominaisuutta
            str(player.points)
        )

    console.print(table)


def main():
    """
    Pääohjelma, joka koordinoi syötteen, haun ja tulostuksen.
    Tämä on nyt alle 10 lausetta.
    """
    season = input("Season [2018-19/.../2024-25] (2024-25): ")
    if not season:
        season = "2024-25"

    stats = setup_services(season)

    nationality = input("Nationality [USA/FIN/SWE/...] (): ")
    players = stats.top_scorers_by_nationality(nationality)

    console = Console()
    
    # Kutsutaan apufunktiota tulostamaan taulukko
    print_player_table(console, players, nationality, season)


if __name__ == "__main__":
    main()

