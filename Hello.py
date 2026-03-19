from PIL import Image, ImageEnhance


img = Image.open("scania.jpg")


resized = img.resize((400, 400))


grayscale = resized.convert("L")


contrast = ImageEnhance.Contrast(grayscale)
high_contrast = contrast.enhance(2)

grayscale.save("resultat.jpg")
