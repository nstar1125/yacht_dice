from y_model import Ymodel
from y_view import Yview
import random

class Ycontroller:
    ym:Ymodel
    yv:Yview
    def __init__(self, y_model:Ymodel, y_view:Yview):
        self.ym, self.yv = y_model, y_view

        for round in range(12):
            self.yv.show_round(round+1)    
            for i in range(len(self.ym.players)):
                self.play_round(i)
    
    def play_round(self, p_num:int):
        self.yv.show_board()
        roll_count:int = 0
        while roll_count<3:
            if roll_count == 0:
                keep_list = [False]*5
                self.roll_dices(keep_list)
                roll_count+=1
                self.yv.show_dices()
                cmd:str = self.yv.ask_cmd()
            if cmd == 's':    #submit
                break
            else:   #roll again
                keep_list = self.yv.ask_dice_keep()
                self.roll_dices(keep_list)
                roll_count+=1
                self.yv.show_dices()
                if roll_count<3:
                    cmd = self.yv.ask_cmd()
        s_idx:int = self.yv.ask_submit_idx(p_num,[self.cal_dices(self.ym.dices,i) for i in range(1,13)])
        self.ym.players[p_num].history.append(s_idx)
        self.ym.players[p_num].board.score[s_idx] = self.cal_dices(self.ym.dices, s_idx)
        self.ym.players[p_num].board.score[0] = self.cal_bonus(p_num)


    def roll_dices(self, keep_list:list):
        for i in range(5):
            if not keep_list[i]:
                self.ym.dices[i] = random.randint(1,6)

    def cal_bonus(self, p_num:int)->int:
        sum:int = 0
        for i in range(1,7):
            sum += self.ym.players[p_num].board.score[i]
        if sum>=63:
            return 35
        else:
            return 0

    def cal_dices(self, dice_list:list, row_num:int)->int:
        if 1 <= row_num and row_num <= 6:
            return dice_list.count(row_num)*row_num
        elif row_num == 7:
            return sum(dice_list)
        elif row_num == 8:
            counts = [dice_list.count(dice_list[i]) for i in range(5)]
            if 4 in counts or 5 in counts:
                return sum(dice_list)
            else:
                return 0
        elif row_num == 9:
            counts = [dice_list.count(dice_list[i]) for i in range(5)]
            if 2 in counts and 3 in counts:
                return sum(dice_list)
            else:
                return 0
        elif row_num == 10:
            temp_set = set(dice_list)
            if temp_set.issuperset(set([1,2,3,4])) or temp_set.issuperset(set([2,3,4,5])) or temp_set.issuperset(set([3,4,5,6])):
                return 15
            else:
                return 0
        elif row_num == 11:
            temp_set = set(dice_list)
            if temp_set.issuperset(set([1,2,3,4,5])) or temp_set.issuperset(set([2,3,4,5,6])):
                return 30
            else:
                return 0
        elif row_num == 12:
            counts = [dice_list.count(dice_list[i]) for i in range(5)]
            if 5 in counts:
                return 50
            else:
                return 0
