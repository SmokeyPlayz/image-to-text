# Image to Text Converter
This is a Python script that converts text from images to readable text and sends the converted text to Discord through a webhook. The script utilizes the Tesseract-OCR library for Optical Character Recognition (OCR) and integrates with the Discord API for notifications.

# How It Works
The script captures an image from your clipboard.
It then applies OCR using Tesseract to extract text from the image.
If text is successfully extracted, it is copied to your clipboard and sent to a designated Discord channel through a webhook.
The script runs continuously, checking for images in your clipboard at regular intervals.
# Prerequisites
Python 3.x installed
A Discord webhook URL for sending messages to a channel
# Setup and Configuration
Clone this repository or download the script (main.py).
Install the required Python libraries by running pip install -r requirements.txt.
# Installing and Configuring Tesseract-OCR
Tesseract-OCR is required for text extraction. Follow these steps to install and configure it:
Download the Tesseract installer from the official repository: https://github.com/UB-Mannheim/tesseract/wiki
Run the installer and note down the installation path. The path is usually something like C:\Program Files\Tesseract-OCR.
Add Tesseract to your system's PATH:
Search for "Environment Variables" in the Start menu and click on "Edit the system environment variables."
In the System Properties window, click the "Environment Variables" button.
In the "System Variables" section, find and select the "Path" variable, then click the "Edit" button.
Click the "New" button and add the path to the Tesseract installation directory (e.g., C:\Program Files\Tesseract-OCR).
Click "OK" to save your changes.
# Configuring Discord Webhook
Create a new webhook in your Discord server/channel by following these steps:
Go to the channel where you want the notifications to appear.
Click on the gear icon next to the channel name to open the Channel Settings.
Click on "Integrations" in the left sidebar.
Click "Create Webhook" and follow the prompts to set up the webhook.
Copy the webhook URL.
Update the tyd.json configuration file with your Tesseract path and the Discord webhook URL.

Run the script using python main.py.

# Troubleshooting
If you encounter errors related to Tesseract-OCR not being found, make sure the Tesseract path in tyd.json is correct.
If you experience issues with the Discord webhook, verify that the webhook URL is correct and accessible.
# Known Issues
The accuracy of text extraction may vary depending on the quality and size of the image.
The script may not work as expected on all systems due to differences in clipboard handling.
# Disclaimer
This script is provided as-is and may not work flawlessly in all scenarios. Use it at your own risk.
# now i do know another way i think u can download it is just by opening this? maybe you gotta join the discord(https://discord.gg/xolo) then use
 https://discord.com/channels/1038575674899841044/1107046001061142681/1145075194818474074

