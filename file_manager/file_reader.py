# Import necessary modules and classes
from file_manager import FileManager
from gz_zip_reader import read_gzip_file, read_zip_file

import os
import pandas as pd

mode = 'r'
# Ask the user to input the file path
file_path = input("Enter the file path: ")
# Check if the file has a .gz extension
if file_path.lower().endswith('.gz'):
    # If the file is a gzip file, use the read_gzip_file function
    file_iterator = read_gzip_file(file_path)
elif file_path.lower().endswith('.zip'):
    # If the file is a zip file, use the read_zip_file function
    file_iterator = read_zip_file(file_path)

else:
    # If not, use FileManager to handle regular file reading
    with FileManager(file_path, mode=mode) as file_io:
        if mode == 'r':
            # Read the file
            file_iterator = file_io.read()
            try:
                for row in file_iterator:
                    print(row)
            except StopIteration:
                print("End of file reached.")
                pass

 