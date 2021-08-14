#RSPLS game
import random
list = ["Rock","Scisorssor","Paper","Lizard","Spock"]
score_player = 0
score_Comp = 0
count = 1
name= str(input("Please Enter your name:  "))
player1 = name
Time_Play = int(input("please select the times you would like to play interger positive number!   "))
while count <= Time_Play:       
    player = str(input(player1 + " Please pick one of Rock, Scisorssor, Paper,Spock:  "))       
    player = player.capitalize()
    check1 = player
    if not (check1.isalpha() and check1 in list):
        print ("player your misspelling the word please try again  ")
        player1=str(input("please make your chosen   "))
    Comp = random.choice(list)
    print ("Computer selecte ", Comp)
    if ((player == ("Rock")) and  (Comp =="Scisorssor") or (player == ("Scisorssor")) and  (Comp =="Rock")):
            if(player == ("Rock")):
                 score_player = score_player + 1
                 print (player + "You win the square ", score_player)
            else:
                 score_Comp = score_Comp + 1
                        
                 print("Rock Crushed Scisorssor, I'm sorry you lost the square")
    elif ((player == ("Rock")) and  (Comp =="Lizard") or (player == ("Lizard")) and  (Comp =="Rock")):
             if(player == ("Rock")):
                 score_player = score_player + 1
                 print (player +" You win the square ", score_player) 
                
             else: 
                 score_Comp = score_Comp + 1
                     
                 print("Rock Smash Lizard, I'm sorry you lost the square")
    elif ((player == ("Paper")) and  (Comp =="Rock") or (player == ("Rock")) and  (Comp =="Paper")):
             if(player == ("Paper")):
                score_player = score_player + 1
                print (player +" You win the square ",score_player)
             else:
                 score_Comp = score_Comp + 1
                    
                 
                 print("Paper Cover Rock, I'm sorry you lost the square")
    elif ((player == ("Paper")) and  (Comp =="Spock") or (player == ("Spock")) and  (Comp =="Paper")):
             if(player == ("Paper")):
                 score_player = score_player + 1
                 print (player +"You win the square ", score_player)
             else:
                 score_Comp = score_Comp + 1
                     
                 print ("Paper disproves Spock, I'm sorry you lost the square")  
               
    elif ((player == ("Paper")) and  (Comp =="Scisorssor") or (player == ("Scisorssor")) and  (Comp =="Paper")):
             if(player == ("Scisorssor")):
                 score_player = score_player + 1
                 print (player +" You win the square ",score_player)
             else:
                 score_Comp = score_Comp + 1
                 
                 print("Scisorssor Cuts Paper, I'm sorry you lost the square")
    elif ((player == ("Lizard")) and  (Comp =="Scisorssor") or (player == ("Scisorssor")) and  (Comp =="Lizard")):
             if(player == ("Scisorssor")):
                 score_player = score_player + 1
                 print (player +" You win the square ",score_player)
             else:
                 score_Comp = score_Comp + 1
                     
                
                 print("Scisorssor Descap Lizard, I'm sorry you lost the square")
    elif ((player == ("Spock")) and  (Comp =="Scisorssor") or (player == ("Scisorssor")) and  (Comp =="Spock")):
             if(player == ("Spock")):
                 score_player = score_player + 1
                 print (player +" You win the square ", score_player)
             else:
                score_Comp = score_Comp + 1
                     
                print("Spock Smashs Scisorssor, I'm sorry you lost the square")
    elif ((player == ("Spock")) and  (Comp =="Rock") or (player == ("Rock")) and  (Comp =="Spock")):
             if(player == ("Spock")):
                 score_player = score_player + 1
                 print (player +" You win the square ", score_player)
             else:
                score_Comp = score_Comp + 1
                
                print("Spock decaption Rock")
    elif ((player == ("Lizard")) and  (Comp =="Spock") or (player == ("Spock")) and  (Comp =="Lizard")):
             if(player == ("Lizard")):
                 score_player = score_player + 1
                 print (player +"You win the square ", score_player)
             else:
                score_Comp = score_Comp + 1
                  
                print("Lizard Poisons Spock")
    elif ((player == ("Lizard")) and  (Comp =="Paper") or (player == ("Paper")) and  (Comp =="Lizard")):
             if(player == ("Lizard")):
                 score_player = score_player + 1
               
             else:
                score_Comp = score_Comp + 1
                
                print("Lizard Eats Paper")
    count = count +1
    print (player + "Score = " + str(score_player) + "----" +"Computer Score=  " + str(score_Comp) )
if (score_player > score_Comp ):
   print (player +"  Our player win the RSPLS game and beat the Computer with ," + str(score_player) +  " | "+ str(score_Comp))
elif (score_player < score_Comp):
    print (player +"  Sorry! the computer win the game  ," + str(score_player) + " | "+ str(score_Comp))
elif (score_player == score_Comp):
    print ("We have no winner the game is draw player score = Computer score  " + str(score_player) + " | "+ str(score_Comp))
   
   