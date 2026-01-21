import base64
import sys
import zlib

def read_raw_binary(file_path):
    """Reads a file and returns its content as raw_binary (bytes)."""
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
    """Compresses bytes using zlib."""
    if data_bytes is None:
        return None
    try:
        return zlib.compress(data_bytes)
    except Exception as e:
        print(f"An error occurred during compression: {e}", file=sys.stderr)
        return None

def raw_binary_to_base64(raw_binary):
    """Encodes raw_binary bytes to Base64 string."""
    if raw_binary is None:
        return None
    base64_bytes = base64.b64encode(raw_binary)
    return base64_bytes.decode('utf-8')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python encode.py <file_path>", file=sys.stderr)
        sys.exit(1)
    
    file_path = sys.argv[1]
    raw_binary = read_raw_binary(file_path)
    compressed_bytes = compress_bytes(raw_binary)
    base64_string = raw_binary_to_base64(compressed_bytes)
    
    if base64_string:
        print(base64_string)
