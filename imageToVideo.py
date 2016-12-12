ffmpeg -loop 1 -i rosepersimmon.jpg -c:v libx264 -t 60 -pix_fmt yuv420p -vf scale=1920:1080 rosepersVid.mp4
