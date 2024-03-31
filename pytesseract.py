import pytesseract as ts
from PIL import Image

img = Image.open("photos/sample_text.jpg")
print(ts.image_to_string(img))
