import json

class ConfigLoader:
    """Loads the configuration from a JSON file."""
    @staticmethod
    def load_config(config_path):
        with open(config_path) as f:
            return json.load(f)
