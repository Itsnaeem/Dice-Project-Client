import os
import requests
import hashlib

SERVER_URL = "http://server:5000"  # Updated to use the service name in Docker Compose

def download_file(url, destination):
    response = requests.get(url)
    with open(destination, 'wb') as file:
        file.write(response.content)

def calculate_checksum(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        return hashlib.sha256(data).hexdigest()

def main():
    client_data_path = "/app/clientfile.txt"  # Adjusted destination file path
    download_file(f"{SERVER_URL}/get_file", client_data_path)
    checksum = calculate_checksum(client_data_path)
    print(f"Client: File downloaded at {client_data_path}")
    print(f"Client: Checksum: {checksum}")

if __name__ == "__main__":
    if not os.path.exists('/app/clientdata'):
        os.makedirs('/app/clientdata')
    os.chdir('/app/clientdata')  # Change working directory to '/app/clientdata'
    main()
