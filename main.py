import os
import requests

# Get the input file name from the user
input_file = input("Enter the name of the file containing image URLs (e.g., more.txt): ")

# Check if the file exists
if not os.path.isfile(input_file):
    print(f"File '{input_file}' not found!")
    exit()

# Read the file containing the image URLs
with open(input_file, 'r') as file:
    urls = file.readlines()

# Start naming images from 51
start_index = 51

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
