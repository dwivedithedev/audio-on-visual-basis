import cv2
import pygame
import time
from regions import regions 

pygame.mixer.init()

# Set the total number of channels
total_channels = len(regions) + 2  # One per region + two for background
pygame.mixer.set_num_channels(total_channels)

# Load background sounds & loop indefinitely on separate channels
background_sound_1 = pygame.mixer.Sound("./louder/BGM/layer_A_alter.wav")
background_sound_1.set_volume(0.9)  # Volume between 0.0 and 1.0
background_sound_2 = pygame.mixer.Sound("./louder/BGM/layer_B_alter.wav")
background_sound_2.set_volume(0.9)

# Reserve channels for background sounds
background_channel_1 = pygame.mixer.Channel(total_channels - 2)
background_channel_2 = pygame.mixer.Channel(total_channels - 1)

# Play background sounds
background_channel_1.play(background_sound_1, loops=-1)
background_channel_2.play(background_sound_2, loops=-1)

# Threshold for detecting black pixels
BLACK_LIGHT_THRESHOLD = 50  # Adjust as needed for your lighting conditions

# Initialize a separate channel for each region
region_channels = {}
region_sounds = {}
current_sounds = {region["name"]: None for region in regions}

for i, region in enumerate(regions):
    try:
        region_channels[region["name"]] = pygame.mixer.Channel(i)
        region_sounds[region["name"]] = {
            "zero": pygame.mixer.Sound(region["zero"]),
            "first": pygame.mixer.Sound(region["first"]),
            "second": pygame.mixer.Sound(region["second"]),
            "third": pygame.mixer.Sound(region["third"]),
            "fourth": pygame.mixer.Sound(region["fourth"]),
        }
    except KeyError as e:
        print(f"Missing key {e} in region: {region['name']}")
        exit()

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
            x_start = region["x_start"]
            y_start = region["y_start"]
            width = region["width"]
            height = region["height"]

            # Validate region coordinates
            if x_start < 0 or y_start < 0 or x_start + width > frame.shape[1] or y_start + height > frame.shape[0]:
                print(f"Skipping region {region['name']} due to invalid coordinates.")
                continue

            # Crop and convert the region to grayscale
            roi = frame[y_start:y_start + height, x_start:x_start + width]
            gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

            # Create a binary mask of "black" regions
            _, black_mask = cv2.threshold(gray, BLACK_LIGHT_THRESHOLD, 255, cv2.THRESH_BINARY_INV)
            black_pixel_count = cv2.countNonZero(black_mask)
            print(f"Black pixel count in {region['name']} ROI: {black_pixel_count}")

            # Determine which sound to play based on black pixel intensity
            sound_key = None
            if black_pixel_count > region["very_high_threshold"]:
                sound_key = "fourth"
            elif black_pixel_count > region["high_threshold"]:
                sound_key = "third"
            elif black_pixel_count > region["mid_threshold"]:
                sound_key = "second"
            elif black_pixel_count > region["low_threshold"]:
                sound_key = "first"
            elif black_pixel_count > region["very_low_threshold"]:
                sound_key = "zero"

            # Retrieve the channel and sound for the region
            channel = region_channels[region["name"]]
            current_sound = current_sounds[region["name"]]

            # Play the appropriate sound if it's not already playing
            if sound_key and current_sound != sound_key:
                sound = region_sounds[region["name"]][sound_key]
                channel.play(sound, loops=-1)
                channel.set_volume(min(max(region["volume"], 0.0), 1.0))  # Clamp volume
                current_sounds[region["name"]] = sound_key
                print(f"{sound_key.capitalize()}-intensity black detected in {region['name']}, playing '{sound_key}' sound.")

            # Stop playing if no significant black intensity is detected
            elif not sound_key and current_sound:
                channel.stop()
                current_sounds[region["name"]] = None
                print(f"No significant black intensity in {region['name']}, stopping sound.")

            # Optional: Display each region's mask
            cv2.imshow(f"Black Mask ({region['name']})", black_mask)

        # Display the original frame
        cv2.imshow("Webcam", frame)

        # Exit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
    pygame.mixer.quit()  # Stops all channels and sounds safely