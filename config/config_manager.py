import json
import os

def load_config(config_file: str):
    """Loads the configuration file."""
    if not os.path.exists(config_file):
        print(f"Configuration file '{config_file}' not found. Creating default config.")
        return create_default_config()

    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error reading configuration file: {e}")
        return None

def create_default_config():
    """Creates a default configuration if the config file is missing or corrupted."""
    default_config = {
        "templates": {
            "default": {
                "output_dir": "downloads",
                "quality": "best",
                "format": "mp4",
                "download_subs": False
            }
        }
    }
    return default_config
