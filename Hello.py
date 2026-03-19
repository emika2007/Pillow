from PIL import Image, ImageEnhance

# Öppna bild
img = Image.open("scania.jpg")

# 1. Skala om bilden
resized = img.resize((400, 400))

# 2. Gör bilden svartvit
grayscale = resized.convert("L")

# 3. Öka kontrasten
#contrast = ImageEnhance.Contrast(grayscale)
#high_contrast = contrast.enhance(2)

# 4. Kolorera den svartvita bilden
#colored = Image.colorize(high_contrast, black="blue", white="yellow")

# 5. Spegelvänd bilden
#mirrored = Image.mirror(grayscale)

# Spara resultatet
grayscale.save("resultat.jpg")
