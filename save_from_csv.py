import csv
import requests
import os

def download_images_from_csv(csv_filename, download_folder):
    """
    Download images from URLs stored in a CSV file.

    Parameters:
    - csv_filename: Path to the CSV file containing image URLs.
    - download_folder: Folder where images will be saved.
    """
    
    # Ensure the download folder exists
    if not os.path.exists(download_folder):
        os.makedirs(download_folder)

    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            image_url = row[0]  # Assuming the URL is in the first column
            download_image(image_url, download_folder)

def download_image(image_url, download_folder):
    """
    Download an image from a given URL and save it to a specified folder.

    Parameters:
    - image_url: URL of the image to download.
    - download_folder: Folder where the image will be saved.
    """
    
    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()

        # Extract the filename from the URL
        filename = os.path.join(download_folder, os.path.basename(image_url))
        
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"Downloaded {image_url} to {filename}")

    except requests.RequestException as e:
        print(f"Error downloading {image_url}. Error: {e}")

# Example usage:
if __name__ == "__main__":
    csv_filename = "images.csv"
    download_folder = "downloaded_images"
    download_images_from_csv(csv_filename, download_folder)
