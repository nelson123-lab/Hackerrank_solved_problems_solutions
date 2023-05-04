# get the user guess the no
import random

def computerguess(lowval, highval, randnum, count =0):
    if highval >= lowval:
        guess = lowval + (highval - lowval) // 2
        if guess == randnum:
            return count

        elif guess > randnum:
            count = count + 1
            return computerguess(lowval, guess-1, randnum, count)

        else:
            count = count + 1
            return computerguess(guess+1, highval, randnum, count)
    else:
        return -1

randnum = random.randint(1,101)
count =0
guess =-99

while (guess != randnum):

    guess = (int) (input("Enter the no between 1  and 100:"))
    if guess < randnum:
        print("higher")
    elif guess > randnum:
        print("lower")
    else:
        print("You guessed it!")
        break
    count = count + 1
print("you took" + str(count) + "guesses")
print("Computer took " + str(computerguess(0,100, randnum)) + " guesses")
