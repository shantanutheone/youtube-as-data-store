import os
def empty_folder(folder_path):
    try:
        # Get a list of all files in the folder
        files = os.listdir(folder_path)

        # Iterate over the files and remove each one
        for file_name in files:
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Removed: {file_path}")

        print(f"The folder '{folder_path}' is now empty.")
    except Exception as e:
        print(f"Error: {e}")

import csv
def append_row_to_csv(file_path, row_data):
    try:
        with open(file_path, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(row_data)
        print(f"Row appended successfully to {file_path}")
    except Exception as e:
        print(f"Error: {e}")

def add_to_db(folder, file_name, yt_video_name, video_url, password):
    path = folder + "/" + file_name
    append_row_to_csv("data/database/info.csv", [path, yt_video_name, video_url, password])

import hashlib

def generate_md5(input_string):
    # Create an MD5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the input string encoded as bytes
    md5_hash.update(input_string.encode('utf-8'))

    # Get the hexadecimal representation of the hash
    md5_hex = md5_hash.hexdigest()

    return md5_hex