#Documentation-
The original code has only file_manager.py, I have added the following python scripts to address issues and added new operations
file_converter.py
file_copy_move_rm.py
file_parquet_reader.py
file_reader.py
file_writer.py
file_xlsx.py
gz_zip_reader.py



#Testing Results:
Under Testing results, the following open issues in GitHub are resolved-

StopIteration Exception while reading a JSON or Parquet file

This has been handled by adding an exception, which will print ‘End of the file reached’ at EOF.
Here is the link to the code- https://github.com/ankan-mazumdar/file-manager/blob/Bg-Data/file_manager/file_reader.py








Parquet read file failed due to unknown encoding

For handling the encoding-decoding failure error, I initially tried setting the encoding standard value as 'utf-8' , 'Latin-1' etc., however, none of them fixed the issue. Finally, it was a simple pandas read_parquet function that helped here. Please find the code link-
https://github.com/ankan-mazumdar/file-manager/blob/Bg-Data/file_manager/file_parquet_reader.py

Please find the test results screenshots-






The gzip file read operation Error: Raised OSError on reading a gzip file due to an invalid argument (Invalid characters in the file path).

The error occurs as the encoding can't recognize the characters, on researching, I found that it is Latin-1 characters rather than utf-8, hence I kept encoding ='Latin-1' in the solution code that worked perfectly. Here's the link to the code-
https://github.com/ankan-mazumdar/file-manager/blob/Bg-Data/file_manager/gz_zip_reader.py
Below is the testing result-


Next, as proposed I have added the functionality for read-write operations for xlsx and zip files-












Converter- This script can do all-round file format conversion from csv to xml, json and  parquet. Parquet to csv json xml and further in this fashion. Code link-
https://github.com/ankan-mazumdar/file-manager/blob/Bg-Data/file_manager/file_converter.py

Testing results- 
Csv to Parquet conversion-




Json to parquet -




Parquet to Json- 



Copy move, create remove operations- As name suggests this script basically can copy , move, make, and remove files from any mentioned path. Here is the code link-
https://github.com/ankan-mazumdar/file-manager/blob/Bg-Data/file_manager/file_copy_move_rm.py








Uploaded the scripts over EMR cluster and tested using python and Spark-.
Csv file -



Json file-



Parquet file reading-



Xlsx file-


Compressed file-


8. Using Spark-submit command-
Issue -Spark-submit to run Python script gets stuck and never proceeds when there is user interaction/inputs are required at run time


https://stackoverflow.com/questions/40910869/python-script-hangs-on-input-method-when-running-spark. 

When we submit an application using spark-submit, we don't interact with Python code, but with Java one, which doesn't expect any input from stdin.
If we want to make it work we have to skip spark-submit and execute this as a Python script.
We could alternatively achieve this by using pyspark or hardcode the filename in the script

9. Read the file using Pyspark


10. Writing parquet file and zipping it-


The file is created -



11.Xlsx file in spark

