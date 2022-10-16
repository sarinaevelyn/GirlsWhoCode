import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
t1=0 
t2=0

def hit(total):
    c=random.choice(cards)
    total=total+c
    print("your score is: " + str(total))
    return total 

def stay(total):  
    print("your final score is: " + str(total))
    return total



def playBlackjack():
    play = input('Player will you hit or stay:\n')
    
    total = 0
    
    while total<21:
            while play == "hit": 
                total=hit(total)
                if total>21: 
                    print("you lose")
                    total=100
                    quit() 
                elif total==21: 
                    print("You got Blackjack")
                    return total 
                    quit()
                else: 
                    play = input('Will you hit or stay:\n')
            while play == "stay": 
                total=stay(total)
                if total>21: 
                    print("you lose")
                    total=100
                    quit() 
                elif total==21: 
                    print("You got Blackjack")
                    return total 
                    quit()
                else: 
                    return total 

t1 = playBlackjack()
t2 = playBlackjack()

if t1>t2: 
    print("Player 1 won")
else: 
    print("Player 2 won")

n = int(input('Enter a number:\n'))
while n>2:
    while (n%2) == 0: 
        if n==2: 
            break 
        else: 
            print(n-2)
            n=n-2
        
    else: 
        print("your number needs to be even")
        n=int(input('Enter a new number:\n'))