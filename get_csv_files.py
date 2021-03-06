# Author:  Alexan Mardigian

import io
import requests
import zipfile

ZIP_URL = "http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip"

# This function will fetch a zip file, containing .csv files, from a given url.
# If no list of .csv files were passed into the fuction, then all the files in the
# zip file will be extracted.  Errors will be printed to standard output if:
# - The user specified files that do not exist in the zip file.
# - The user provided an invalid url.
# - The user was trying to unzip a file that is not a .zip file.
# - An HTTP error was returned from the HTTP request.
def get_zipped_csv_files(url=ZIP_URL, csv_files=[], extract_path=None):
    try:
        response    = requests.get(url)
        zipped_csvs = zipfile.ZipFile(io.BytesIO(response.content))

        # If no csv_files were specified (empty csv_files),
        # then extract all files in the zip file.  Otherwise,
        # extract each file listed in csv_files.
        if not csv_files: 
            zipped_csvs.extractall(path=extract_path)
        else:
            for csv_file in csv_files:
                try:
                    zipped_csvs.extract(csv_file, path=extract_path)
                except KeyError:
                    print("\nget_zipped_csv_files() failed.  File " + csv_file + " not found in  zip file.")
                
    except requests.HTTPError as e:
        print("\nget_zipped_csv_files() failed with HTTP Error " + e.code)
    except requests.exceptions.MissingSchema:
        print("\nget_zipped_csv_files() failed.  Invalid URL " + url)
    except zipfile.BadZipFile:
        print("\nget_zipped_csv_files() failed.  File is not a zip file.")
