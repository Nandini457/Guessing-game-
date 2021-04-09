print('this is guessing game')
import random
random_number = random.randrange(1,10)
guess = int(input("what could be the number"))
correct = False
print(random_number)

while not correct:
    if guess==random_number:
        print("congrats you gotr it")
        correct = True
    elif guess>random_number:
        print("too Low")
        break
    elif guess<random_number:
        print("too high")
        break
    else:
        print("try something else")
        break










