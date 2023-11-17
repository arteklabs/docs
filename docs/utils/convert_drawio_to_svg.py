"""Convert a draw.io file into a svg file.

The convertion requires the installation of the draw.io CLI, which is perhaps not a valid production
dependency. The diagrams will be committed as svg files, althought this is not ideal. Draw.io could
be perhaps a CICD dependency.
"""
import glob
import os
import subprocess

# Get the current working directory
current_dir = os.getcwd()

# Get the parent directory
parent_dir = os.path.dirname(current_dir)
source = os.path.join(parent_dir, "sphinx/src")
target = os.path.join(parent_dir, "sphinx/static/img")


def get_drawio_files():
    file_pattern = "*.drawio"

    file_paths = []
    # Iterate over all files and directories in the given directory
    for root, _, _ in os.walk(source):
        # Use glob to find files that match the pattern
        matching_files = glob.glob(os.path.join(root, file_pattern))
        # Append matching file paths to the list
        file_paths.extend(matching_files)

    return file_paths


def get_file_name(path):
    return os.path.basename(path).split(".")[0] + ".svg"


files = get_drawio_files()
for drawio_file in files:
    file_name = get_file_name(drawio_file)
    file_path = os.path.join(target, file_name)
    cmd = f"draw -x -f svg -o {file_path} {drawio_file}"

    subprocess.run(cmd, shell=True, executable="/bin/bash")
