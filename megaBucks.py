
import os
import random
from art import logo


megaBuckNums= []
megaNumberGenerated = 0
x = 0


print(logo)


d = int(input('How Many Lines of megabucks do you want to play?'))


def generateNums():
  n = 0
  
  while n < 6:
    
    megaNumberGenerated= random.randint(1,50)
    #print(megaNumberGenerated)
    if megaNumberGenerated not in megaBuckNums:
      megaBuckNums.append(megaNumberGenerated)
      megaBuckNums.sort()
      n += 1  

while x < d:
  generateNums()
  printed_nums = ""
  for numbs in megaBuckNums:
    printed_nums = printed_nums + str(numbs) + ", "
      

    #cdprint(f"your numbers are {megaBuckNums}")
    print(f"your numbers are {printed_nums}")
    x += 1 
    megaBuckNums= []

 
go_again = input("Do you like these numbers? Yes or No: ").lower()
if go_again == "yes":
  print("Good Luck!!!")
else:
   generateNums()

