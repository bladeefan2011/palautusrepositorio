"""
Tämä moduuli määrittelee PlayerReader-luokan,
joka hakee pelaajatiedot URL-osoitteesta.
"""

import requests
from player import Player

# KORJAUS (R0903): Poistetaan 'too-few-public-methods' -valitus,
# koska tälle luokalle riittää yksi julkinen metodi.
# pylint: disable=R0903
class PlayerReader:
    """Lukee pelaajatiedot annetusta URL-osoitteesta."""
    def __init__(self, url):
        """Alustaa lukijan URL-osoitteella."""
        self.url = url

    def get_players(self):
        """
        Hakee ja palauttaa pelaajat Player-olioina.

        Returns:
            list: Lista Player-olioita.
        """
        response = requests.get(self.url, timeout=10).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players

