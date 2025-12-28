import os
import time
from concurrent.futures import ProcessPoolExecutor
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
        tasks = [(img, output_folder) for img in images]  # list of tuples

        print(f"\nFor running {size} dataset ({len(images)} images)")

        for p in [1, 2, 4]:
            print(f"Starting processing with {p} worker(s)...")
            start = time.time()

            with ProcessPoolExecutor(max_workers=p) as executor:
                # Pass the tuple tasks, because process_image expects a single tuple argument
                list(executor.map(process_image, tasks))

            end = time.time()
            print(f"concurrent.futures | workers={p} | time={end-start:.2f}s")