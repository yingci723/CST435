from PIL import Image
from filters import *
import os
import multiprocessing

def process_image(args):
    path, output_folder = args

    pid = multiprocessing.current_process().pid
    print(f"[PID {pid}] Processing {os.path.basename(path)}")

    img = Image.open(path).convert("RGB")

    img = grayscale(img)
    img = gaussian_blur(img)
    img = sobel_edge(img)
    img = sharpen(img)
    img = brightness(img, 30)

    os.makedirs(output_folder, exist_ok=True)
    img.save(os.path.join(output_folder, os.path.basename(path)))

    return os.path.basename(path)