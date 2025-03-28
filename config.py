import os

def is_production():
    """Check if we're running in production using FLASK_ENV environment variable"""
    return os.environ.get('FLASK_ENV') == 'production'

# Set base path depending on environment
BASE_PATH = '/100DoC/day1-band' if is_production() else ''
STATIC_PATH = f'{BASE_PATH}/static'

# For debugging
if __name__ == '__main__':
    print(f"Running in {'production' if is_production() else 'development'} mode")
    print(f"BASE_PATH: {BASE_PATH}")
    print(f"STATIC_PATH: {STATIC_PATH}") 