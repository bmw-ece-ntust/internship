# Use an official Ubuntu image as a base
FROM ubuntu:20.04

# Set the environment variables to prevent interactive prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    cmake \
    make \
    gcc \
    g++ \
    pkg-config \
    libfftw3-dev \
    libmbedtls-dev \
    libsctp-dev \
    libyaml-cpp-dev \
    libgtest-dev \
    libzmq3-dev \
    git \
    curl \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Clone the srsRAN_Project repository
RUN git clone https://github.com/srsran/srsRAN_Project.git /opt/srsRAN_Project

# Build srsRAN
RUN cd /opt/srsRAN_Project && \
    mkdir build && \
    cd build && \
    cmake ../ -DENABLE_EXPORT=ON -DENABLE_ZEROMQ=ON && \
    make -j$(nproc)

# Set the working directory to /apps/cu
WORKDIR /apps/cu

# Copy the built srscu binary to /usr/bin
RUN cp /opt/srsRAN_Project/build/apps/cu/srscu /usr/bin/srscu

# Define the command to run the srscu with the specified configuration file
CMD ["srscu", "-c", "cu.yml"]