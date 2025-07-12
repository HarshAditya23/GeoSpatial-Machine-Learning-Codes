# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 16:45:56 2025

@author: gaurh
"""

import json
import os

def replace_tiff_with_png_in_json_files(folder_path):
    # List all files in the folder
    json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]
    
    # Loop through each JSON file
    for json_file in json_files:
        json_file_path = os.path.join(folder_path, json_file)
        
        # Read the content of the JSON file
        try:
            with open(json_file_path, 'r') as file:
                data = json.load(file)
            
            # Get the list of image paths (assuming the JSON has the "images" key)
            image_paths = data.get("images", [])
            
            # Replace .tiff extension with .png
            updated_image_paths = []
            for path in image_paths:
                if path.endswith(".tiff") or path.endswith(".tif"):
                    updated_image_paths.append(path.rsplit(".", 1)[0] + ".png")
                else:
                    updated_image_paths.append(path)
            
            # Update the JSON data with the new image paths
            data["images"] = updated_image_paths
            
            # Save the updated JSON file
            with open(json_file_path, 'w') as file:
                json.dump(data, file, indent=4)
            
            print(f"Updated {json_file} with .png extensions.")
        
        except Exception as e:
            print(f"Error processing {json_file}: {e}")

# Example Usage:
folder_path = "chunks"  # Folder containing the 13 JSON files
replace_tiff_with_png_in_json_files(folder_path)