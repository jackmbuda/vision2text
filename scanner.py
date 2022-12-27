from PIL import Image
import subprocess
import pytesseract
import sys

if len(sys.argv) != 2:
    sys.exit("Photo directory required as CLI argument.")
else:
    target_dir = sys.argv[1]
    print("Directory being scanned:", target_dir)

result = subprocess.run(["pwd"], capture_output=True, text=True)
pwd = result.stdout.replace("\n", "")
result = subprocess.run(["ls", sys.argv[1]], capture_output=True, text=True)

files = []
buff = []
for c in result.stdout:
    if c == '\n':
        files.append(''.join(buff))
        buff = []
    else:
        buff.append(c)
else:
    if buff:
       files.append(''.join(buff))

for image in files:
    print("Image file being scanned: " + image)
    print(pytesseract.image_to_string(Image.open(pwd + "/" + target_dir + "/" + image)))