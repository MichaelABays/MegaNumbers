

import random

megaBuckNums= []
megaNumberGenerated = 0
x = 0


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
  print(f"your numbers are {megaBuckNums}")
  x += 1 
  megaBuckNums= []
 



