import os
import glob
from PIL import Image

def genernateThumbnail(dir):
    for file in glob.glob(dir + '/*[jpg,png]'):
        img = Image.open(file)
        img.thumbnail([s * 0.2 for s in img.size])
        print(img.format, img.size, img.mode)
        name = os.path.join(dir, '..\cover', os.path.basename(file))
        img.save(name, img.format)
    print('done!')
    input()

if __name__ == '__main__':
    dir = os.path.abspath(os.path.dirname(__file__))
    genernateThumbnail(dir)