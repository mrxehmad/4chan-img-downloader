import os
import requests

# Read the file containing the image URLs
with open('more.txt', 'r') as file:
    urls = file.readlines()

# Start naming images from 51
start_index = 108

# Create a directory to save the downloaded images
os.makedirs('downloaded_images', exist_ok=True)

# Download each image
for i, url in enumerate(urls, start=start_index):
    url = url.strip()
    if url:
        try:
            # Get the image extension from the URL
            extension = os.path.splitext(url)[-1]
            # Create the filename
            filename = f"downloaded_images/{i}{extension}"
            # Download the image
            response = requests.get(url)
            response.raise_for_status()  # Check if the download was successful
            # Save the image
            with open(filename, 'wb') as image_file:
                image_file.write(response.content)
            print(f"Downloaded {filename}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {url}: {e}")
