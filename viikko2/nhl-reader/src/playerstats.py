from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader):
        pelaajat = reader.get_players()
        self.players = pelaajat

    
    def top_scorers_by_nationality(self, nationality):
        lista = []
        for player in self.players:
            if player.nationality == nationality:
                lista.append(player)
        sorted_players = sorted(lista, key= lambda x: x.assists + x.goals, reverse=True)
        return sorted_players