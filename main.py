# Import necessary libraries
import pytesseract
from PIL import ImageGrab
import clipboard
import json
import os
import requests
import logging
import time

# Function to set up logging configuration
def setup_logging(log_file):
    # Configure logging settings
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

# Function to load configuration from JSON file
def load_config(config_file):
    # Default configuration settings
    default_config = {
        "tesseract": {
            "path": "C:/Program Files/Tesseract-OCR"
        },
        "discord": {
            "webhook_url": "webhook here"
        }
    }
    try:
        # Load configuration from file
        with open(config_file, 'r') as f:
            config = json.load(f)
            return {**default_config, **config}
    except FileNotFoundError:
        logging.error("Config file not found. Using default settings.")
        return default_config
    except json.JSONDecodeError:
        logging.error("Error decoding JSON in the config file.")
        return default_config

# Function to convert screenshot to text and send to Discord
def screenshot_to_text(config):
    try:
        # Capture screenshot from clipboard
        screenshot = ImageGrab.grabclipboard()

        if screenshot is None:
            logging.warning("No image found in clipboard.")
            return

        # Perform OCR on the screenshot to extract text
        extracted_text = pytesseract.image_to_string(screenshot, config=config['tesseract']['path'])

        if extracted_text:
            # Copy extracted text to clipboard
            clipboard.copy(extracted_text)
            logging.info("Image content:\n" + extracted_text)
            logging.info("Text extracted from image and copied to clipboard.")

            webhook_url = config['discord']['webhook_url']
            if webhook_url.startswith("https://discord.com/api/webhooks/"):
                # Prepare payload for Discord webhook
                payload = {
                    "content": f"Successfully converted image to text:\n\n{extracted_text}\n\nMade by DH_heister"
                }
                # Send message to Discord webhook
                response = requests.post(webhook_url, json=payload)
                if response.status_code == 204:
                    logging.info("Message sent to Discord webhook.")
                else:
                    logging.error("Failed to send message to Discord webhook.")
            else:
                logging.error("Invalid Discord webhook URL format.")
        else:
            logging.warning("No text could be extracted from the image.")
    except pytesseract.TesseractNotFoundError:
        logging.error("Tesseract not found. Please check the path in the configuration.")
    except Exception as e:
        logging.error("An error occurred:", exc_info=True)

# Entry point of the script
if __name__ == "__main__":
    # Configuration file paths
    config_file = "tyd.json"
    log_file = "log.txt"

    # Set up logging
    setup_logging(log_file)
    
    # Load configuration settings
    config = load_config(config_file)
    
    # Check Tesseract OCR path and Discord webhook URL
    if not os.path.exists(config['tesseract']['path']):
        logging.error("Tesseract not found at the specified path.")
    elif not config['discord']['webhook_url'].startswith("https://discord.com/api/webhooks/"):
        logging.error("Invalid Discord webhook URL format in the configuration.")
    else:
        # Continuously perform screenshot to text conversion
        while True:
            # Perform screenshot to text conversion
            converted_text = screenshot_to_text(config)
            
            # Print converted text in the console
            if converted_text:
                print("Successfully converted image to text:")
                print(converted_text)
            
            time.sleep(1)  # Wait for 1 seconds before checking again
