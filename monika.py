import base64
from PIL import Image
from PIL import ImageOps

INPUT_PATH = 'characters/monika.chr'
OUTPUT_PATH = 'decoded/monika.txt'

def main():
    img = Image.open(INPUT_PATH)
    img = img.crop((330, 330, 470, 470))

    width, height = img.size

    text = ''
    tmp = ''

    for y in range(height):
        for x in range(width):
            p, *_ = img.getpixel((x, y))
            tmp += str(int(p / 255))

            if len(tmp) == 8:
                text += chr(int(tmp, 2))
                tmp = ''

    decoded = base64.b64decode(text).decode('utf-8')

    with open(OUTPUT_PATH, 'w') as f:
        f.write(decoded)

    print(OUTPUT_PATH)

if __name__ == "__main__":
    main()
