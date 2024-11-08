import cv2
from pygame import mixer
import time

# Initialize Pygame mixer for playing sounds
mixer.init()

# Load background sounds and play them on a loop
background_sound_1 = mixer.Sound("./bgm/A.wav")  # Replace with your first background sound file path
background_sound_2 = mixer.Sound("./bgm/B.wav")  # Replace with your second background sound file path
background_channel_1 = background_sound_1.play(-1)  # Loop background sound A indefinitely
background_channel_2 = background_sound_2.play(-1)  # Loop background sound B indefinitely

# Load sounds
# Layer 1
l11 = "./l1/1.wav"    # Replace with your high-intensity black sound file path
l12 = "./l1/2.wav" # Replace with your low-intensity black sound file path
# Layer 2
l21 = "./l2/1.wav"
l22 = "./l2/2.wav"

# Set thresholds for detecting intense black regions
BLACK_LIGHT_THRESHOLD = 50     # Threshold for detecting black pixels (lower means darker)
HIGH_BLACK_PIXELS = 10000      # High threshold for black pixel count
LOW_BLACK_PIXELS = 1000        # Low threshold for black pixel count

# Region of interest dimensions (top-left portion of the frame)
ROI_WIDTH = 200    # Adjust width as needed
ROI_HEIGHT = 200   # Adjust height as needed

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

current_sound = None

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Crop the frame to focus only on the top-left region
        roi = frame[:ROI_HEIGHT, :ROI_WIDTH]

        # Convert the region of interest to grayscale to analyze darkness levels
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        # Threshold to create a binary mask of "black" regions
        _, black_mask = cv2.threshold(gray, BLACK_LIGHT_THRESHOLD, 255, cv2.THRESH_BINARY_INV)

        # Count the number of black pixels in the ROI
        black_pixel_count = cv2.countNonZero(black_mask)
        print(f"Black pixel count in ROI: {black_pixel_count}")

        # Play sounds based on intensity of black pixels in the ROI
        if black_pixel_count > HIGH_BLACK_PIXELS:
            if current_sound != "bright":
                mixer.music.load(l11)
                mixer.music.play(-1)  # Loop the bright sound indefinitely
                current_sound = "bright"
                print("High-intensity black detected in ROI, playing bright sound.")
        elif black_pixel_count > LOW_BLACK_PIXELS:
            if current_sound != "contrast":
                mixer.music.load(l12)
                mixer.music.play(-1)  # Loop the contrast sound indefinitely
                current_sound = "contrast"
                print("Low-intensity black detected in ROI, playing contrast sound.")
        else:
            # Stop playing if neither condition is met
            if current_sound:
                mixer.music.stop()
                current_sound = None
                print("No significant black intensity detected in ROI, stopping sound.")

        # Display the original frame and the black mask of the ROI (optional)
        cv2.imshow("Webcam", frame)
        cv2.imshow("Black Mask (ROI)", black_mask)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.1)

finally:
    cap.release()
    cv2.destroyAllWindows()
    mixer.music.stop()
    background_channel_1.stop()  # Stop background sound A
    background_channel_2.stop()  # Stop background sound B