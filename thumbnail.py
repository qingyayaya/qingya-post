#!/usr/bin/python

import os
import glob
from PIL import Image

dir = os.path.abspath(os.path.dirname(__file__))

def genernateThumbnail():
    for post in glob.glob(dir + '/posts/*/'):
        file = glob.glob(post + 'cover/cover.*[jpg,png]')[0]
        img = Image.open(file)
        img.thumbnail([s * 0.2 for s in img.size])
        img.save(os.path.join(post, 'assets', os.path.basename(file)), img.format)
        print(img.filename, img.format, img.size, img.mode)
    print('done!')

if __name__ == '__main__':
    genernateThumbnail()