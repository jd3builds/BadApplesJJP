from PIL import ImageEnhance, Image

def preprocess():
    img = Image.open("IMG_SCANNED.png")

    enhancer = ImageEnhance.Sharpness(image=img)
    enhance2 = ImageEnhance.Contrast(image=img)
    enhance3 = ImageEnhance.Color(image=img)

    # provides a varying sharpness for comparison

    factor = 9
    enhancer.enhance(factor)
    factor = 2
    enhance2.enhance(factor)
    factor = 0.5
    enhance3.enhance(factor)

    img.save("IMG_SCANNED.png")