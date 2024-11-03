class Player:
    def __init__(self, fname, position) :
        self.fname = fname
        self.position = position

    def __str__(self) :
        return f"{self.fname} {self.position}"

    def teamName(self, team):
        print("Welcome the squad of the", team)