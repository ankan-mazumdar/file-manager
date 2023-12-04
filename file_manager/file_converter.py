import xmltodict
import json
import csv
import pandas as pd
import os

def convert_csv_to_xlsx(csv_file, xlsx_file):
    df = pd.read_csv(csv_file)
    df.to_excel(xlsx_file, index=False)
    print(f"CSV file '{csv_file}' converted to XLSX file '{xlsx_file}' successfully.")

def convert_csv_to_parquet(csv_file, parquet_file):
    df = pd.read_csv(csv_file)
    df.to_parquet(parquet_file, index=False)
    print(f"CSV file '{csv_file}' converted to Parquet file '{parquet_file}' successfully.")

def convert_xml_to_json(xml_file, json_file):
    with open(xml_file, 'r') as xml:
        data_dict = xmltodict.parse(xml.read())
        json_data = json.dumps(data_dict, indent=2)
        with open(json_file, 'w') as json_out:
            json_out.write(json_data)
    print(f"XML file '{xml_file}' converted to JSON file '{json_file}' successfully.")

def convert_xml_to_csv(xml_file, csv_file):
    with open(xml_file, 'r') as xml:
        data_dict = xmltodict.parse(xml.read())
        df = pd.json_normalize(data_dict)
        df.to_csv(csv_file, index=False)
    print(f"XML file '{xml_file}' converted to CSV file '{csv_file}' successfully.")

def convert_xml_to_parquet(xml_file, parquet_file):
    with open(xml_file, 'r') as xml:
        data_dict = xmltodict.parse(xml.read())
        df = pd.json_normalize(data_dict)
        df.to_parquet(parquet_file, index=False)
    print(f"XML file '{xml_file}' converted to Parquet file '{parquet_file}' successfully.")

def convert_json_to_xml(json_file, xml_file):
    with open(json_file, 'r') as json_in:
        data_dict = json.load(json_in)
        xml_data = xmltodict.unparse(data_dict, pretty=True)
        with open(xml_file, 'w') as xml_out:
            xml_out.write(xml_data)
    print(f"JSON file '{json_file}' converted to XML file '{xml_file}' successfully.")

def convert_json_to_csv(json_file, csv_file):
    df = pd.read_json(json_file, lines=True)
    df.to_csv(csv_file, index=False)
    print(f"JSON file '{json_file}' converted to CSV file '{csv_file}' successfully.")

def convert_json_to_parquet(json_file, parquet_file):
    df = pd.read_json(json_file, lines=True)
    df.to_parquet(parquet_file, index=False)
    print(f"JSON file '{json_file}' converted to Parquet file '{parquet_file}' successfully.")

def convert_parquet_to_csv(parquet_file, csv_file):
    df = pd.read_parquet(parquet_file)
    df.to_csv(csv_file, index=False)
    print(f"Parquet file '{parquet_file}' converted to CSV file '{csv_file}' successfully.")

def convert_parquet_to_xml(parquet_file, xml_file):
    df = pd.read_parquet(parquet_file)
    json_data = df.to_json(orient='records', lines=True)
    data_dict = json.loads(json_data)
    xml_data = xmltodict.unparse({'root': {'record': data_dict}}, pretty=True)
    with open(xml_file, 'w') as xml_out:
        xml_out.write(xml_data)
    print(f"Parquet file '{parquet_file}' converted to XML file '{xml_file}' successfully.")

def convert_parquet_to_json(parquet_file, json_file):
    df = pd.read_parquet(parquet_file)
    json_data = df.to_json(orient='records', lines=True)
    with open(json_file, 'w') as json_out:
        json_out.write(json_data)
    print(f"Parquet file '{parquet_file}' converted to JSON file '{json_file}' successfully.")

def main():
    # Ask the user for the file path
    source_file = input("Enter the source file path: ")

    # Determine the file type based on the extension
    _, file_extension = os.path.splitext(source_file)
    file_extension = file_extension.lower()

    if file_extension == '.csv':
        # Ask the user for the destination file path for CSV to Parquet conversion
        destination_file = input("Enter the destination Parquet file path: ")

        # Additional option for CSV to XLSX conversion
        convert_to_xlsx = input("Do you want to convert to XLSX? (y/n): ").lower()
        if convert_to_xlsx == 'y':
            xlsx_destination_file = input("Enter the destination XLSX file path: ")
            convert_csv_to_xlsx(source_file, xlsx_destination_file)
        else:                                   
            convert_csv_to_parquet(source_file, destination_file)
    elif file_extension == '.xml':
        # Ask the user for the destination file path for XML to Parquet conversion
        destination_file = input("Enter the destination Parquet file path: ")

        convert_xml_to_parquet(source_file, destination_file)
    elif file_extension == '.json':
        # Ask the user for the destination file path for JSON to Parquet conversion
        destination_file = input("Enter the destination Parquet file path: ")

        convert_json_to_parquet(source_file, destination_file)
    elif file_extension == '.parquet':
        # Ask the user for the destination file path and conversion type for Parquet to CSV, XML, or JSON conversion
        destination_file = input("Enter the destination file path: ")
        conversion_type = input("Choose conversion type (parquet_to_csv, parquet_to_xml, parquet_to_json): ").lower()

        if conversion_type == 'parquet_to_csv':
            convert_parquet_to_csv(source_file, destination_file)
        elif conversion_type == 'parquet_to_xml':
            convert_parquet_to_xml(source_file, destination_file)
        elif conversion_type == 'parquet_to_json':
            convert_parquet_to_json(source_file, destination_file)
        else:
            print("Invalid conversion type. Please choose parquet_to_csv, parquet_to_xml, or parquet_to_json.")
    else:
        print("Invalid file type. Please provide a CSV, XML, JSON, or Parquet file.")

if __name__ == "__main__":
    main()
