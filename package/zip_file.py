import zipfile
import os

# Path to your zip file
zip_path = r'D:\Git file\MDS\application\project.zip'

# Directory to extract to
extract_to = r'D:\Git file\MDS\application'

# Make sure the target directory exists
os.makedirs(extract_to, exist_ok=True)

# Unzip the file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print(f'Files extracted to: {extract_to}')
