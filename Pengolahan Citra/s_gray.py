from PIL import Image

citra = Image.open("gambar.jpg")
gray = citra.convert('L')
gray.show()
