import random



class Card:
    def __init__(self, suit, rank):
       self.suit=suit
       self.rank=rank 

    def __str__(self):
       
       return f"{self.rank['rank']} of {self.suit}"
       

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

       
        for suit in suits:  # Changed variable name from 'card' to 'suit'
            for rnk in ranks:
                self.cards.append(Card(suit, rnk))  # Correctly create a Card instance
                
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
            
class Hand:
    def __init__(self, dealer=False):
        self.cards=[]
        self.value=0
        self.dealer=dealer
    
    def add_card(self, card_list):
        self.cards.extend(card_list) 

    def calculate_value(self):
        self.value=0
        has_ace=False 
        for Card in self.cards:
            card_value=int(Card.rank["value"])
            self.value+=card_value
            if(Card.rank["rank"]=="A"):
                has_ace=True

        if has_ace and self.value>21:
            self.value-=10

    def get_value(self):
        self.calculate_value  #instance specific data calling
        return self.value

    def is_blackjack():
        return self.get_value() ==21
    
    def  display():
        print("Your hand")
        

deck=deck()
deck.shuffles()
hand=Hand()
hand.add_card(deck.deal(2))
print(hand.cards[0])
print(hand.cards[1]) # changes from home pc