# Use the NVIDIA CUDA 11.2 base image with cuDNN 8.1 support
FROM nvidia/cuda:11.2.2-cudnn8-runtime-ubuntu20.04

# Set environment variables to avoid any installation prompts
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary dependencies and Python packages
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    python3-venv \
    build-essential \
    libcupti-dev \
    wget && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip3 install --upgrade pip

# Install TensorFlow 2.10
RUN pip3 install tensorflow==2.10

# Set the working directory inside the container
WORKDIR /workspace

# Start the container with bash as default
CMD ["/bin/bash"]
