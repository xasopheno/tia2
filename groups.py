def linearNumbers(numImages):
  value = 2
  n = 1
  x = value
  y = 1

  xUp = False
  yUp = True 

  groupOne = []
  groupTwo = []

  while n < numImages:
    for i in range(1, x + 1):
      groupOne.append(int(n))
      n += 1

    for j in range(1, y + 1):
      groupTwo.append(int(n))
      n += 1    

    if x == 1:
      xUp = True
    if x == value:
      xUp = False
    if xUp == True:  
      x += 1
    else:
      x -= 1
      if x == value:
        xUp = False

    if y == value:
      yUp = False
    if y == 1:
      yUp = True
    if yUp == True:  
      y += 1
    else:
      y -= 1
      if y == 1:
        yUp = False

  return groupOne, groupTwo

# groupOne, groupTwo = linearNumbers(1400)

def switch(numImages):
  # back and forth between two videos equally
  value = 1
  n = 1
  x = 50
  y = 2

  groupOne = []
  groupTwo = []

  while n < numImages:
    for i in range(1, x + 1):
      groupOne.append(int(n))
      n += 1

    for j in range(1, y + 1):
      groupTwo.append(int(n))
      n += 1   

    # x += 1
    # y += 1
    
  return groupOne, groupTwo

# groupOne, groupTwo = switch(1200)

# print 'groupOne'
# print groupOne

# print 'groupTwo'
# print groupTwo

