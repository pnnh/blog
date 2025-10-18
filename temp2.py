import os

def rename_subdirs(root_dir):
    # Walk through the directory tree recursively
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # We use topdown=False to rename from the deepest directories first,
        # avoiding issues with renaming parent directories before children.
        
        # Iterate over the subdirectories in the current dirpath
        for dirname in dirnames:
            # Check if the directory name ends with '.chan'
            if dirname.endswith('.chan'):
                # Construct the full old path
                old_path = os.path.join(dirpath, dirname)
                
                # New name: remove the '.chan' suffix
                new_name = dirname[:-5]  # Remove the last 5 characters ('.chan')
                new_path = os.path.join(dirpath, new_name)
                
                # Rename the directory
                try:
                    os.rename(old_path, new_path)
                    print(f"Renamed '{old_path}' to '{new_path}'")
                except OSError as e:
                    print(f"Error renaming '{old_path}': {e}")

# Example usage: replace 'your_root_directory' with the actual path
if __name__ == "__main__":
    root_directory = 'docs'  # Specify your root directory here
    rename_subdirs(root_directory)