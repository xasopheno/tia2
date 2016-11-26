ffmpeg -f image2 -r 30 -i %04d.bmp -c:v libx264 -pix_fmt yuv420p out.mp4
