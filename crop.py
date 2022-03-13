#!"C:\Users\Mauro_Oliveira\AppData\Local\Programs\Python\Python310\python.exe"

from PIL import Image
import os

img_folder = "C:\\Users\\Mauro_Oliveira\\Pictures\\Screenshots"
output_folder = "C:\\Users\\Mauro_Oliveira\\Pictures\\Screenshots\\cropped"
file_extension = ".png"

def crop():
    for file_name in os.listdir(img_folder):
        file_path = os.path.join(img_folder, file_name)
        output_file_path = os.path.join(output_folder, file_name)

        if not os.path.isfile(file_path):
            continue
        if not file_name.endswith(file_extension):
            continue
        if os.path.exists(output_file_path):
            continue

        with Image.open(file_path) as image:
            imCrop = image.crop((0, 0, 1920, 1080))
            imCrop.save(output_file_path, "BMP", quality=100)
            print(f"File {file_name} successfully croped!")

if __name__ == "__main__":
    crop()