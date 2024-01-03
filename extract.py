import rasterio

# Open the GeoTIFF file
file_path = '/Users/nayandas/Downloads/42S_20170101-20180101.tif'
with rasterio.open(file_path) as src:
    # metadata = src.meta
    # print("Metadata:", metadata)

    band1 = src.read(1)  # Replace 1 with the desired band number
    print("Band 1 data:", band1)
    

