from picamera2 import Picamera2
import time
import os

time.sleep(5)

def capture_photo():
    # Create a Picamera2 instance
    camera = Picamera2()

    # Configure the camera
    camera_config = camera.create_preview_configuration()
    camera.configure(camera_config)

    # Start the camera
    camera.start()

    # Create a 'photos' subfolder if it doesn't exist
    if not os.path.exists('photos'):
        os.makedirs('photos')

    # Initialize reference time and interval time
    ref_time = time.time()
    int_time = ref_time

    while True:
        # Update interval time
        int_time += 5

        # Check if 60 seconds have passed
        if int_time - ref_time >= 60:
            # Generate a unique filename based on current time
            filename = f"photos/captured_image_{int(time.time())}.png"

            # Capture and save the image in the 'photos' subfolder
            camera.capture_file(filename)

            # Print a message indicating the file has been saved
            print(f"Photo captured and saved as {filename}")

            # Subtract 60 seconds from interval time
            int_time -= 60

        # Wait for 5 seconds before checking again
        time.sleep(5)

    # Stop the camera
    camera.stop()

if __name__ == "__main__":
    capture_photo()
