import os
import pandas as pd
import xmltodict
import json
import pyarrow as pa
import pyarrow.parquet as pq
import xml.etree.ElementTree as ET
import gzip
import zipfile
import io

def read_csv(csv_file):
    try:
        df = pd.read_csv(csv_file)
        print(f"Content of CSV file '{csv_file}':\n{df}")
    except Exception as e:
        print(f"Error: {e}")

def read_parquet(parquet_file):
    try:
        table = pq.read_table(parquet_file)
        df = table.to_pandas()
        print(f"Content of Parquet file '{parquet_file}':\n{df}")
    except Exception as e:
        print(f"Error: {e}")

def read_xml(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        data_dict = xmltodict.parse(ET.tostring(root), dict_constructor=dict)
        df = pd.json_normalize(data_dict)
        print(f"Content of XML file '{xml_file}':\n{df}")
    except Exception as e:
        print(f"Error: {e}")

def read_gzip_file(file_path):
    with gzip.open(file_path, 'rt', encoding='latin-1') as file:
        for line in file:
            yield line.strip()

def read_zip_file(file_path):
    # with zipfile.ZipFile(file_path, 'r') as zip_file:
    #     file_info = zip_file.infolist()[0]
    #     with zip_file.open(file_info, 'r') as file:
    #         for line in io.TextIOWrapper(file):
    #             yield line.strip()

    with zipfile.ZipFile(file_path, 'r') as zipf:
            # Get a list of all files in the zip
            file_list = zipf.namelist()
            # Extract and print the contents of each file in the zip
            for file_name in file_list:
                with zipf.open(file_name) as file:
                    content = file.read()
                    print(f"Content of {file_name}:\n{content.decode('utf-8')}")


def main():
    # Ask the user for the action (read, write, convert)
    action = input("Choose an action (read, write, convert): ").lower()

    # Ask the user for the file name
    file_name = input("Enter the file name (include the extension): ")

    # Verify that the file exists
    if action != 'write' and not os.path.exists(file_name):
        print(f"Error: File '{file_name}' not found.")
        return

    if action == 'write':
        # Ask the user for the destination file name
        destination_file = input("Enter the destination file name (include the extension): ")

        if file_name.lower().endswith('.csv'):
            # Perform writing and compression for CSV
            data = pd.DataFrame({"col1": [1, 2, 3], "col2": ['A', 'B', 'C']})
            data.to_csv(destination_file, index=False)
            compress_option = input("Compress to .gz? (y/n): ").lower()
            if compress_option == 'y':
                with open(destination_file, 'rb') as f_in:
                    with gzip.open(destination_file + '.gz', 'wb') as f_out:
                        f_out.writelines(f_in)
                print(f"File '{destination_file}' compressed to '{destination_file}.gz' successfully.")
        elif file_name.lower().endswith('.json'):
            # Perform writing and compression for JSON
            data = pd.DataFrame({"col1": [1, 2, 3], "col2": ['A', 'B', 'C']})
            data.to_json(destination_file, orient='records', lines=True)
            compress_option = input("Compress to .gz or .zip? (gz/zip/n): ").lower()
            if compress_option == 'gz':
                with open(destination_file, 'rb') as f_in:
                    with gzip.open(destination_file + '.gz', 'wb') as f_out:
                        f_out.writelines(f_in)
                print(f"File '{destination_file}' compressed to '{destination_file}.gz' successfully.")
            elif compress_option == 'zip':
                with zipfile.ZipFile(destination_file + '.zip', 'w') as zipf:
                    zipf.write(destination_file, os.path.basename(destination_file))
                print(f"File '{destination_file}' compressed to '{destination_file}.zip' successfully.")
        elif file_name.lower().endswith('.xml'):
            # Perform writing and compression for XML
            data = pd.DataFrame({"col1": [1, 2, 3], "col2": ['A', 'B', 'C']})
            data_dict = data.to_dict(orient='records')
            xml_data = xmltodict.unparse({'root': {'record': data_dict}}, pretty=True)
            with open(destination_file, 'w') as xml_out:
                xml_out.write(xml_data)
            compress_option = input("Compress to .gz or .zip? (gz/zip/n): ").lower()
            if compress_option == 'gz':
                with open(destination_file, 'rb') as f_in:
                    with gzip.open(destination_file + '.gz', 'wb') as f_out:
                        f_out.writelines(f_in)
                print(f"File '{destination_file}' compressed to '{destination_file}.gz' successfully.")
            elif compress_option == 'zip':
                with zipfile.ZipFile(destination_file + '.zip', 'w') as zipf:
                    zipf.write(destination_file, os.path.basename(destination_file))
                print(f"File '{destination_file}' compressed to '{destination_file}.zip' successfully.")
        elif file_name.lower().endswith('.parquet'):
            # Perform writing and compression for Parquet
            data = pd.DataFrame({"col1": [1, 2, 3], "col2": ['A', 'B', 'C']})
            table = pa.Table.from_pandas(data)
            pq.write_table(table, destination_file)
            compress_option = input("Compress to .gz or .zip? (gz/zip/n): ").lower()
            if compress_option == 'gz':
                with open(destination_file, 'rb') as f_in:
                    with gzip.open(destination_file + '.gz', 'wb') as f_out:
                        f_out.writelines(f_in)
                print(f"File '{destination_file}' compressed to '{destination_file}.gz' successfully.")
            elif compress_option == 'zip':
                with zipfile.ZipFile(destination_file + '.zip', 'w') as zipf:
                    zipf.write(destination_file, os.path.basename(destination_file))
                print(f"File '{destination_file}' compressed to '{destination_file}.zip' successfully.")
        else:
            print("Invalid file type for writing.")
    elif action == 'read':
        # Choose the appropriate read function based on file format
        if file_name.lower().endswith('.csv'):
            read_csv(file_name)
        elif file_name.lower().endswith('.parquet'):
            read_parquet(file_name)
        elif file_name.lower().endswith('.xml'):
            read_xml(file_name)
        elif file_name.lower().endswith('.gz'):
            for line in read_gzip_file(file_name):
                print(line)
        elif file_name.lower().endswith('.zip'):
            for line in read_zip_file(file_name):
                print(line)
        else:
            print("Invalid file format for reading.")
    else:
        print("Invalid action. Please choose read, write, or convert.")

if __name__ == "__main__":
    main()
