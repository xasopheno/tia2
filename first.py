import os
from os import walk
from os import system
import random
from path import path
import glob

from groups import linearNumbers, switch

videosToMix = os.listdir('/Users/dannymeyer/documents/projects/tia2/videosToMix')

def getVideoFiles(path):
  """
  Returns a random video file, chosen among the files of the given path.
  """
  files = videosToMix 
  availableFiles = []
  count = 0
  numFiles = len(files)
  while count < numFiles:
    if files[count].endswith('MOV'):
      availableFiles += [files[count]]
    count += 1
  # print availableFiles
  return availableFiles

getVideoFiles(videosToMix)

# choose two files
fileOne, fileTwo = getVideoFiles(videosToMix)


# while fileTwo == fileOne:
#   fileTwo == getRandomFile(videosToMix)

print fileOne, fileTwo
