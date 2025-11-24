import cv2
import numpy as np
import pyautogui
from random import randint

cap = cv2.VideoCapture(0)

# Getting screen dimensions - my laptop is kinda old
desk_w, desk_h = pyautogui.size()

# HSV values for yellow marker (used some random docs + trial/error)
lo = np.array([20,100,100])
hi = np.array([40,255,255])

print("Started! Put something yellow in front of your webcam and move it to control the mouse. Don't judge my code :)")

prevX, prevY, stillC = None, None, 0

while True:
    ret, cam_img = cap.read()
    if not ret:
        print("Webcam not working. Did you unplug it?")
        break

    # Mirror the image for easier control (always confuses me otherwise)
    cam_img = cv2.flip(cam_img, 1)
    frame_dims = cam_img.shape

    # Convert BGR to HSV because it's easier for color stuff
    hsv_img = cv2.cvtColor(cam_img, cv2.COLOR_BGR2HSV)

    # Generate mask for yellow
    mask = cv2.inRange(hsv_img, lo, hi)

    # Randomly erode/dilate, mostly out of habit
    n = randint(1,2)
    mask = cv2.erode(mask, None, iterations=n)
    mask = cv2.dilate(mask, None, iterations=n)

    cons, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if cons:
        main_blob = max(cons, key=cv2.contourArea)
        (curX, curY), rad = cv2.minEnclosingCircle(main_blob)

        # Only react if blob is decent sized (no dust bunnies please)
        if rad > 12:
            cv2.circle(cam_img, (int(curX),int(curY)), int(rad), (255,0,0), 3)

            # Use floats, but round before moving mouse (old habit)
            sx = int((curX/frame_dims[1])*desk_w)
            sy = int((curY/frame_dims[0])*desk_h)
            pyautogui.moveTo(sx, sy)

            # If hovering mostly still for a bit, trigger click
            if prevX is not None and abs(curX-prevX)<7 and abs(curY-prevY)<7:
                stillC += 1
                if stillC >= 22:
                    pyautogui.click()
                    print(f"Clicked at {sx},{sy} using yellow marker.")
            else:
                stillC = 0
            prevX, prevY = curX, curY
        else:
            stillC = 0
    else:
        stillC = 0

    cv2.imshow('YellowTracker', cam_img)
    cv2.imshow('YellowMask', mask)
    k = cv2.waitKey(1) & 0xFF
    if k==27:
        print("Done for now. Peace!")
        break

cap.release()
cv2.destroyAllWindows()
