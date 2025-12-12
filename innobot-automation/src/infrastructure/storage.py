import os

class Storage:
    """
    File handling utilities for the project.
    """
    @staticmethod
    def ensure_dir(path: str):
        """
        Ensure output directory exists.
        Creates folder if missing.
        """
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def save_pdf(file_path: str, data: bytes):
        """
         Save raw PDF bytes to a specified file path.
        """
        with open(file_path, "wb") as f:
            f.write(data)
