import numpy as np
from random import shuffle


class coloda():

    def __init__(self):

        self.coloda = []

        for i in range(4):
            
            mass = [i for i in range(9)]
            shuffle(mass)
            self.coloda.extend(mass)
        
    


class player():
    
    def __init__(self, cards):
        
        self.cards = cards.copy()
        

        for i in range(len(self.cards), 36):
            self.cards.append(-1)
        print(self.cards)
        
        
       
    def take_cards(self, new_cards, n):
    
        win_card = []

        for j in range(n):
            
            win_card.append(self.cards[0])
            i = 0
           
            while self.cards[i] != -1:
        
                self.cards[i] = self.cards[i + 1]
                i += 1
        
        
        for k in range(i,i + len(win_card)):
            
            self.cards[k - 1] = win_card[k - i]
        
        
        for j in range(len(new_cards)):
        
            self.cards[i + n - 1] = new_cards[j]
            i += 1
        


    def dont_take_cards(self, n):

        for j in range(n):
            i = 0

            while self.cards[i] != -1:
            
                self.cards[i] = self.cards[i + 1]
                i += 1



class game():
    
    
    def __init__(self, players):
        
        col = coloda()
        self.cards = col.coloda.copy()
        self.count_players = players if players > 1 and players < 5 else print("error")
        shuffle(self.cards)
        self.players = []
       
        for i in range(self.count_players):
            
            giving_cards = [self.cards[j] for j in range(36//self.count_players * i, 36//self.count_players * (i + 1))]
            self.players.append(player(giving_cards))

    def maax(self, spisok):

        for i in range(len(spisok)):
            if spisok[i] == 0 and 8 in spisok:
                return 0
        
        return max(spisok)
        

    def move(self, indexes, new_cards, counter_of_iterration):
        
        for i in indexes:
                        
            new_cards.append(self.players[i].cards[counter_of_iterration - 1])

        m = self.maax(new_cards)

        stetchik = []

        counter_of_iterration += 1
        print(counter_of_iterration)

        for i in range(self.count_players):

            if new_cards[i] == m:

                stetchik.append(i)
        
        if len(stetchik) == 1:

            self.players[stetchik[0]].take_cards(new_cards, counter_of_iterration)
            
            for i in range(self.count_players):
                
                if stetchik[0] == i:
                    continue
                
                else:    
                    self.players[i].dont_take_cards(counter_of_iterration)            
            
            return 1

        else:
            counter_of_iterration += 1
            self.move(stetchik, new_cards)

   
    def real_game(self):
        
        while 1 > 0:
            
            if (self.count_players == 1):
                return "Game over"

            for i in range(len(self.players)):

                if self.players[i].cards[0] == -1:
                    self.count_players -= 1
                    self.players.remove(self.players[i])
            
            self.move([i for i in range(self.count_players)], [])
                    
            






if __name__ == "__main__":

    game = game(2)
    game.real_game()

    
    