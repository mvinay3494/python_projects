import moviepy
from moviepy.editor import *
import re
import sys
import time

prog_start_time = time.time()
movie_name = str(sys.argv[1])
subtitle = str(sys.argv[2])
keyword = str(sys.argv[3])
output_loc = str(sys.argv[4])
times = []
openFile = open(subtitle, 'r')
readFile = openFile.readlines()
previousLine = ""
for line in readFile:
    if keyword in line:
        # print(line)
        if previousLine[:1].isdigit():
            lines = re.split(r"-->|,", re.sub(" ", "", previousLine))
            times.append((lines[0], lines[2]))
    previousLine = line
# print(times)
openFile.close()

clips = []
clip = VideoFileClip(movie_name)
for value in times:
    start_time = sum(x * int(t) for x, t in zip([3600, 60, 1], value[0].split(":")))
    end_time = sum(x * int(t) for x, t in zip([3600, 60, 1], value[1].split(":")))
    # print("start time = "+str(start_time)+" end time = "+str(end_time))
    clip_cut = clip.subclip(start_time, end_time)
    clips.append(clip_cut)

final = concatenate_videoclips(clips)
final.write_videofile(output_loc+"compiled.mp4")
# ffmpeg_extract_subclip(movie_name, 20, 30, target-name="compiled.mp4")


prog_end_time = time.time()

print("Time taken to create the file is " + str(round((prog_end_time - prog_start_time), 2)))