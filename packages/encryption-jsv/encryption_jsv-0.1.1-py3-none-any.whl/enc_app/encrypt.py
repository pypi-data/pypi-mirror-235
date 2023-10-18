import argparse
from cryptography.fernet import Fernet


# Function to encrypt a file
def encrypt_file(file_path, key, output_file): 
    try:
        with open(file_path, "rb") as file:
            data = file.read()
        
        cipher_suite = Fernet(key)
        encrypted_data = cipher_suite.encrypt(data)

        with open(output_file, "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)

        print(f"File '{file_path}' encrypted and saved as '{output_file}'")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    
    parser = argparse.ArgumentParser(description="File Encryption Tool")
    parser.add_argument("--file", required=True, help="Path to the file you want to encrypt")
    parser.add_argument("--algorithm", required=True, choices=["AES", "DES"], help="Encryption algorithm (AES or DES)")
    parser.add_argument("--key", required=True, help="Secret key for encryption")
   

    args = parser.parse_args()

    file_path = args.file
    algorithm = args.algorithm
    key = args.key.encode()
    output_file = f"{file_path}.enc"

    try:
        encrypt_file(file_path, key, output_file)
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

