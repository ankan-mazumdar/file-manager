import zipfile

mode = 'w'
# Ask the user to input the file path
file_path = input("Enter the file path: ")

with open(file_path, "w") as file:
    file.write("This is a Big Data Project content.")

with open(file_path, "r") as file:
    print(file.read())

# Zipping the file
zip_file_path = file_path + ".zip"
zipfile.ZipFile(zip_file_path, mode='w').write(file_path)
print(f'The file has been zipped and saved as {zip_file_path}')    