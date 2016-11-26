import os
from os import walk
from os import system
import random
from path import path

videosToMix = os.listdir('/Users/dannymeyer/documents/projects/tia2/videosToMix')

def getRandomFile(path):
  """
  Returns a random video file, chosen among the files of the given path.
  """
  files = videosToMix 
  index = random.randrange(0, len(files))
  if files[index].endswith('MOV'):
    return files[index]
  else:
    getRandomFile(videosToMix)

#choose two files
fileOne = getRandomFile(videosToMix)
fileTwo = getRandomFile(videosToMix)

while fileTwo == fileOne:
  fileTwo == getRandomFile(videosToMix)

print fileOne, fileTwo

# create folders for each file
folderOne = '/Users/dannymeyer/documents/projects/tia2/videoFolders/' + fileOne
folderTwo = '/Users/dannymeyer/documents/projects/tia2/videoFolders/' + fileTwo
os.mkdir(folderOne)
os.mkdir(folderTwo)

# move folder of videos
os.chdir('/Users/dannymeyer/documents/projects/tia2/videosToMix')

# separate videos into frames
cmdFileOne = 'ffmpeg -i ' + fileOne + ' -r 5/1 ' + folderOne + '/$filename%03d.bmp'
cmdFileTwo = 'ffmpeg -i ' + fileTwo + ' -r 5/1 ' + folderTwo + '/$filename%03d.bmp'

os.system(cmdFileOne)
os.system(cmdFileTwo)

finalDirectory = '/Users/dannymeyer/documents/projects/tia2/videoFolders/reNumberedImages'

os.chdir(finalDirectory)

def reNumberImages():
  suffix = '.bmp'
  videoOneImages = os.listdir(folderOne)
  videoTwoImages = os.listdir(folderTwo)

  n = 0
  for image in videoOneImages:
    if image.endswith('.bmp'):
      print image
      os.rename('/Users/dannymeyer/documents/projects/tia2/videoFolders/' + fileOne + '/' + image, str('%04d') % n + '.bmp')
      n += 2
  
  n = 1
  for image in videoTwoImages:
    if image.endswith('.bmp'):
      print image
      os.rename('/Users/dannymeyer/documents/projects/tia2/videoFolders/' + fileTwo + '/' + image, str('%04d') % n + '.bmp')
      n += 2

reNumberImages()

cmdBuild = 'ffmpeg -f image2 -r 50 -i %04d.bmp -c:v libx264 -pix_fmt yuv420p out.mp4'
os.system(cmdBuild)

# Clean up
print('Cleaning up')
d = path(finalDirectory)
files = d.walkfiles("*.bmp")
for file in files:
    file.remove()
    # print "Removed {} file".format(file)

os.rmdir(folderOne)
os.rmdir(folderTwo)

print('Complete')
print(fileOne, fileTwo)
print('have been combined')
