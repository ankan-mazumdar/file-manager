import pandas as pd

def read_parquet(file_path):
    df = pd.read_parquet(file_path)
    return df

#user to input the file path
file_path = input("Enter the path of the Parquet file: ")

# Call the read_parquet function with the user-input file path
data_frame = read_parquet(file_path)

# Display the DataFrame
print(data_frame)
