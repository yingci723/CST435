import os
import time
from multiprocessing import Pool
from worker import process_image

DATASET_SIZES = [100, 200, 300, 400]

def get_images(folder):
    return [os.path.join(folder, f) for f in os.listdir(folder) if f.lower().endswith(".jpg")]

if __name__ == "__main__":

    for size in DATASET_SIZES:
        dataset_folder = f"dataset_{size}"
        output_folder = f"output_{size}"
        os.makedirs(output_folder, exist_ok=True)

        images = get_images(dataset_folder)
        tasks = [(img, output_folder) for img in images]  # create tuple tasks

        print(f"\nFor running {size} dataset ({len(images)} images)")

        for p in [1, 2, 4]:
            print(f"Starting processing with {p} process(es)...")
            start = time.time()

            with Pool(processes=p) as pool:
                pool.map(process_image, tasks)  # pass tuples

            end = time.time()
            print(f"multiprocessing | processes={p} | time={end-start:.2f}s")
