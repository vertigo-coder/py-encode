import base64
import zlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import hashlib

def derive_key_from_password(password):
    return hashlib.sha256(password.encode('utf-8')).digest()

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def aes_decrypt(encrypted_data, key):
    if encrypted_data is None:
        return None
    try:
        iv = encrypted_data[:16]
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(encrypted_data[16:])
        return unpad(decrypted_data, AES.block_size)
    except Exception as e:
        print(f"An error occurred during decryption: {e}")
        return None

def decompress_bytes(data_bytes):
    if data_bytes is None:
        return None
    try:
        return zlib.decompress(data_bytes)
    except Exception as e:
        print(f"An error occurred during decompression: {e}")
        return None

def write_binary_to_file(binary_data, file_path):
    if binary_data is None:
        return False
    try:
        with open(file_path, 'wb') as file:
            file.write(binary_data)
        return True
    except Exception as e:
        print(f"An error occurred while writing to file: {e}")
        return False

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="Path to the text file containing the base64 string")
    parser.add_argument("output_file", help="Path to save the decoded file")
    parser.add_argument("-p", "--password", help="Password for decryption")
    args = parser.parse_args()
    
    base64_string = read_text_file(args.input_file)

    if args.password:
        encrypted_data = base64.b64decode(base64_string)
        key = derive_key_from_password(args.password)
        decrypted_data = aes_decrypt(encrypted_data, key)
        decompressed_data = decompress_bytes(decrypted_data)
    else:
        compressed_data = base64.b64decode(base64_string)
        decompressed_data = decompress_bytes(compressed_data)
    
    if write_binary_to_file(decompressed_data, args.output_file):
        print(f"File successfully saved to {args.output_file}")
    else:
        exit(1)