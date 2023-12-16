import zipfile
import io

def zip_file(file_path):
    with open(file_path, 'rb') as file:
        # Read the content of the file
        file_content = file.read()

    # Create a BytesIO object to store the compressed data
    zip_buffer = io.BytesIO()

    # Create a ZipFile object and write the file content to it
    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        zip_file.writestr(file_path, file_content)

    # Get the binary data of the compressed file
    zip_data = zip_buffer.getvalue()

    return zip_data