# Example Python Program for thresholding

from PIL import Image


# Method to process the red band
def pixelProcRed(intensity):
    return 0


# Method to process the blue band
def pixelProcBlue(intensity):
    return intensity


# Method to process the green band
def pixelProcGreen(intensity):
    return 0


# Create an image object
imageObject = Image.open(r"C:\Users\Hemanta Dongol\Desktop\Image Processing\Lab 1\Image\image 2.jpg")

# Split the red, green and blue bands from the Image
multiBands = imageObject.split()

# Apply point operations that does thresholding on each color band
redBand = multiBands[0].point(pixelProcRed)
greenBand = multiBands[1].point(pixelProcGreen)
blueBand = multiBands[2].point(pixelProcBlue)

# Display the individual band after thresholding

# Red band of the Image after Thresholding:
redBand.show()

# Green band of the Image after Thresholding:
greenBand.show()

# Blue band of the Image after Thresholding:
blueBand.show()

# Create a new image from the threshold red, green and blue brands
# Merged Image after thresholding operation to have blue pixel in the foreground:
newImage = Image.merge("RGB", (redBand, greenBand, blueBand))

# Display the merged image after thresholding
newImage.show()
