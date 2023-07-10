from PIL import Image
import pytesseract
import sys
import re

SCREENSHOT_PATH = '/Users/ken/Library/Application Support/minecraft/screenshots/'

def getCoordinates(path):
    image = Image.open(path)
    allText = pytesseract.image_to_string(image)
    coordinatesLine = [line for line in allText.splitlines() if line.startswith('Block')]
    coordinatesLine = [re.sub(r'^Block:\s+', '', line) for line in coordinatesLine]
    coordinatesLine = [re.sub(r'\s+\[.+\]$', '', line) for line in coordinatesLine]

    coordinates = coordinatesLine[0]
    return coordinates

imagePath = sys.argv[1]
print(getCoordinates(imagePath))

