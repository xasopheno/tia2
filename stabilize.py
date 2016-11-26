import os
from os import system

os.chdir('/Users/dannymeyer/documents/projects/tia2/videosToStabilize')


videos = os.listdir('/Users/dannymeyer/documents/projects/tia2/videosToStabilize')

videosToStabilize = '/Users/dannymeyer/documents/projects/tia2/videosToStabilize'

for video in videos:
  if video.endswith('.MOV'):
    print video
    detectTransformVectors = 'ffmpeg -i ' + video + ' -vf vidstabdetect=stepsize=6:shakiness=8:accuracy=9:result=transform_vectors.trf -f null -'
    stabilzeVideo = 'ffmpeg -i  ' + video + ' -vf vidstabtransform=input=transform_vectors.trf:zoom=1:smoothing=30,unsharp=5:5:0.8:3:3:0.4 -vcodec libx264 -preset slow -tune film -crf 18 -acodec copy ' + video + 'stable.MOV'
    
    os.system(detectTransformVectors)
    os.system(stabilzeVideo)
    print video + ' stablized, my friend.'



# get framerate
# ffmpeg -i filename

# detect transform_vectors
# ffmpeg -i londonpark.MOV -vf vidstabdetect=stepsize=6:shakiness=8:accuracy=9:result=transform_vectors.trf -f null -

# stabilze video
# ffmpeg -i londonpark.MOV -vf vidstabtransform=input=transform_vectors.trf:zoom=1:smoothing=30,unsharp=5:5:0.8:3:3:0.4 -vcodec libx264 -preset slow -tune film -crf 18 -acodec copy SMOOTH_OUTPUT_VIDEO.MOV
