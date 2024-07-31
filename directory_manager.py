import os
import shutil
from datetime import datetime

class DirectoryManager:
    """Manages directory creation and file operations."""
    
    @staticmethod
    def create_output_directory():
        date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_dir = os.path.join(os.getcwd(), date_str)
        os.makedirs(output_dir, exist_ok=True)
        return output_dir

    @staticmethod
    def copy_file_to_directory(source, destination, logger, tag):
        try:
            shutil.copy(source, destination)
            source_last_dir = os.path.basename(os.path.dirname(source))
            destination_last_dir = os.path.basename(os.path.dirname(destination))
            logger.info(f"for tag '{tag}': File from '{source_last_dir}' copied to '{destination_last_dir}'")
        except Exception as e:
            logger.error(f"Failed to copy {source} to {destination}: {e}")

    @staticmethod
    def move_folder(source_folder, destination_root, logger, tag):
        destination_folder = os.path.join(destination_root, os.path.basename(source_folder))
        try:
            shutil.move(source_folder, destination_folder)
            source_last_dir = os.path.basename(source_folder)
            destination_last_dir = os.path.basename(destination_folder)
            logger.info(f"for tag '{tag}': Moved folder '{source_last_dir}' to '{destination_last_dir}' ")
        except Exception as e:
            logger.error(f"Failed to move folder {source_folder} to {destination_folder}: {e}")
