import random

n = random.randint(1,90)
#print(n)

guess=0

attempts=0

while guess!=n:
    guess=int(input("Enter Number: "))
    attempts+=1
    if guess>n:
        print("Too High")
    elif(guess<n):
        print("Too Low")
    else:
        print("Correct")

    
print("It took ",attempts, "attempts")