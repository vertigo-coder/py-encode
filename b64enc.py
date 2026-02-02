import base64
import sys
import zlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad, pad
import argparse
import os
import hashlib

def read_raw_binary(file_path):
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File not found at '{file_path}'", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        return None

def compress_bytes(data_bytes):
    try:
        return zlib.compress(data_bytes)
    except Exception as e:
        print(f"An error occurred during compression: {e}", file=sys.stderr)
        return None

def derive_key_from_password(password):
    return hashlib.sha256(password.encode('utf-8')).digest()

def raw_binary_to_base64(raw_binary):
    if raw_binary is None:
        return None
    base64_bytes = base64.b64encode(raw_binary)
    return base64_bytes.decode('utf-8')

def write_base64_to_file(base64_string, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(base64_string)
        return True
    except Exception as e:
        print(f"An error occurred while writing to file: {e}", file=sys.stderr)
        return False

def aes_encrypt(data_bytes, key):
    try:
        iv = os.urandom(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(data_bytes, AES.block_size)
        encrypted_data = cipher.encrypt(padded_data)
        return iv + encrypted_data
    except Exception as e:
        print(f"An error occurred during encryption: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="Path to the file to process")
    parser.add_argument("-e", "--encrypt", help="Encrypt the data")
    parser.add_argument("-o", "--output", help="Output file path")
    args = parser.parse_args()
    
    if args.encrypt:
        key = derive_key_from_password(args.encrypt)
        raw_binary = read_raw_binary(args.file_path)
        compressed_bytes = compress_bytes(raw_binary)
        encrypted_bytes = aes_encrypt(compressed_bytes, key)
        base64_string = raw_binary_to_base64(encrypted_bytes)
        if args.output:
            if write_base64_to_file(base64_string, args.output):
                print(f"Base64 string saved to {args.output}")
            else:
                print("Failed to write to output file")
        else:
            if base64_string:
                print(base64_string)
    else:
        raw_binary = read_raw_binary(args.file_path)
        compressed_bytes = compress_bytes(raw_binary)
        base64_string = raw_binary_to_base64(compressed_bytes)
        if args.output:
            if write_base64_to_file(base64_string, args.output):
                print(f"Base64 string saved to {args.output}")
            else:
                print("Failed to write to output file")
        else:
            if base64_string:
                print(base64_string)