
# 🟡 Yellow Marker Mouse Controller

A simple, real-time computer vision project that maps the position of a physical yellow marker in your webcam feed to control your computer's mouse cursor.

## 📝 Problem Statement

Traditional computer mice can sometimes be inconvenient or inaccessible for quick, simple interactions. This project addresses the need for a **hands-free, motion-based input method** by utilizing a common, easily identifiable object (a yellow marker) as a direct input device. The goal is to translate the 2D movement of this object into precise cursor movements on the screen, with an added feature to simulate a mouse click based on momentary stillness.

## 🎯 Scope of the Project

This project is a proof-of-concept focusing purely on marker tracking and basic input simulation:

1.  **Color Tracking:** Identify and isolate a specific color range (Yellow) within the webcam feed using the HSV color space.
2.  **Cursor Mapping:** Calculate the centroid of the detected object and map its pixel coordinates (from the camera frame) to the absolute screen coordinates (desktop resolution).
3.  **Mouse Control:** Use the `pyautogui` library to move the actual system cursor based on the tracked object's position.
4.  **Click Simulation:** Implement a rudimentary "dwell-to-click" mechanism. If the marker remains relatively stationary for a defined period (22 frames), a left mouse click is simulated at the current cursor position.

**Out of Scope:** Advanced features such as scrolling, right-clicking, gesture recognition, or calibration routines for varying lighting conditions are not included in this version.

## 🧑‍💻 Target Users

This tool is primarily intended for:

*   **Hobbyists and Learners:** Individuals learning about real-time computer vision, color segmentation, and basic hardware interaction using Python libraries like OpenCV and PyAutoGUI.
*   **Accessibility Experimenters:** Those looking for simple, non-contact input alternatives, although robust accessibility features are not guaranteed.
*   **Quick Prototyping:** Anyone needing a fast way to move a cursor across a screen using simple, physical objects.

## ✨ High-Level Features

| Feature | Description |
| :--- | :--- |
| **Real-Time Tracking** | Processes video feed from the default webcam (index 0) frame-by-frame. |
| **Color Segmentation** | Uses custom HSV ranges to robustly isolate the target yellow object from the background. |
| **Cursor Mapping** | Dynamically scales the object's movement to match the dimensions of the user's primary monitor. |
| **Flipping for Intuition** | The camera feed is horizontally flipped so that moving the marker left moves the cursor left, matching user intuition. |
| **Dwell-to-Click** | A simple, built-in mechanism that triggers a left mouse click after the marker has remained stable for a short duration. |
| **Contour Filtering** | Filters out small, irrelevant noise (like dust or small reflections) by requiring the tracked contour to exceed a minimum area (`rad > 12`). |
