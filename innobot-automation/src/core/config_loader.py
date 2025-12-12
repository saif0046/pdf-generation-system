import json

class ConfigLoader:
    """
    Loads configuration values from a JSON file.
    Used to load project settings such as output folder,
    placeholder strategies, template paths, and counts.
    """

    @staticmethod
    def load(path: str):
        with open(path, "r") as f:
            return json.load(f)
