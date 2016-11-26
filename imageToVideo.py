ffmpeg -loop 1 -i red.png -c:v libx264 -t 15 -pix_fmt yuv420p -vf scale=320:240 redVid.mp4
