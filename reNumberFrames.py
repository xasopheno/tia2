import os
from os import walk
from os import system

blueFiles = os.listdir('/Users/dannymeyer/documents/projects/tia2/videoFolders/reNumberedImages')
# redFiles = os.listdir('/Users/dannymeyer/documents/projects/tia2/redvid')
# allFiles



# for filename in blueFiles:
#     if filename.endswith(".bmp"):
#         os.rename(filename, str('%04d') % n + '.bmp')
#         n += 2

# print blueFiles
# print redFiles
suffix = '.bmp'
# n = 0
# for filename in redFiles:
#   if filename.endswith(".bmp"):
#     print filename
#     os.rename('/Users/dannymeyer/documents/projects/tia2/redvid/' + filename, str('%04d') % n + '.bmp')
#     n += 2


n = 1
for filename in blueFiles:
  if filename.endswith(".bmp"):
    print filename
    os.rename('/Users/dannymeyer/documents/projects/tia2/videoFolders/reNumberedImages/' + filename, str('%04d') % n + '.bmp')
    n += 1



