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
            logger.info(f"for tag '{tag}': File copied from '{source}' copied to '{destination}'")
            
        except Exception as e:
            logger.error(f"for tag '{tag}: Failed to copy {source} to {destination}: {e}")
        try:
            # Rename the copied file
            return DirectoryManager.rename_copied_file(destination, logger)
        except Exception as e:
            logger.error(f"for tag '{tag} in {destination}: Failed to rename: {e}")

            
    @staticmethod
    def rename_copied_file(destination, logger):
        try:
            # Get the folder path
            folder_path = destination
            
            # Find the file that starts with "1 - Checklist" in the destination folder
            checklist_file = None
            for file in os.listdir(folder_path):
                if "checklist" in file.lower():
                    checklist_file = file
                    break

            pcform_file = file
            for file in os.listdir(folder_path):
                if "pcform" in file.lower():
                    pcform_file = file
                    break            

            if checklist_file is None:
                raise FileNotFoundError("Checklist file not found in the destination folder.")
            if pcform_file is None:
                raise FileNotFoundError("pcform file not found in the destination folder.")

            # Create the new file name by replacing "Checklist" with "PCForm"
            new_file_name = checklist_file.replace("1 - Checklist", "2 - PCForm")
            new_file_name = new_file_name.replace("1 - checklist", "2 - PCForm")

            file_extension = os.path.splitext(destination)[1]
            
            # Define the new file path
            new_file_path = os.path.join(folder_path, new_file_name)
            pcform_file_path=os.path.join(folder_path, pcform_file)
            # Rename the copied file
            os.rename(pcform_file_path, new_file_path)
            logger.info(f"File renamed to '{new_file_name}'")
            return new_file_path
            
        except Exception as e:
            logger.error(f"Failed to rename file {destination}: {e}")


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
