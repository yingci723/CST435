from PIL import Image
from filters import *
import os
import multiprocessing
import threading   # <-- add this

def process_image(args):
    path, output_folder = args

    # Detect whether running in Process or Thread
    pid = multiprocessing.current_process().pid
    tid = threading.get_ident()

    # If multiprocessing uses multiple processes, each will have unique PID.
    # Thread version will show same PID but different Thread IDs.
    print(f"[PID {pid} | TID {tid}] Processing {os.path.basename(path)}")

    img = Image.open(path).convert("RGB")
    img = grayscale(img)
    img = gaussian_blur(img)
    img = sobel_edge(img)
    img = sharpen(img)
    img = brightness(img, 30)

    os.makedirs(output_folder, exist_ok=True)
    img.save(os.path.join(output_folder, os.path.basename(path)))

    return os.path.basename(path)
