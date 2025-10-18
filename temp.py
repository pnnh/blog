import os
import shutil
import sys

def process_directory(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename == 'index.md':
                # Full path to the original file
                original_file = os.path.join(dirpath, filename)
                
                # Get the parent directory name
                parent_dir_name = os.path.basename(dirpath)
                
                # Remove '.note' suffix if present
                if parent_dir_name.endswith('.note'):
                    parent_dir_name = parent_dir_name[:-5]  # Remove last 5 characters: '.note'
                
                # New filename: parent_dir_name + '.md'
                new_filename = parent_dir_name + '.md'
                
                # Full path to the renamed file in the same directory
                renamed_file = os.path.join(dirpath, new_filename)
                
                # Rename the file
                os.rename(original_file, renamed_file)
                
                # Copy the renamed file to the parent of the parent directory (same level as parent_dir)
                grandparent_dir = os.path.dirname(dirpath)
                copy_destination = os.path.join(grandparent_dir, new_filename)
                
                # Copy the file
                shutil.copy(renamed_file, copy_destination)
                
                print(f"Processed: {original_file} -> {renamed_file} and copied to {copy_destination}")

if __name__ == "__main__":
    root_directory = 'docs'  # Change this to your target root directory
    if not os.path.isdir(root_directory):
        print(f"Error: {root_directory} is not a valid directory.")
        sys.exit(1)
    
    process_directory(root_directory)