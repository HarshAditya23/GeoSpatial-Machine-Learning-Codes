# -*- coding: utf-8 -*-
"""
Created on Tue Jul  1 22:28:19 2025

@author: BharatRohan
"""

from PIL import Image
Image.MAX_IMAGE_PIXELS = None
import numpy as np

def clip_tiff_image(image_path, chunk_size=1024, output_dir="chunks"):
    # Open the TIFF image using Pillow
    with Image.open(image_path) as img:
        # Get the size of the image
        img_width, img_height = img.size
        
        print(f"Image size: {img_width}x{img_height}")
        
        # Convert the image to a numpy array for easier chunking
        img_array = np.array(img)

        # Calculate the number of chunks based on the specified chunk size
        num_chunks_width = (img_width // chunk_size) + (1 if img_width % chunk_size != 0 else 0)
        num_chunks_height = (img_height // chunk_size) + (1 if img_height % chunk_size != 0 else 0)

        # Loop through each chunk and save them as individual images
        chunk_index = 0
        for i in range(num_chunks_height):
            for j in range(num_chunks_width):
                # Calculate chunk coordinates
                left = j * chunk_size
                upper = i * chunk_size
                right = min(left + chunk_size, img_width)
                lower = min(upper + chunk_size, img_height)

                # Crop the chunk from the image
                chunk = img.crop((left, upper, right, lower))

                # Save the chunk to the output directory
                chunk_filename = f"{output_dir}/chunk_{chunk_index}.tiff"
                chunk.save(chunk_filename)
                print(f"Saved: {chunk_filename}")
                
                chunk_index += 1

if __name__ == "__main__":
    image_path = "file.tif"  # Replace with your image path
    clip_tiff_image(image_path)
