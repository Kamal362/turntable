guess_num = 0
secrete_num = 20
print("Guess number between 1 - 50")

def guessNum(num):
    num = int(input("Enter a number: "))
    if num <=50:
       if guessNum == secrete_num:
           print("Congratulations, you win!")
       else:
           print("sorry your guess is outside the range")    

print(guessNum(secrete_num))
    