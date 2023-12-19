import zipfile
import binascii
from utils.encryption import *

def file_to_zip(input_file_path, output_zip_path):
    with zipfile.ZipFile(output_zip_path, 'w') as zip_file:
        zip_file.write(input_file_path)

def zip_to_binary_format(zip_file_path):
    # Read the binary content of the zipped file
    with open(zip_file_path, 'rb') as zipped_file:
        binary_content = zipped_file.read()

    # Convert binary content to "01010101" format
    binary_string = ''.join(format(byte, '08b') for byte in binary_content)

    return binary_string


def convert_binary_to_zip(binary_content, output_zip_path):
    # Convert binary string to bytes
    bytes_data = bytearray(int(binary_content[i:i+8], 2) for i in range(0, len(binary_content), 8))

    # Write the bytes to a zip file
    with open(output_zip_path, 'wb') as zip_file:
        zip_file.write(bytes_data)

def convert_file_to_binary(file_path, password):
    file_name = file_path.split("/")[-1].split(".")[0]
    zip_file_path = f"data/zipped_files/{file_name}.zip"
    file_to_zip(file_path, zip_file_path)
    #TODO: Create Encrypted ZIP File and Return it's binary
    # encrypted_zip_file_path = f"data/zipped_files/{file_name}_encrypted.zip"
    # encrypt_zip(zip_file_path, encrypted_zip_file_path, password)
    binary_string = zip_to_binary_format(zip_file_path)
    return binary_string

def unzip(zip_file_path, output_folder):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(output_folder)