import cv2
from pygame import mixer
import time
from regions import regions  # Import regions from the separate Python file

mixer.init()

# Load background sounds & loop indefinitely
background_sound_1 = mixer.Sound("./bgm/A.wav")  # First background sound file path
mixer.Sound("./bgm/A.wav").set_volume(0.4)
background_sound_2 = mixer.Sound("./bgm/B.wav")  # Second background sound file path
mixer.Sound("./bgm/B.wav").set_volume(0.8)
background_channel_1 = background_sound_1.play(-1)  
background_channel_2 = background_sound_2.play(-1) 

# Threshold for detecting black pixels
BLACK_LIGHT_THRESHOLD = 50  # Adjust as needed for your lighting conditions

# Dictionary to track the current sound playing for each region
current_sounds = {region["name"]: None for region in regions}

# Initialize webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Process each region
        for region in regions:
            # Determine the region's coordinates
            x_start = region["x_start"]
            y_start = region["y_start"]
            width = region["width"]
            height = region["height"]

            # Crop and convert the region to grayscale
            if x_start >= 0:
                roi = frame[y_start:y_start + height, x_start:x_start + width]
            else:
                roi = frame[y_start:y_start + height, x_start:]

            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

            # Create a binary mask of "black" regions
            _, black_mask = cv2.threshold(gray, BLACK_LIGHT_THRESHOLD, 255, cv2.THRESH_BINARY_INV)
            black_pixel_count = cv2.countNonZero(black_mask)
            print(f"Black pixel count in {region['name']} ROI: {black_pixel_count}")

            # Determine which sound to play based on black pixel intensity
            if black_pixel_count > region["high_threshold"]:
                if current_sounds[region["name"]] != "high":
                    mixer.music.load(region["high_sound"])
                    mixer.music.set_volume(region["volume"])  # Set the volume for high sound
                    mixer.music.play(-1)  # Loop the high-intensity sound
                    current_sounds[region["name"]] = "high"
                    print(f"High-intensity black detected in {region['name']}, playing high sound.")
            elif black_pixel_count > region["low_threshold"]:
                if current_sounds[region["name"]] != "low":
                    mixer.music.load(region["low_sound"])
                    mixer.music.set_volume(region["volume"])  # Set the volume for high sound
                    mixer.music.play(-1)  # Loop the low-intensity sound
                    current_sounds[region["name"]] = "low"
                    print(f"Low-intensity black detected in {region['name']}, playing low sound.")
            else:
                # Stop playing if neither condition is met
                if current_sounds[region["name"]]:
                    mixer.music.stop()
                    current_sounds[region["name"]] = None
                    print(f"No significant black intensity in {region['name']}, stopping sound.")

            # Optional: Display each region's mask
            cv2.imshow(f"Black Mask ({region['name']})", black_mask)

        # Display the original frame
        cv2.imshow("Webcam", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.1)

finally:
    cap.release()
    cv2.destroyAllWindows()
    mixer.music.stop()
    background_channel_1.stop()
    background_channel_2.stop()
