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
