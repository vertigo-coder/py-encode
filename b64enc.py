import base64
import sys
import zlib

def file_to_shellcode(file_path):
    """Reads a file and returns its content as shellcode (bytes)."""
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

def shellcode_to_base64(shellcode):
    """Encodes shellcode bytes to Base64 string."""
    if shellcode is None:
        return None
    base64_bytes = base64.b64encode(shellcode)
    return base64_bytes.decode('utf-8')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python encode.py <file_path>", file=sys.stderr)
        sys.exit(1)
    
    file_path = sys.argv[1]
    shellcode = file_to_shellcode(file_path)
    compressed_bytes = compress_bytes(shellcode)
    base64_string = shellcode_to_base64(compressed_bytes)
    
    if base64_string:
        print(base64_string)