import os
import random

# Set the source directory
dir_path = "C:\\Users\\hp\\Desktop\\uav\\flags"

# Get a list of all PNG files in the directory
png_files = [f for f in os.listdir(dir_path) if f.endswith(".png")]

# Shuffle the files randomly
random.shuffle(png_files)

# Rename each file with an alphabetic name from 'a.png' to 'z.png'
for i, f in enumerate(png_files):
    new_name = chr(ord('a') + i) + ".png"
    os.rename(os.path.join(dir_path, f), os.path.join(dir_path, new_name))