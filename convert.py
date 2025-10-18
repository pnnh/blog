import os
import subprocess
import tempfile

def create_lua_filter():
    """
    Creates a temporary Lua filter to rewrite .md links to .html in relative hyperlinks.
    Based on Pandoc's Lua filter examples for Link elements.
    """
    lua_script = """
function Link(el)
  if el.target:match("%.md$") and not el.target:match("^https?://") and not el.target:match("^mailto:") then
    el.target = el.target:gsub("%.md$", ".html")
  end
  return el
end
"""
    # Create a temporary file for the Lua script
    with tempfile.NamedTemporaryFile(mode='w', suffix='.lua', delete=False) as temp_file:
        temp_file.write(lua_script)
        return temp_file.name

def convert_md_to_html(directory):
    """
    Traverses the given directory, finds all .md files, and converts them to HTML using Pandoc.
    Applies a Lua filter to preserve/adjust internal relative links.
    """
    lua_filter_path = create_lua_filter()
    try:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.md'):
                    input_path = os.path.join(root, file)
                    output_path = os.path.join(root, file[:-3] + '.html')  # Replace .md with .html
                    file_name_without_ext = os.path.splitext(file)[0]  # Extract base name without .md
                    # Call Pandoc with Lua filter
                    cmd = [
                        'pandoc',
                        input_path,
                        '-o', output_path,
                        '--lua-filter', lua_filter_path,
                        '--standalone',  # Optional: Generates a complete HTML file with <head> and <body>
                        '--metadata', f'title={file_name_without_ext}'  # Set title to file name
                    ]
                    try:
                        subprocess.run(cmd, check=True) 
                        print(f"Successfully converted: {input_path} -> {output_path} with title '{file_name_without_ext}'")
                    except subprocess.CalledProcessError as e:
                        print(f"Error converting {input_path}: {e}")
    finally:
        # Clean up the temporary Lua file
        os.unlink(lua_filter_path)

# Example usage: Replace 'path_to_directory' with your actual folder path
if __name__ == "__main__":
    path_to_directory = 'docs'  # e.g., '/Users/yourname/documents/markdown_files'
    convert_md_to_html(path_to_directory)