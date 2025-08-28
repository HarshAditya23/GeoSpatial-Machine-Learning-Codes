# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 13:03:41 2024

@author: gaurh
"""

import rasterio
from rasterio.mask import mask
import geopandas as gpd
from shapely.geometry import mapping
from scipy import ndimage

#Path to the input raster image and shapefile
raster_path = r''
shapefile_path = r''

# Load the shapefile using geopandas
gdf = gpd.read_file(shapefile_path)

# Open the raster image using rasterio
with rasterio.open(raster_path) as src:
    for index, row in gdf.iterrows():
        # Get the geometry of the polygon
        geom = row['geometry']
        
        # Convert the geometry to a GeoJSON-like dictionary
        geojson_geom = mapping(geom)
        
        # Read the raster data within the polygon extent
        out_image, out_transform = mask(src, [geojson_geom], crop=True)
        
        # Apply nearest neighbor resampling to the clipped raster data
        out_image_resampled = ndimage.zoom(out_image, zoom=(1, 1, 1), order=0)
        
        # Update the metadata
        out_meta = src.meta.copy()
        out_meta.update({
            "driver": "GTiff",
            "height": out_image_resampled.shape[1],
            "width": out_image_resampled.shape[2],
            "transform": out_transform
        })
        
        # Get the name from the attribute of the shapefile
        field_name = row['Name']
        
        # Define the output path for the clipped image using the name
        output_path = f'/{field_name}.tif'
        # Save the clipped image
        with rasterio.open(output_path, "w", **out_meta) as dest:
            dest.write(out_image_resampled)
        
        print(f"Clipped image for polygon {index} saved to {output_path}")

print("Clipping complete.")