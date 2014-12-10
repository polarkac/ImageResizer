import os

import PIL

def iterateThroughImages(folderPath, minimumSize=(1920, 1080)):
    pass

if __name__ == '__main__':
    folderPath = None
    while True:
        folderPath = input('Type path to image folder: ')
        if os.path.isdir(folderPath):
            break
        else:
            print('You have to type existing path!')

    minImageSize = ()
    while len(minImageSize) != 2:
        inputSize = input('Minimum image size (1920x1080): ')
        inputSize = tuple(inputSize.split('x'))
        try:
            width = int(inputSize[0])
            height = int(inputSize[1])
            if width <= 0 or height <= 0:
                raise ValueError
            minImageSize = (width, height)
        except (IndexError, ValueError):
            print('You have to type valid size!')

    iterateThroughImages(folderPath, minImageSize)
