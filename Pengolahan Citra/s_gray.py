from PIL import Image #import library pillow

citra = Image.open("gambar.jpg") #open image file
gray = citra.convert('L') #convert image file to grayscale
gray.show() #show image
