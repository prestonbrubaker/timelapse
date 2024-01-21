from picamera2 import Picamera2
import time
import os
import RPi.GPIO as GPIO

switch_pin = 11
led_pin = 12

time.sleep(5)

GPIO.setmode(GPIO.BOARD)      # use PHYSICAL GPIO Numbering
GPIO.setup(ledPin, GPIO.OUT)   # set ledPin to OUTPUT mode
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)    # set buttonPin to PULL UP INPUT mode

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
    switch_closed = True
    
    while True:
        # Update interval time
        int_time += 5

        if GPIO.input(switch_pin)==GPIO.LOW: # if button is pressed
            #GPIO.output(led_pin,GPIO.HIGH)   # turn on led
            print ('switch closed >>>')     # print information on terminal
            switch_closed =  True
        else : # if button is relessed
            #GPIO.output(led_pin,GPIO.LOW) # turn off led 
            print ('switch open <<<')   
            switch_closed = False

        
        # Check if 60 seconds have passed
        if(int_time - ref_time >= 60 and switch_closed == False):
            # Generate a unique filename based on current time
            filename = f"photos/captured_image_{int(time.time())}.png"

            # Capture and save the image in the 'photos' subfolder
            camera.capture_file(filename)

            # Print a message indicating the file has been saved
            print(f"Photo captured and saved as {filename}")

            # Subtract 60 seconds from interval time
            int_time -= 60
            GPIO.output(led_pin,GPIO.HIGH)   # turn on led
            time.sleep(1)
            GPIO.output(led_pin,GPIO.LOW) # turn off led 
            

        # Wait for 5 seconds before checking again
        time.sleep(5)

    # Stop the camera
    camera.stop()

if __name__ == "__main__":
    capture_photo()
