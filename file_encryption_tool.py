from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
import os

def generate_key(password):
    """Generate a 256-bit AES key from the given password."""
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()

def encrypt_file(file_path, password):
    """Encrypt a file using AES encryption."""
    key = generate_key(password)
    iv = Random.new().read(AES.block_size)  # 16-byte IV
    cipher = AES.new(key, AES.MODE_CFB, iv)
    
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    encrypted_data = iv + cipher.encrypt(file_data)
    
    with open(file_path + ".enc", 'wb') as f:
        f.write(encrypted_data)
    
    print(f"File encrypted successfully: {file_path}.enc")

def decrypt_file(file_path, password):
    """Decrypt a previously encrypted file."""
    key = generate_key(password)
    
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    iv = file_data[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    decrypted_data = cipher.decrypt(file_data[AES.block_size:])
    
    decrypted_file_path = file_path.replace(".enc", "_decrypted")
    with open(decrypted_file_path, 'wb') as f:
        f.write(decrypted_data)
    
    print(f"File decrypted successfully: {decrypted_file_path}")

def main():
    """Command-line interface for encryption and decryption."""
    choice = input("Enter 'E' to encrypt or 'D' to decrypt: ").strip().upper()
    file_path = input("Enter file path: ").strip()
    password = input("Enter encryption password: ")
    
    if not os.path.exists(file_path):
        print("Error: File not found!")
        return
    
    if choice == 'E':
        encrypt_file(file_path, password)
    elif choice == 'D':
        decrypt_file(file_path, password)
    else:
        print("Invalid choice! Please enter 'E' or 'D'.")

if __name__ == "__main__":
    main()
