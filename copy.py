import os
import shutil

def copy_html_files(source_dir, target_dir):
    """
    Copies all .html files from the source directory and its subdirectories
    to the target directory, preserving the original directory structure.
    Creates the target directory if it does not exist.
    
    Parameters:
    source_dir (str): The path to the source directory.
    target_dir (str): The path to the target directory.
    """
    # Create the target directory if it does not exist
    os.makedirs(target_dir, exist_ok=True)
    
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.html'):
                # Calculate the relative path from the source directory
                rel_path = os.path.relpath(root, source_dir)
                # Construct the target subdirectory path
                target_root = os.path.join(target_dir, rel_path)
                # Create the target subdirectory if it does not exist
                os.makedirs(target_root, exist_ok=True)
                # Copy the file to the target location
                source_file = os.path.join(root, file)
                target_file = os.path.join(target_root, file)
                shutil.copy(source_file, target_file)

# Example usage:
copy_html_files('docs', 'blog')