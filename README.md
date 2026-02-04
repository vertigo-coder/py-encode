# b64enc
a python utility for encoding, compressing, and encrypting files into Base64 strings.
## Features
*   AES-256-CBC Encryption
*   Zlib Compression
## Requirements
```bash
pip install pycryptodome
```
## Usage
**Encrypt a file:**
```bash
python3 -m b64enc <input_file> -e <password> -o <output_file>
```
**Compress and encode a file (no encryption):**
```bash
python3 -m b64enc <input_file> -o <output_file>
```
**Decompress and decrypt a file:**
```bash
python3 -m decrypt <input_file> <output_file> -p <password>
```
**Decompress a file (no encryption):**
```bash
python3 -m decrypt <input_file> <output_file> 
```

