"""
Tämä moduuli määrittelee Player-luokan.
"""

class Player:
    """
    Luokka edustaa yhtä NHL-pelaajaa ja heidän tilastojaan.
    """
    def __init__(self, player_dict): 
        """
        Alustaa pelaaja-olion sanakirjan (dict) perusteella.
        """
        self.name = player_dict['name']
        self.nationality = player_dict['nationality']
        self.assists = player_dict['assists']
        self.goals = player_dict['goals']
        self.team = player_dict['team']
        self.games = player_dict['games']

    @property
    def points(self):
        """
        Palauttaa pelaajan kokonaispisteet (maalit + syötöt).
        """
        return self.goals + self.assists

    def __str__(self):
        """
        Palauttaa pelaajan tiedot siistinä merkkijonona.
        """
        return f"{self.name:20} {self.team:15} {self.goals:2} + {self.assists:2} = {self.points}"
    
