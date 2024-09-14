# Image Downloader Script

This Python script downloads images from a list of URLs provided in a text file and saves them with sequential filenames starting from 51, while keeping the original file extensions.

## Features
- Reads image URLs from a file provided by the user.
- Downloads each image and saves it in the `downloaded_images` folder.
- Automatically names images starting from 51 (e.g., `51.png`, `52.jpg`, etc.).
- Retains the original image file extensions.

## Requirements
- Python 3.x
- `requests` module

## Installation

1. Clone or download this repository to your local machine.
2. Install the required Python package by running:
   ```bash
   pip install requests
   ```

## Usage

1. Place your text file (e.g., `more.txt`) in the same directory as the script. This file should contain one image URL per line.

2. Run the script:
   ```bash
   python script_name.py
   ```

3. When prompted, enter the name of the file containing the image URLs (e.g., `more.txt`).

4. The script will download each image and save it in the `downloaded_images` folder.

## Example File (`more.txt`)

```txt
https://is2.4chan.org/y/1722370635659735.png
https://is2.4chan.org/y/1722778573406161.jpg
```

## Output

The images will be saved in a folder called `downloaded_images` with names like:
```
51.png
52.jpg
```

## License

This project is licensed under the MIT License.
