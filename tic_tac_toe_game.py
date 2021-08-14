#RSPLS game
def RSPLS_game(player):
    import random
    #print (first,second)
    list = ["Rock","Scissor","Paper","Lizard","Spock"]
    player1 = str(input("pick one of Rock, Scissor, Paper,Lizard,Spock:  "))
    player1 = player1.capitalize()
    check1 = player1
    if not (check1.isalpha() and check1 in list):
        print ("playe1 your misspelling the word please try again  ")
        player1=str(input("please make your chosen   "))
    Comp = random.choice(list)
    print (Comp)
    if ((player1 == ("Rock")) and  (Comp =="Scissor") or (player1 == ("Scissor")) and  (Comp =="Rock")):
           if(player1 == ("Rock")):
                 result = "X"
                 print ("You win the square ", result)
           else:
                result = "O"          
                print("Rock Crushed Scissor, I'm sorry you lost the square")
    elif ((player1 == ("Rock")) and  (Comp =="Lizard") or (player1 == ("Lizard")) and  (Comp =="Rock")):
            if(player1 == ("Rock")):
                 result = "X"
                 print ("You win the square ", result)
            else: 
                result = "O"      
                print("Rock Smash Lizard, I'm sorry you lost the square")
    elif ((player1 == ("Paper")) and  (Comp =="Rock") or (player1 == ("Rock")) and  (Comp =="Paper")):
            if(player1 == ("Paper")):
                 result = "X"
                 print ("You win the square ", result)
            else:
                result = "O"     
                print("Paper Cover Rock, I'm sorry you lost the square")
    elif ((player1 == ("Paper")) and  (Comp =="Spock") or (player1 == ("Spock")) and  (Comp =="Paper")):
            if(player1 == ("Paper")):
                 result = "X"
                 print ("You win the square ",result)
            else:
                result = "O"     
                print ("Paper disproves Spock, I'm sorry you lost the square")  
               
    elif ((player1 == ("Scissor")) and  (Comp =="Paper") or (player1 == ("Paper")) and  (Comp =="Scissor")):
             if(player1 == ("Scissor")):
                 result = "X"
                 print ("You win the square ", result)
             else:
                result = "O"      
                print("Scissor Cuts Paper, I'm sorry you lost the square")
    elif ((player1 == ("Lizard")) and  (Comp =="Scissor") or (player1 == ("Scissor")) and  (Comp =="Lizard")):
            if(player1 == ("Scissor")):
                 result = "X"
                 print ("You win the square " ,result)
            else:
                result = "O"     
                print("Scisorssor Descap Lizard, I'm sorry you lost the square")
    elif ((player1 == ("Spock")) and  (Comp =="Scissor") or (player1 == ("Scissor")) and  (Comp =="Spock")):
            if(player1 == ("Spock")):
                 result = "X"
                 print ("You win the square ", result)
            else:
                result = "O"      
                print("Spock Smashs Scissor, I'm sorry you lost the square")
    elif ((player1 == ("Spock")) and  (Comp =="Rock") or (player1 == ("Rock")) and  (Comp =="Spock")):
             if(player1 == ("Spock")):
                 result = "X"
                 print ("You win the square ",result)
             else:
                result = "O"      
                print("Spock decaption Rock, I'm sorry you lost the square")
    elif ((player1 == ("Lizard")) and  (Comp =="Spock") or (player1 == ("Spock")) and  (Comp =="Lizard")):
             if(player1 == ("Lizard")):
                 result = "X"
                 print ("You win the square ", result)
             else:
                result = "O"     
                 
                print("Lizard Poisons Spock, I'm sorry you lost the square")
    elif ((player1 == ("Lizard")) and  (Comp =="Paper") or (player1 == ("Paper")) and  (Comp =="Lizard")):
             if(player1 == ("Lizard")):
                 result = "X"
                 print ("You win the square ", result)
             else:
                result = "O"      
                print("Lizard Eats Paper, I'm sorry you lost the square")
    return result                            
#Tic-Tac-Toe game
# main routine                
import random
player = [ ]
row1 = str(" |  |  ")
line = str("----------")
row2 = str(" |  |  ")
row3 = str(" |  |  ")
score = ""

Row = ("1,2,3")
Column = ("1,2,3")

#print (score[0] + "|" + score[1] + "|" + score[2] +"\n" +"----------"+ score[3] + "|" + score[4] + "|" + score[5] +"\n" +"----------" + score[6] + "|" + score[7] + "|" + score[8] )
count = 1
for i in range(2):
    player.append(input("Please enter you name!   "))

print ((player) , "are the two plyers of Tic-Tac-Toe game")
Selector = random.choice(player)

if Selector == player[0]:
    first = player[0]
    second = player[1]
else:
    first = player[1]
    second = player[0]
    
print ("The system choose " + Selector + " to start the game.")    
print (first + " will be playing ( X ) today, and gets to pick the first spot on the bord good luck!")
print ( row1 + "\n"+ line + "\n" +row2 + "\n" +line + "\n" + row3)
   
while count <= 9:
        print (first + ", where would you like to place your X")
        Row = int(input("Row:   "))
        Column = int(input("Column:  "))
        print ("In order to win your square you must win a game of Rock, Scissors, Paper, Lizard, Spock !")
        if (RSPLS_game(player) == 'X'):
            score = "X"
        
            if (Row == 1 and Column == 1):
                row1= row1[:0] + score +row1[1:]
            elif (Row == 1 and Column == 2):
                row1= row1[:2] + score +row1[3:]
            elif (Row == 1 and Column == 3):
                row1= row1[:4] + score +row1[5:]
            elif (Row == 2 and Column == 1):
                row2= row2[:0] + score +row2[1:]
            elif (Row == 2 and Column == 2):
                row2= row2[:2] + score +row2[3:]
            elif (Row == 2 and Column == 3):
                row2= row2[:4] + score +row2[5:]
            elif (Row == 3 and Column == 1):
                row3= row3[:0] + score +row3[1:]
            elif (Row == 3 and Column == 2):
                row3= row3[:2] + score +row3[3:]
            elif (Row == 3 and Column == 3):
                row3= row3[:4] + score +row3[5:]
            print ( row1 + "\n"+ line + "\n" +row2 + "\n" +line + "\n" + row3)
            count =count + 1
        else:  
            score = "O"
        
            if (Row == 1 and Column == 1):
                 row1= row1[:0] + score +row1[1:]
            elif (Row == 1 and Column == 2):
                row1= row1[:2] + score +row1[3:]
            elif (Row == 1 and Column == 3):
                row1= row1[:4] + score +row1[5:]
            elif (Row == 2 and Column == 1):
                row2= row2[:0] + score +row2[1:]
            elif (Row == 2 and Column == 2):
                row2= row2[:2] + score +row2[3:]
            elif (Row == 2 and Column == 3):
                row2= row2[:4] + score +row2[5:]
            elif (Row == 3 and Column == 1):
                row3= row3[:0] + score +row3[1:]
            elif (Row == 3 and Column == 2):
                row3= row3[:2] + score +row3[3:]
            elif (Row == 3 and Column == 3):
                row3= row3[:4] + score +row3[5:]
            print ( row1 + "\n"+ line + "\n" +row2 + "\n" +line + "\n" + row3)
            count = count +1
#The second player will take it's turn       
        print (second,", where would you like to place your O")
        Row = int(input("Row:   "))
        Column = int(input("Column:  "))
        print ("In order to win your square you must win a game of Rock, Scissors, Paper, Lizard, Spock !")
#Enter the RSPLS module
# result == 'X' win the change it to 'O' second player mark        
        if (RSPLS_game(player) == "X"):
            score = "O"
            if (Row == 1 and Column == 1):
                row1= row1[:0] + score +row1[1:]
            if (Row == 1 and Column == 2):
                row1= row1[:2] + score +row1[3:]
            if (Row == 1 and Column == 3):
                row1= row1[:4] + score +row1[5:]
            if (Row == 2 and Column == 1):
                row2= row1[:0] + score +row1[1:]
            if (Row == 2 and Column == 2):
                row2= row1[:2] + score +row1[3:]
            if (Row == 2 and Column == 3):
                row2= row1[:4] + score +row1[5:]
            if (Row == 3 and Column == 1):
                row3= row1[:0] + score +row1[1:]
            if (Row == 3 and Column == 2):
                row3= row1[:2] + score +row1[3:]
            if (Row == 3 and Column == 3):
                row3= row1[:4] + score +row1[5:]
            print ( row1 + "\n"+ line + "\n" +row2 + "\n" +line + "\n" + row3)
            count = count + 1
          
            
#The condition when second player lose the RSPRL game
#The mark will go to the first player which is play with 'X' mark            
        else:
            score = "X"
     
            if (Row == 1 and Column == 1):
                row1= row1[:0] + score +row1[1:]
            if (Row == 1 and Column == 2):
                row1= row1[:2] + score +row1[3:]
            if (Row == 1 and Column == 3):
                row1= row1[:4] + score +row1[5:]
            if (Row == 2 and Column == 1):
                row2= row1[:0] + score +row1[1:]
            if (Row == 2 and Column == 2):
                row2= row1[:2] + score +row1[3:]
            if (Row == 2 and Column == 3):
                row2= row1[:4] + score +row1[5:]
            if (Row == 3 and Column == 1):
                row3= row1[:0] + score +row1[1:]
            if (Row == 3 and Column == 2):
                row3= row1[:2] + score +row1[3:]
            if (Row == 3 and Column == 3):
                row3= row1[:4] + score +row1[5:]
            print ( row1 + "\n"+ line + "\n" +row2 + "\n" +line + "\n" + row3)
            count = count + 1
         
     
        while True:

         if ((row1[0] == 'X' and row1[2] == 'X' and row1[4] == 'X') or (row1[0] == 'O' and row1[2] == 'O' and row1[4] == 'O')):
             print ("we have winner")
         elif((row2[0] == 'X' and row2[2] == 'X' and row2[4] == 'X') or (row2[0] == 'O' and row2[2] == 'O' and row2[4] == 'O')):
             print ("we have winner")
         elif((row3[0] == 'X' and row3[2] == 'X' and row3[4] == 'X') or (row3[0] == 'O' and row3[2] == 'O' and row3[4] == 'O')):
             print ("we have winner")
         elif((row1[0] == 'X' and row2[0] == 'X' and row3[0] == 'X') or (row1[0] == 'O' and row2[0] == 'O' and row3[0] == 'O')):
             print ("we have winner")
         elif((row1[2] == 'X' and row2[2] == 'X' and row3[2] == 'X') or (row1[2] == 'O' and row2[2] == 'O' and row3[2] == 'O')):
             print ("we have winner")
         elif((row1[4] == 'X' and row2[4] == 'X' and row3[4] == 'X') or (row1[4] == 'O' and row3[4] == 'O' and row3[4] == 'O')):
            print ("we have winner")
         if((row1[0] == 'X' and row2[2] == 'X' and row3[4] == 'X') or (row1[0] == 'O' and row2[2] == 'O' and row3[4] == 'O')):
            print ("we have winner")
         if((row1[4] == 'X' and row2[2] == 'X' and row3[0] == 'X') or (row1[4] == 'O' and row2[2] == 'O' and row3[0] == 'O')):
            print ("we have winner")
             
                 

    
    
        


   



    



    
    
       
       
    
      


    

