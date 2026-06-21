import sys
from PIL import Image
import os

'''
GIFSPLIT by Kellen

This is a tool to split a gif into pngs of each frame.
Drag the gif onto the script and it will dump all frames into a folder called frames.
'''

file_path = os.path.abspath(os.path.dirname(__file__))
os.makedirs(file_path + "\\frames\\")

with Image.open(sys.argv[1]) as im:
    for i in range(im.n_frames):
        im.seek(i)
        im.save('{}{}{}.png'.format(file_path, "\\frames\\", i))