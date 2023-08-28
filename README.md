# Image to Text Converter
This is a Python script that converts text from images to readable text and sends the converted text to Discord through a webhook. The script utilizes the Tesseract-OCR library for Optical Character Recognition (OCR) and integrates with the Discord API for notifications.

# How It Works
The script captures an image from your clipboard.
It then applies OCR using Tesseract to extract text from the image.
If text is successfully extracted, it is copied to your clipboard and sent to a designated Discord channel through a webhook.
The script runs continuously, checking for images in your clipboard at regular intervals.
# Prerequisites
Python 3.x installed
Tesseract-OCR installed (refer to the installation guide for your system)
A Discord webhook URL for sending messages to a channel
# Setup and Configuration
Clone this repository or download the script (main.py).
Install the required Python libraries by running pip install -r requirements.txt.
Update the tyd.json configuration file with your Tesseract path and Discord webhook URL.
Run the script using python main.py.
# Troubleshooting
If you encounter errors related to Tesseract-OCR not being found, make sure the Tesseract path in tyd.json is correct.
If you experience issues with the Discord webhook, verify that the webhook URL is correct and accessible.
# Known Issues
The accuracy of text extraction may vary depending on the quality and size of the image.
The script may not work as expected on all systems due to differences in clipboard handling.
# Disclaimer
This script is provided as-is and may not work flawlessly in all scenarios. Use it at your own risk.
