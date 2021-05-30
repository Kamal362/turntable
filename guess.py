guess_num = 0
secerate_num = 14
try_again = False
inp = ""

print("Guess a number between one 1 - 50")

def tryAgain():
     print("Do you want to continue guessing? yes/no ")
     inp = str(input("=> choose: "))
     if inp == "yes" or "Yes" or "YES":
        try_again = True
        print("try again!")
     elif inp == "no" or "NO" or "No": 
        print("Thanks for using the program! bye")   
        try_again  
        #break

while guess_num !=secerate_num:
    guess_num = int(input("Quess the secrete number: "))
    if guess_num <= 50 and guess_num == secerate_num:
       print("Your are right!") 
    else:
        print("Error! Your number is outside the range")
        #print(try_again())
        if try_again:
           break
        else:
           tryAgain()
           
         
   
    
        