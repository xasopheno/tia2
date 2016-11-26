import os
from os import walk

blueFiles = os.listdir('/Users/dannymeyer/documents/projects/tia2/bluevid')
redFiles = os.listdir('/Users/dannymeyer/documents/projects/tia2/redvid')


n = 0
suffix = '.bmp'
# for filename in blueFiles:
#     if filename.endswith(".bmp"):
#         os.rename(filename, str('%04d') % n + '.bmp')
#         n += 2

# print blueFiles
# print redFiles

for filename in redFiles:
  if filename.endswith(".bmp"):
    print filename
    os.rename('/Users/dannymeyer/documents/projects/tia2/redvid/' + filename, str('%04d') % n + '.bmp')
    n += 2


for filename in blueFiles:
  if filename.endswith(".bmp"):
    print filename
    os.rename('/Users/dannymeyer/documents/projects/tia2/bluevid/' + filename, str('%04d') % n + '.bmp')
    n += 1
