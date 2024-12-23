import os

def create_directory(output_dir: str):
    """Ensures the output directory exists."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
