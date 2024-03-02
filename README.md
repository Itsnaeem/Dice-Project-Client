# Dice-Project-Part-1-Client

# Client Application

This repository contains the client application for interacting with the server and receiving files.

## Setup Instructions

1. **Choose an appropriate base image from the Official Images list.**

2. **Create a Dockerfile for the client container with the following specifications:**

    ```Dockerfile
    # Use an appropriate base image
    FROM python:3.9-slim

    # Set working directory
    WORKDIR /app

    # Copy requirements file
    COPY requirements.txt .

    # Install dependencies
    RUN pip install --no-cache-dir -r requirements.txt

    # Copy client application files
    COPY client.py .

    # Command to run the client application
    CMD ["python", "client.py"]
    ```

3. **Use Docker Compose to define and run the client container:**

    ```yaml
    version: '3'

    services:
      client:
        build: ./client
        ports:
          - "5001:5001"
        volumes:
          - clientdata:/app/clientdata
        networks:
          - app-network

    volumes:
      clientdata:
    ```

4. **Write a client application in your preferred language that does the following:**

    ```python
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
    ```

5. **Ensure the server is running and accessible at the specified URL (`http://server:5000`).**

6. **Run the client application by building the Docker container and starting it with Docker Compose.**

