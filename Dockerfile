# Use an official Python runtime as a parent image
FROM python:3.9

# Install dependencies for pygame font and image loading
RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg-dev \
    libpng-dev \
    python3-dev \
    xorg-dev \
    libfontconfig1 \
    fontconfig \
    libxrender1 \
    libx11-6 \
    && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the requirements.txt file into the container at /usr/src/app
COPY requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container at /usr/src/app
COPY . .

# Make sure to copy the images directory into the container
COPY images/ images/

# Run main.py when the container launches
CMD ["python", "./main.py"]
