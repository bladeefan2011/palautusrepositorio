"""
Tämä moduuli määrittelee PlayerStats-luokan,
joka laskee tilastoja pelaajalistasta.
"""

# KORJAUS (W0611): Tuontia käytetään nyt tyyppivihjeessä
from playerreader import PlayerReader

# KORJAUS (R0903): Poistetaan 'too-few-public-methods' -valitus.
# pylint: disable=R0903
class PlayerStats:
    """
    Hallinnoi ja laskee tilastoja PlayerReader-olion
    tarjoamista pelaajista.
    """
    def __init__(self, reader: PlayerReader): 
        """
        Alustaa tilastoluokan.

        Args:
            reader (PlayerReader): Olio, joka osaa hakea pelaajadatan.
        """
        pelaajat = reader.get_players()
        self.players = pelaajat

    def top_scorers_by_nationality(self, nationality):
        """
        Palauttaa listan pelaajista annetusta kansalaisuudesta
        pisteiden mukaan laskevassa järjestyksessä.
        """
        lista = []
        for player in self.players:
            if player.nationality == nationality:
                lista.append(player)
        
        
        sorted_players = sorted(lista, key=lambda x: x.points, reverse=True)
        return sorted_players

