#Run: python -u Random1.py
#This program prints out 3 animals randomly

import random
dDict = dict() # Create dictionary 
dDict[1] = "Tiger" # Populate the dictionary
dDict[2] = "Elephant" # Populate the dictionary
dDict[3] = "Lion" # Populate the dictionary

iSpin = 0
while True:
  print('Press Enter to spin; q to quit')
  sText = input()
  if (sText.lower() == 'q'): #capture q to break loop
    break

  if (sText == ''): #capture Enter Key
    iNumber = random.randint(1,3)
    sAnimal = '|' + dDict[iNumber] + '|'
    for i in range(1, 3):
      iNumber = random.randint(1,3)
      sAnimal = sAnimal + dDict[iNumber] + '|' #add more animal
    iSpin = iSpin + 1
    print('Spin: ' + str(iSpin))
    print('Animals: ' + sAnimal)
print('-------------')
