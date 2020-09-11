#Chinmay Keskar
#October 25th, 2019
#island_dice.py
#How to build an island dice game using random numbers, loops, and functions?
import random #importing the random function

options = True #setting options to be true
while options: #setting while loop for options
    helpmenu = input('Welcome to the Island Dice game! Enter s to start, q to quit, or h for help.') #asking user to input s to start, q to quit, or h for help
    if helpmenu == 's': #checking if user entered s
        print('You start with a 1000 shells.')

        #declaring all global variables with their respective values
        risked_shells = 0
        dicetotal = 0 
        i= 0 
        compare = 0 
        remainshells = 0 
        numshells = 1000 
    
        
        
        
        def highorlow(): #creating a function to ask user to enter high or low, casts the input into a string, and then returns highorlow
            highorlow = input('Enter high or low:') 
            highorlow = str(highorlow) 
            return highorlow 

        def dicerolls(s): #creating a function that rolls two dice and takes their total - variable s is passed as the parameter. The program then prints the roll total by concatenation and returns the value
            a = random.randint(1,6) 
            b = random.randint(1,6) 
            total = a+b 
            print('roll total:' + str(total))  
            return total 
        
        def riskamount(x): #creating a function that asks user to enter an amount of shells to risk - variable x is passed as the parameter. This function also makes sure the player only risks a positive amount of shells.
            x = input('Enter how many shells you want to risk:') #asking user to enter number of shells to risk
            x = int(x) #making x equal the integer cast of itself
            while x <= 0: #while loop that runs while x is less than or equal to 0 - x represents amount of risked shells
                print('You can only risk a positive amount of shells.') #entering error message if user enters a risk amount less than or equal to 0
                x = input('Enter how many shells you want to risk:') #asking user to enter number of shells to risk
                x = int(x) #making x equal the integer cast of itself
            while x > numshells: #while loop that runs while x is more than number of shells
                print('You do not have enough shells to risk that amount.') #printing error message that tells user that they cannot risk that many shells
                x = input('Enter how many shells you want to risk:') #asking user to enter number of shells to risk
                x = int(x) #making x equal the integer cast of itself
            return x  #returning x to wherever the function was called
            

        def compareguess(o): #creating a function that compares user choice of high/low with dice total
            if bet == 'high' and i >= 1 and i <= 6: #checking if bet was not equal to low and i is from 1 to 6 ( i represents dice roll total)
                print('Bust! Wrong call.') #print statement that tells user that they had a wrong call.
                o -= risked_shells #making o equal itself minus risked shells
            elif i == 7: #checking if i is 7
                print('7 is an automatic bust.') #print statement that tells user that they had a bust
                o -= risked_shells #making o equal itself minus risked shells
            elif bet == 'low' and i >= 8 and i <= 12: #checking if bet is low and i is greater than/equal to 8 and less than/equal to 12
                print('Bust! Wrong Call.') #print statement that tells user that they had a wrong call
                o -= risked_shells #making o equal itself minus risked shells
            elif bet == 'low' and i >= 1 and i<= 6: #checking if bet is low and i is greater than/equal to 1 and less than/equal to 6
                print('Good Call!') #print statement that tells user that they had a good call
                o =  risked_shells*2 + o #making o equal itself plus twice the risked shells
            elif bet == 'high' and i >= 8 and i <= 12: #checking if bet is high and i is greater than/equal to 8 and less than/equal to 12
                print('Good Call!.')#print statement that tells user that they had a good call
                o = risked_shells*2 + o #making o equal itself plus twice the risked shells
            print('shells remaining:' + str(o)) #concatenating 'shells remaining' with the string cast of o
            return o #returning o
            




       
       
        while numshells > 0: #while loop that runs while number of shells is more than 0
            risked_shells = riskamount(risked_shells) #passing risked shells through the function riskamount() and making that equal risked shells
            bet = highorlow() #calling the highorlow() function to bet
            i = dicerolls(i) #passing i through function dicerolls() and making i equal to that
            numshells = compareguess(numshells) #passing numshells through function compareguess() and making that equal numshells
           
            
            
            
            
        

    if helpmenu == 'h': #checking if user entered h for help
        #printing help statements along with blanks for indentation
        print('')
        print('Enter number of shells to risk and choice of high/low to the prompts.')
        print('The program will roll two dice and find their total. A total from 1 to 6 is low and a total from 8 to 12 is high. 7 is an automatic bust')
        print('if the call is right, the amount of shells are doubled and added to the total. if the call is wrong, the shells at risk are lost.')
        print('do not try to risk an amount of shells that is greater than what you have.')
        print('')
    if helpmenu == 'q': #checking if user entered q to quit
        #printing farewell message and making options equal false so that the program ends
        print('Thanks for playing Island Dice!')
        options = False

        
            
                

            
                
                

        

        


        
            

        

        
            
            

        

        
            

        

        

       
            
            
        
        
    
