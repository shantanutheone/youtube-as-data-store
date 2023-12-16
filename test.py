from utils.zip import *
# Example usage
file_path = 'data/sample.js' 
zip_file_path = "data/sample.zip"
file_to_zip(file_path, zip_file_path)
result = zip_to_binary_format(zip_file_path)


convert_binary_to_zip(result, "data/sample_back.zip")
unzip("data/sample_back.zip", "extracted_files/")