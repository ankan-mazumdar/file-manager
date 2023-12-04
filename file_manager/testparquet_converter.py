import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq  # Import the parquet submodule
import os

# Create a sample dataset
data = {
    "name": ["Alice", "Bob", "Charlie"],
    "age": [30, 25, 22]
}

df = pd.DataFrame(data)

# Save the dataset to CSV
csv_file_path = "sample_data.csv"
df.to_csv(csv_file_path, index=False)

# Read the CSV file using pandas
df_csv = pd.read_csv(csv_file_path)

# Convert the DataFrame to Parquet
table = pa.Table.from_pandas(df_csv)
parquet_file_path = "small_parquet_file.parquet"

# Use the write_table function from the parquet submodule
pq.write_table(table, parquet_file_path)

# Verify the Parquet file size
file_size = os.path.getsize(parquet_file_path)
print("Parquet file size:", file_size, "bytes")
