import os

from PIL import Image

def createWorkingDirectories(folderPath):
    os.mkdir(os.path.join(folderPath, 'original'))
    os.mkdir(os.path.join(folderPath, 'resized'))

def iterateThroughImages(folderPath, minimumSize=(1920, 1080)):
    imageFiles = [
        image for image in os.listdir(folderPath)
        if os.path.isfile(os.path.join(folderPath, image))
    ]
    for imageFile in imageFiles:
        try:
            image = Image.open(os.path.join(folderPath, imageFile))
        except OSError:
            continue

        resizeImage(image, folderPath, minimumSize)

def resizeImage(image, folderPath, minimumSize):
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
        if not inputSize:
            inputSize = (1920, 1080)
        else:
            inputSize = tuple(inputSize.split('x'))
        try:
            width = int(inputSize[0])
            height = int(inputSize[1])
            if width <= 0 or height <= 0:
                raise ValueError
            minImageSize = (width, height)
        except (IndexError, ValueError) as e:
            print(e)
            print('You have to type valid size!')

    try:
        createWorkingDirectories(folderPath)
    except OSError:
        print('Folders \'original\' or \'resized\' already exists in given path.')
        shouldContinue = input('Should we continue (yes, no): ')
        if shouldContinue != 'yes':
            exit()
    iterateThroughImages(folderPath, minImageSize)
