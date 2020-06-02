class Match:
    """Classe définissant un match caractérisée par :
    - son nom
    - la liste des joueurs y prenant part"""


    def __init__(self, name, players):
        """Constructeur de notre classe"""
        self.name = name
        self.players = players
