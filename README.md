# Mouse Control Using Hand Gestures

## Overview

This project explores the intersection of computer vision and user interface innovation, providing a touch-free way to control a computer using hand gestures.  
This project demonstrates how to control a computer mouse using hand gestures. By leveraging the power of computer vision and Python libraries, the system detects hand movements through a webcam and translates them into mouse actions. This provides a touch-free way to interact with a computer, ideal for innovative and assistive applications.

## Features
- Real-time hand tracking and gesture recognition.
- Control mouse movement using hand gestures.
- Perform mouse actions like left-click, right-click, and scroll.
- Uses a simple webcam, requiring no specialized hardware.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - OpenCV: For real-time computer vision and image processing.
  - Mediapipe: For hand detection and tracking.
  - PyAutoGUI: For controlling the mouse pointer and performing actions.

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- A functional webcam

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/Anshu370/Mouse-Control-Using-Hand-Gestures.git
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
3. Run the script:
   ```bash
   python main.py

## Usage

1. Ensure your webcam is connected and functioning.
2. Run the program using the command mentioned in the installation steps.
3. Move your hand in front of the camera to control the mouse pointer.
4. Use specific gestures to perform actions like clicking and scrolling:
   - Move hand: Controls the mouse pointer.
   - Gesture for click: Close a specific number of fingers to simulate a left or right click (as defined in the code).
   - Gesture for scroll: Move the hand up or down in a specific pattern.

## File Structure

- `main.py`: Entry point of the project, contains the logic for gesture recognition and mouse control.
- `requirements.txt`: Lists the dependencies required to run the project.
- Additional scripts and resources for hand gesture detection.

## Contributing

Contributions are welcome! If you'd like to improve this project, please:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with detailed information about your changes.

## License

This project is open-source and available under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- [Mediapipe](https://google.github.io/mediapipe/): For providing efficient and easy-to-use hand tracking tools.
- [PyAutoGUI](https://pyautogui.readthedocs.io/): For enabling mouse automation.
- [OpenCV](https://opencv.org/): For real-time image processing and computer vision functionalities.

## Contact

If you have any questions or suggestions, feel free to reach out:

- **GitHub**: [Anshu370](https://github.com/Anshu370)

