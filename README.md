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
python b64enc.py <input_file> -e <password> -o <output_file>
```
**Compress and encode a file (no encryption):**
```bash
python b64enc.py <input_file> -o <output_file>
```
