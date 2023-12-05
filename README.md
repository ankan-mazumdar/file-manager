#Documentaton and Testng Link- 

https://docs.google.com/document/d/1WNZ-ROChD1NpbkMS6eDWjHIeXL7Jd8IumljB-sj3-HQ/edit

Documentation-
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

1.[StopIteration Exception while reading a JSON or Parquet file](https://github.com/deepaknairrpf/file-manager/issues#:~:text=Issues%20list-,StopIteration%20Exception%20while%20reading%20a%20JSON%20or%20Parquet%20file,-%239%20opened%202)

This has been handled by adding an exception, which will print ‘End of the file reached’ at EOF.
Here is the link to the code- https://github.com/ankan-mazumdar/file-manager/blob/Bg-Data/file_manager/file_reader.py

![image](https://github.com/ankan-mazumdar/file-manager/assets/69012134/b2288d07-f48c-4161-88dd-e62d11eb3075)

![image](https://github.com/ankan-mazumdar/file-manager/assets/69012134/4ae3e9f4-5abd-43c4-8334-f797019ed29a)


2. Parquet read file failed due to unknown encoding[(https://github.com/deepaknairrpf/file-manager/issues/8)](https://github.com/deepaknairrpf/file-manager/issues#:~:text=2-,Parquet%20read%20file%20failed%20due%20to%20unknown%20encoding,-%238%20opened%202)

For handling the encoding-decoding failure error, I initially tried setting the encoding standard value as 'utf-8' , 'Latin-1' etc., however, none of them fixed the issue. Finally, it was a simple pandas read_parquet function that helped here. Please find the code link-
https://github.com/ankan-mazumdar/file-manager/blob/Bg-Data/file_manager/file_parquet_reader.py

Please find the test results screenshots-

![image](https://github.com/ankan-mazumdar/file-manager/assets/69012134/a2aece8e-5f4c-496a-8ef9-76f888b657fd)

![image](https://github.com/ankan-mazumdar/file-manager/assets/69012134/8ed93fed-7930-4ae3-a0a1-3e2f4cc56a0a)

![image](https://github.com/ankan-mazumdar/file-manager/assets/69012134/31b8f6dc-995e-40b3-a374-dd4f58dcbe3b)


3.The gzip file read operation Error: Raised OSError on reading a gzip file due to an invalid argument (Invalid characters in the file path).
  https://github.com/deepaknairrpf/file-manager/issues/7
  
The error occurs as the encoding can't recognize the characters, on researching, I found that it is Latin-1 characters rather than utf-8, hence I kept encoding ='Latin-1' in the solution code that worked perfectly. Here's the link to the code-
https://github.com/ankan-mazumdar/file-manager/blob/Bg-Data/file_manager/gz_zip_reader.py
Below is the testing result-

![image](https://github.com/ankan-mazumdar/file-manager/assets/69012134/fca6bf09-6d1c-4b2c-adb2-3cb3c8790783)


4. Next, as proposed I have added the functionality for read-write operations for xlsx and zip files-

![image](https://github.com/ankan-mazumdar/file-manager/assets/69012134/f061e788-be69-4e13-84a1-ab64090f0c04)

![image](https://github.com/ankan-mazumdar/file-manager/assets/69012134/3f446517-631c-4d0f-9274-b4ea44055426)


5. Converter- This script can do all-round file format conversion from csv to xml, json and  parquet. Parquet to csv json xml and further in this fashion. Code link-
https://github.com/ankan-mazumdar/file-manager/blob/Bg-Data/file_manager/file_converter.py

Testing results- 
![image](https://github.com/ankan-mazumdar/file-manager/assets/69012134/159386f7-efab-4f34-ab59-56f69a4a7b7b)


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

