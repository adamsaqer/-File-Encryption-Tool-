# File Encryption Tool 🔐

## Overview
This project is a **Basic File Encryption Tool** that allows users to **encrypt and decrypt files** securely using **AES-256 encryption**.

## Features
- 🔒 **AES-256 encryption** for strong security.
- 🛑 **Password-based encryption** (only the correct password can decrypt files).
- 🖥️ **Command-line interface (CLI)** for easy usage.
- 📂 **Works with any file type** (documents, images, videos, etc.).

## Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/file-encryption-tool.git
cd file-encryption-tool
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Usage
#### **Encrypt a File**
```bash
python file_encryption_tool.py
```
- Choose `E` when prompted.
- Enter the **file path** and **password**.
- The encrypted file will be saved as `filename.enc`.

#### **Decrypt a File**
```bash
python file_encryption_tool.py
```
- Choose `D` when prompted.
- Enter the **encrypted file path** and **password**.
- The decrypted file will be saved as `filename_decrypted`.

## File Structure
```
📂 file-encryption-tool/
├── file_encryption_tool.py  # Main script
├── requirements.txt         # Dependencies
├── README.md                # Documentation
```

## License
This project is licensed under the **MIT License**.
