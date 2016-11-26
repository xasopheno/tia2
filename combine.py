ffmpeg -framerate 1 -pattern_type glob -i '*.bmp' -c:v libx264 out.mov

ffmpeg -r 1/5 -i *.bmp
 -c:v libx264 -vf "fps=25,format=yuv420p" out.mp4

