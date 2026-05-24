import random
l=["Rock","Paper","Scissor"]
while True:
    c=int(input("""\t---------------GAME STARTS-------------------
                   1).Wanna play?
                   2).Don't Wanna play?
                   Enter your choice:"""))
    
    if(c==1):
        uscore=0
        cscore=0
        for i in range(5):
        
            uch=int(input("""\t############ Select your Weapon ################
                            1).Rock
                            2).Paper
                            3).Scissor
                            Your choice:"""))
            cch=random.choice(l)
            if(uch==1):
                uch="Rock"
            elif(uch==2):
                uch="Paper"
            elif(uch==3):
                uch="Scissor"
            else:
                print("Invalid Choice")

            if(uch==cch):
                print("\nAhhhh.....You unfortunately guessed same a the opponent!!!!.....DRAW is what it is")
                print("Both gain 1 Point\n")
                uscore+=1
                cscore+=1
            elif((uch=="Rock" and cch=="Scissor") or (uch=="Paper" and cch=="Rock") or (uch=="Scissor" and cch=="Paper")):
                print("\nYou won this round, 2 points for you!!!!\n")
                uscore+=2
            elif((cch=="Rock" and uch=="Scissor") or (cch=="Paper" and uch=="Rock") or (cch=="Scissor" and uch=="Paper")):
                print("\nUnfortunately you lost this round and opponent won, 2 points for opponent\n")
                cscore+=2
            else:
                print("\nInvalid Choice by the user....So this round will be skipped\n")
                
            
        if(uscore==cscore):
            print("Your score is:",uscore,". \nOpponent's score is:",cscore)
            print("DRAW")
        elif(uscore>cscore):
            print("Your score is:",uscore,". \nOpponent's score is:",cscore)
            print("Yayyyyyy...You Won!!!")
        else:
            print("Your score is:",uscore,". \nOpponent's score is:",cscore)
            print("Unfortunately you lost....Better luck next time")
    elif(c==2):
        exit()
    else:
        print("Invalid Input")
    
