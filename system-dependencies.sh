#!/bin/bash
apt-get update && apt-get install -y \
    x11-apps \
    libx11-6 \
    libxext6 \
    libxrender1 \
    fontconfig \
    libfreetype6-dev \
    libsdl2-ttf-2.0-0 \
    fonts-dejavu \
    && rm -rf /var/lib/apt/lists/*