from PIL import Image
from PIL import ImageOps

INPUT_PATH = 'characters/natsuki.chr'
OUTPUT_PATH = 'decoded/natsuki.jpg'

def main():
    img = Image.open(INPUT_PATH)
    img = ImageOps.invert(img)
    img = ImageOps.flip(img)

    img.save(OUTPUT_PATH)

    print(OUTPUT_PATH)

if __name__ == "__main__":
    main()
