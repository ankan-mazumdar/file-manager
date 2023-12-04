import os
import pandas as pd
import xmltodict
import json
import pyarrow.parquet as pq
import xml.etree.ElementTree as ET

def convert_csv_to_xlsx(csv_file, xlsx_file):
    try:
        df = pd.read_csv(csv_file)
        df.to_excel(xlsx_file, index=False)
        print(f"CSV file '{csv_file}' converted to XLSX file '{xlsx_file}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

def convert_json_to_xlsx(json_file, xlsx_file):
    try:
        df = pd.read_json(json_file, lines=True)
        df.to_excel(xlsx_file, index=False)
        print(f"JSON file '{json_file}' converted to XLSX file '{xlsx_file}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

def convert_xml_to_xlsx(xml_file, xlsx_file):
    try:
        with open(xml_file, 'r') as xml_data:
            data_dict = xmltodict.parse(xml_data.read())
            df = pd.json_normalize(data_dict)

        xlsx_dir = os.path.dirname(xlsx_file)
        if not os.path.exists(xlsx_dir):
            os.makedirs(xlsx_dir)

        df.to_excel(xlsx_file, index=False)
        print(f"XML file '{xml_file}' converted to XLSX file '{xlsx_file}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

def convert_parquet_to_xlsx(parquet_file, xlsx_file):
    try:
        table = pq.read_table(parquet_file)
        df = table.to_pandas()
        df.to_excel(xlsx_file, index=False)
        print(f"Parquet file '{parquet_file}' converted to XLSX file '{xlsx_file}' successfully.")
    except Exception as e:
        print(f"Error: {e}")

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

def read_xlsx(xlsx_file):
    try:
        df = pd.read_excel(xlsx_file)
        print(f"Content of XLSX file '{xlsx_file}':\n{df}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Ask the user for the file name
    file_name = input("Enter the file name (include the extension): ")

    # Verify that the file exists
    if not os.path.exists(file_name):
        print(f"Error: File '{file_name}' not found.")
        return

    # Ask the user for the action (read, write, or convert)
    action = input("Choose an action (read, write, convert): ").lower()

    if action == 'read':
        # Choose the appropriate read function based on file format
        if file_name.lower().endswith('.csv'):
            read_csv(file_name)
        elif file_name.lower().endswith('.parquet'):
            read_parquet(file_name)
        elif file_name.lower().endswith('.xml'):
            read_xml(file_name)
        elif file_name.lower().endswith('.xlsx'):  
            read_xlsx(file_name)    
        else:
            print("Invalid file format for reading.")
    elif action == 'write':
        # Generate a default XLSX file name
        xlsx_file = os.path.splitext(file_name)[0] + ".xlsx"

        # Ask the user for the XLSX file name (optional, press Enter to use the default)
        xlsx_file = input(f"Enter the XLSX file name (press Enter to use '{xlsx_file}'): ") or xlsx_file

        # Convert the file to XLSX
        convert_csv_to_xlsx(file_name, xlsx_file)

        # Read and display the content of the XLSX file
        read_xlsx(xlsx_file)
    elif action == 'convert':
        # Ask the user for the destination file name
        destination_file = input("Enter the destination file name (include the extension): ")

        if file_name.lower().endswith('.csv'):
            convert_csv_to_xlsx(file_name, destination_file)
        elif file_name.lower().endswith('.json'):
            convert_json_to_xlsx(file_name, destination_file)
        elif file_name.lower().endswith('.xml'):
            convert_xml_to_xlsx(file_name, destination_file)
        elif file_name.lower().endswith('.parquet'):
            convert_parquet_to_xlsx(file_name, destination_file)
        else:
            print("Invalid file type for conversion.")
    else:
        print("Invalid action. Please choose read, write, or convert.")

if __name__ == "__main__":
    main()
