def makeNumbers():
  n = 1
  x = 5
  y = 1

  groupOne = []
  groupTwo = []

  xUp = False
  yUp = True

  while n < 100:
    for i in range(1, x + 1):
      groupOne.append(int(n))
      n += 1

    for j in range(1, y + 1):
      groupTwo.append(int(n))
      n += 1    

    # if x == 1:
    #   xUp = True
    # if y == 5:
    #   yDown = False 
    if x > 1:
      x -= 1
    else:
      x = 5
    
    if y < 6:
      y += 1
    else:
      y = 1

  return groupOne, groupTwo

groupOne, groupTwo = makeNumbers()


print 'groupOne'
print groupOne

print 'groupTwo'
print groupTwo

