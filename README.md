# coloured-object-tracker


Color Mouse (Webcam Yellow Object Tracker):
Control your mouse cursor with a yellow object in front of your webcam!
Hand-written Python script lets you move and click the mouse with simple gestures, using OpenCV and pyautogui.

Features:
Move mouse cursor using a yellow object via camera tracking.

Mouse click is triggered when the object holds mostly still for a split second.

Fast and fun way to interact with your PC—no physical mouse needed.

Customizable sensitivity and color bounds (tune to your marker or toy).

Requirements:
Python 3.8+

OpenCV (cv2)

NumPy (numpy)

PyAutoGUI (pyautogui)

Installation
Install dependencies (if needed):

text
pip install opencv-python numpy pyautogui
Download or copy the provided Python script (usually named color_mouse.py).

Usage
Run the script:

text
python color_mouse.py
Hold a yellow object (highlighter, toy, etc.) in front of your webcam.

Move the object—your cursor will follow!

Keep the object steady for about half a second to trigger a left mouse click.

Customization
For different lighting or color tones, tweak the color bounds in the script:

python
YELLOW_LO = np.array([20,100,100])
YELLOW_HI = np.array([40,255,255])
You can also adjust the sensitivity for click detection by changing NEED_STEADY.

Troubleshooting
If the webcam doesn’t work, check cables or camera permissions.

For bad detection, adjust color bounds or improve room lighting.

Credits, License, and Disclaimer
Hand-built with Python and OpenCV for fun home automation/experimentation.
No warranty. Use and modify freely.
Name: Shashwat Mishra
Reg.no: 25BCY10080
