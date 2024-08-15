
import random

class deck:
    def __init__(self):
        self.cards=[]
        suits=["spade","heart","clubs","diamonds"]
        # ranks=["A","2","3","4","5","6","7","8","9","10","j","Q","K"]

        ranks=[
            {"rank":"A", "value":11},
            {"rank":"2", "value":2},
            {"rank":"3", "value":3},
            {"rank":"4", "value":4},
            {"rank":"5", "value":5},
            {"rank":"6", "value":6},
            {"rank":"7", "value":7},
            {"rank":"8", "value":8},
            {"rank":"9", "value":9},
            {"rank":"10", "value":10},
            {"rank":"J", "value":10},
            {"rank":"K", "value":10},
            {"rank":"Q", "value":10}
        ]

        for card in suits:
            for rnk in ranks:
                self.cards.append([card,rnk])

    def shuffles(self):
        if len(self.cards)>1:
            random.shuffle(self.cards)

    def deal(self,num):
        crrd=[]
        if len(self.cards)>0:
            for n in range( num):
                crrd.append(self.cards.pop())
            return crrd 
        else:
            return crrd,"No more card available to be drawn"   
            

    # shuffles()
    # card_delt=deal(2)
    # card=card_delt[0]
    # rank=card[1]

    # if rank=="A":
    #     value=11
    # elif rank=="J" or rank=="K" or rank=="Q":
    #     value=10
    # else:
    #     value=rank

    # rank_dict={"rank":rank, "value":value}

    # print(rank_dict["rank"], rank_dict["value"])

    
deck1=deck()
deck2=deck()

print(deck1.cards)

deck2.shuffles()
print(deck2.cards)  #file commit
