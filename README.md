
# Eye Detection & Eye-Controlled Mouse

This project uses OpenCV and MediaPipe to detect eyes and control your PC using eye movements. It also includes features for monitoring cheating by tracking eye and face positions.

## Features
- Eye-controlled mouse movement and click
- Virtual bounding box for monitoring (Prevent cheating)
- Face and pupil detection with alerts

## Setup Instructions

1. **Install Python dependencies:**
	- See `requirements.txt` for required packages.
	- Install with:
	  ```
	  pip install -r requirements.txt
	  ```
	- For PyTorch (if using CUDA), follow pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu128.

2. **Environment Setup:**
	- Make sure your webcam is connected.
	- If using GPU acceleration, set up CUDA and install compatible PyTorch.
