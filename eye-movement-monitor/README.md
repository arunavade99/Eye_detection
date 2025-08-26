# Eye Movement Monitor

This project is designed to monitor eye movements using a webcam feed. It is particularly useful for applications such as exam proctoring, where it is essential to ensure that the participant's gaze remains within a designated area.

## Project Structure

```
eye-movement-monitor
├── src
│   ├── main.py          # Entry point for the application
│   ├── utils
│   │   └── detection.py # Functions for detecting eye movements
│   └── config
│       └── settings.py  # Configuration settings for the application
├── requirements.txt     # List of dependencies
└── README.md            # Project documentation
```

## Installation

To set up the project, follow these steps:

1. Clone the repository:
   ```
   git clone <repository-url>
   cd eye-movement-monitor
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   python src/main.py
   ```

2. The application will initialize the webcam feed and display a bounding box on the screen. It will monitor the eye movements within this box.

3. Ensure that your face is visible within the webcam feed for accurate detection.

## Configuration

You can adjust the parameters for eye movement detection in the `src/config/settings.py` file. This includes:

- Dimensions of the bounding box
- Sensitivity thresholds for detecting eye movements

## Dependencies

The project requires the following libraries:

- OpenCV
- MediaPipe
- NumPy
- PyAutoGUI (if applicable)

Make sure to install these libraries using the `requirements.txt` file.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.