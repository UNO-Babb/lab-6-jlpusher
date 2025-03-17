#DiceRoll.py
#Name: Jessica Pusher
#Date: 3.16.25
#Assignment: DiceRoll.py
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  
  rollCount = input("How many times should we roll the dice?")
  rollCount = int(rollCount)

  for r in range(rollCount):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    diceSum = dice1 + dice2  #adding dice values together
    rolls[diceSum-1] = rolls[diceSum-1] + 1
   
  #find the sum total of the two dice
  
  #print statictics for dice rolls
  dice = 1
  for count in rolls: 
    ratio = count/rollCount
    percent = ratio*100
    print(dice, ":", count, ":", percent, "%")
    dice = dice + 1

  print(rolls)

if __name__ == '__main__':
  main()
