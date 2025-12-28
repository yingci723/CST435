This project demonstrates parallel image processing using Python to efficiently process multiple images. 
It applies a sequence of filters for grayscale, Gaussian blur, Sobel edge detection, sharpening, and brightness adjustment on datasets of different sizes (dataset_100, dataset_200, etc.). 
The project compares multiprocessing and concurrent.futures to show how parallel execution improves performance.

Features
- Supports multiple datasets with different sizes.
- Uses multiprocessing.Pool and ProcessPoolExecutor for parallel processing.
- Saves processed images in corresponding output folders (output_100, output_200, etc.).
- Prints process IDs and runtime for performance tracking.

Infrastructure Setup 
1. Instance Configuration 
- Navigate to the Compute Engine section in the Google Cloud Console.
- Select Create Instance.
- Machine Family: Select General purpose, Series E2.
- Machine Type: Select E2 series and e2-highcpu-8 (8 vCPU ,4 core, 8 GB memory)
- Boot Disk: Select Debian GNU/Linux 12 (bookworm) with 20 GB storage.
- Firewall: Default settings are sufficient.

3. Deployment 
- Click Create to provision the resource.
- Once the Status indicator turns green, click SSH to establish a secure shell 
connection. 

How to Run
1. Set up Python environment and install dependencies:
- $ sudo apt update
- $ sudo apt install -y python3-pip python3-venv
- $ python3 -m venv venv
- $ source venv/bin/activate
- $ pip install pillow numpy 

2. Upload and unzip your datasets:
- $ sudo apt update
- $ sudo apt install -y unzip
- $ unzip dataset.zip 

3. Run the scripts:
- python main_multiprocessing.py
- python main_concurrent.py

Notes
- Adjust the number of processes/workers in the scripts [1, 2, 4].
- Ensure dataset folder names match the scripts (dataset_100, dataset_200, etc.).
- Output images are saved in output_100, output_200, etc.
