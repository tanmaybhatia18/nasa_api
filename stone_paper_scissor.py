import random
b=int(input("press 1 for paper\npress 2 for stone\npress 3 for scissor\n"))
items=["scissor","paper","stone"]
r=random.choice(items)
if(b==1):
    print("Our choice:paper")
    print("Computer's choice:",r)
elif(b==2):
    print("Our choice:stone")
    print("Computer's choice:",r)
elif(b==3):
    print("Our choice:scissor")
    print("Computer's choice:",r)
