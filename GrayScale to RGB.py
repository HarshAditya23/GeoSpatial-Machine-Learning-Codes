# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 18:05:40 2024

@author: gaurh
"""

from PIL import Image
import os

def convert_grayscale_to_rgb(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Open the grayscale image
        grayscale_image = Image.open(input_path)

        # Convert grayscale to RGB
        rgb_image = grayscale_image.convert("RGB")

        # Save the RGB image
        rgb_image.save(output_path)

    print("Conversion complete.")

# Example usage:
input_folder = r""
output_folder = r""
convert_grayscale_to_rgb(input_folder, output_folder)