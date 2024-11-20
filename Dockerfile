FROM python:3.10-slim

# Install necessary system dependencies including libgl1
RUN apt-get update && apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    libgl1 && \
    apt-get clean

# Copy application code into the container
COPY . /app
WORKDIR /app

# Upgrade pip and install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Specify the default command to run your application
CMD ["python", "app.py"]
