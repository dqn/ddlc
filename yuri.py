import base64

INPUT_PATH = 'characters/yuri.chr'
OUTPUT_PATH = 'decoded/yuri.txt'

def main():
    with open(INPUT_PATH) as f:
        yuri = f.read()

    decoded = base64.b64decode(yuri).decode('utf-8')

    with open(OUTPUT_PATH, 'w') as f:
        f.write(decoded)

    print(OUTPUT_PATH)

if __name__ == "__main__":
    main()
