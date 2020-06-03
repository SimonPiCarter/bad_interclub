class Constraint:
    """Classe définissant une contrainte abstraite caractérisée par :
    - son nom"""


    def __init__(self, name):
        """Constructeur de notre classe"""
        self.name = name


class RankConstraint(Constraint):
    """Classe définissant une contrainte sur le match caractérisée par :
    - son nom
    - le nom du match
    - le rang du match"""


    def __init__(self, name, matchName, matchRank):
        """Constructeur de notre classe"""
        Constraint.__init__(self, name)
        self.matchName = matchName
        self.matchRank = matchRank

class OrderConstraint(Constraint):
    """Classe définissant une contrainte imposant le premier match avant le second match par :
    - son nom
    - le nom du premier match
    - le nom du second match"""


    def __init__(self, name, firstMatch, secondMatch):
        """Constructeur de notre classe"""
        Constraint.__init__(self, name)
        self.firstMatch = firstMatch
        self.secondMatch = secondMatch
