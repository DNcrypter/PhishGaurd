import os
import requests

def get_file_signature(file_path):
    """
    Get the first four bytes of a file and return its signature.

    Parameters:
        file_path (str): The path to the file.

    Returns:
        bytes: The first four bytes of the file or None if an error occurs.
    """
    try:
        with open(file_path, 'rb') as file:
            return file.read(4)
    except Exception as e:
        print(f"Error reading file '{file_path}': {str(e)}")
        return None

def check_file_signature(signature):
    """
    Check the file signature against known file types.

    Parameters:
        signature (bytes): The signature to check.

    Returns:
        str: The detected file type or 'Unknown' if not found.
    """
    # Known file signatures (this should be expanded based on the actual signatures available)
    file_signatures = {
        b'\x89PNG': 'PNG image',
        b'\xff\xd8\xff': 'JPEG image',
        b'GIF8': 'GIF image',
    }