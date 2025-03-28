import os
import socket

def is_production():
    """Check if we're running on the production server by hostname"""
    return 'agenticstudio.co' in socket.gethostname()

# Set base path depending on environment
BASE_PATH = '/100DoC/day1-band' if is_production() else ''
STATIC_PATH = f'{BASE_PATH}/static'

# For debugging
if __name__ == '__main__':
    print(f"Running in {'production' if is_production() else 'development'} mode")
    print(f"BASE_PATH: {BASE_PATH}")
    print(f"STATIC_PATH: {STATIC_PATH}") 