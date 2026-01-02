import os
import time
from concurrent.futures import ThreadPoolExecutor
from worker import process_image

DATASET_SIZES = [100, 200, 300, 400]

def get_images(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(".jpg")]

if __name__ == "__main__":
    
    for size in DATASET_SIZES:
        dataset_folder = f"dataset_{size}"
        output_folder = f"output_{size}"
        os.makedirs(output_folder, exist_ok=True)

        images = get_images(dataset_folder)
        tasks = [(img, output_folder) for img in images]  # list of tuples

        print(f"\nFor running {size} dataset ({len(images)} images)")

        for p in [1, 2, 4]:
            print(f"\nStarting processing with {p} thread(s)...")
            start = time.time()

            with ThreadPoolExecutor(max_workers=p) as executor:
                list(executor.map(process_image, tasks))

            end = time.time()
            print(f"concurrent.futures | threads={p} | time={end-start:.2f}s")
