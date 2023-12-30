from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64, os

def generate_cipher_suite(password):
    # Your password
    password = password.encode()

    # Derive a key from the password using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        salt=b'PBKDF2HMAC',  
        iterations=100000,  
        length=32  
    )

    key = base64.urlsafe_b64encode(kdf.derive(password))
    cipher_suite = Fernet(key)
    return cipher_suite

def encrypt_file(file_path, cipher_suite, output_folder):
    try:
        # Read the content of the file
        with open(file_path, 'rb') as file:
            file_data = file.read()

        # Encrypt the file data
        encrypted_data = cipher_suite.encrypt(file_data)

        # Get the filename without the path
        file_name = os.path.basename(file_path)

        # Create the path for the encrypted file in the specified output folder
        encrypted_file_path = os.path.join(output_folder, file_name + '.encrypted')

        # Write the encrypted data to the new file
        with open(encrypted_file_path, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)

        print(f"File encrypted and saved to: {encrypted_file_path}")
        return encrypted_file_path

    except Exception as e:
        print(f"Error: {e}")
        return None

def decrypt_file(encrypted_file_path, cipher_suite, output_folder):
    try:
        # Read the content of the encrypted file
        with open(encrypted_file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()

        # Decrypt the file data
        decrypted_data = cipher_suite.decrypt(encrypted_data)

        # Get the original filename without the '.encrypted' extension
        original_file_name = os.path.splitext(os.path.basename(encrypted_file_path))[0]

        # Create the path for the decrypted file in the specified output folder
        decrypted_file_path = os.path.join(output_folder, original_file_name)

        # Write the decrypted data to the new file
        with open(decrypted_file_path, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)

        print(f"File decrypted and saved to: {decrypted_file_path}")
        return decrypted_file_path

    except Exception as e:
        print(f"Error: {e}")
        return None
