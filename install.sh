#!/bin/bash

# Fix SSL certificates on macOS
/Applications/Python\ 3.12/Install\ Certificates.command

# Install the package in editable mode with pip
pip install -e .

# Ensure dependencies are installed
pip install python-editor pyperclip

echo "Installation complete."
