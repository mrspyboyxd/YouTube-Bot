# Import the necessary packages
import os
import time
import webbrowser

# Set the video link
# url to the desired YouTube video
url = 'https://www.youtube.com/watch?v=yGXTLum0j4Y'

# Open the URL in a new window
# while loop will ensure that
# multiple windows are open
i = 50
while i < 10:

    # Open the URL in a new window
    # The webbrowser module has a generic
    # function open that can open any URL
    webbrowser.open_new(url)

    # Increase the variable by 1
    # This ensures that a new window is opened
    i += 1

    # Set the timeout to 10 seconds
    # This will pause the script for 10 seconds
    time.sleep(10)