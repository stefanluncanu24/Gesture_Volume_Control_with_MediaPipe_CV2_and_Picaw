# Volume Control by Gesture

This project uses MediaPipe, OpenCV, and the Picaw Python library to enable intuitive volume control via hand gestures. Start by raising one hand to signal the intent to adjust the volume, then raise the second hand to control the volume using the distance between your thumb and index finger.

## Features

- **Real-Time Hand Tracking**: Detects and tracks the position of the hand in real-time using MediaPipe.
- **Volume Adjustment**: Interfaces with the system's audio to adjust the volume level based on the distance between the thumb and the index finger.

## Modules

- `HTM.py`: Contains the `handDetector` class for hand tracking.
- `main.py`: The main script that initializes the camera and processes the video stream.
- `VolumeHandControl.py`: Includes methods for processing frames and adjusting volume based on gesture recognition.

## Contributing

Feel free to fork this project and submit pull requests. You can also open an issue for bugs or feature requests.
