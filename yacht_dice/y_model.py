class Board:
    score:list  #0:bonus, 1:aces, ... 6:sixes, 7:choice, 8:4_kind, 9:f_house, 10:ss, 11:ls, 12:yacht

    def __init__(self):
        self.score = [-1]*13
        

class Player:
    board:Board
    history:list
    def __init__(self):
        self.board = Board()
        self.history = []

class Ymodel:
    players:list
    dices:list
    def __init__(self):
        self.players = []
        self.dices = []
        p_len:int = 2   #플레이어 수
        for i in range(p_len):
            self.players.append(Player())
        for i in range(5):
            self.dices.append(0)
        