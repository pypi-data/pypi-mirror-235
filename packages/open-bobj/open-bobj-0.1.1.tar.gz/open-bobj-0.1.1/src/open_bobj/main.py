import os
import sys
import subprocess


def run_blender_with_obj_files(obj_files):
    if len(obj_files) == 0:
        raise ValueError("No files are provided.")

    # Path to Blender executable
    blender_executable = "blender"

    # Create the command to run Blender with the Python script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    blender_script = os.path.join(script_dir, "obj_import.py")
    obj_files_as_str = ";".join(obj_files)
    command = [blender_executable, "-P", blender_script, "--", obj_files_as_str]

    # Run Blender with the script and OBJ files
    subprocess.run(command)


def main():
    if len(sys.argv) < 2:
        raise ValueError("No files are provided.")

    obj_files = sys.argv[1:]
    run_blender_with_obj_files(obj_files)


if __name__ == "__main__":
    main()
