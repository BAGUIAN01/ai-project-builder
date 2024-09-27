


import sys
import os
import subprocess
import venv
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import current_config


def create_virtual_environment(base_path):
    """
    The function creates a virtual environment, 
    upgrades pip, and logs the process.
    """
    logging.warning("Starting virtual environment creation")
    venv_path = os.path.join(base_path, current_config.VENV_DIRECTORY)

    venv.EnvBuilder(with_pip=True).create(venv_path)
    logging.warning(f"Virtual environment created at {venv_path}")

    python_executable = os.path.join(
        venv_path, "Scripts" if os.name == "nt" else "bin",
        current_config.PYTHON_EXECUTABLE)

    subprocess.call(
        [python_executable, "-m", "pip", "install", "--upgrade", "pip"])

    logging.warning("Pip has been upgraded.")

    with open(os.path.join(base_path, 'requirements.txt'), 'w') as req_file:
        subprocess.call(
            [python_executable, "-m", "pip", "freeze"],
            stdout=req_file
        )
    logging.warning("requirements.txt has been created.")

    activate_script = os.path.join(venv_path, "Scripts", "activate") \
        if os.name == "nt" else os.path.join(venv_path, "bin", "activate")

    logging.warning(
        "To activate the virtual environment, run the following command:\n"
        f"  {activate_script} (Windows)"
    )


def create_directory_structure(base_path):
    """
    The function creates a specific directory structure for a project.
    """
    base_path = os.path.join(os.getcwd(), "test")
    structure = {
        "data": ["original", "processed"],
        "notebooks": [],
        "src": [],
        "saved_models": []
    }

    for folder in structure.keys():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

    for data_folder in structure["data"]:
        data_folder_path = os.path.join(base_path, "data")
        folder_path = os.path.join(data_folder_path, data_folder)
        os.makedirs(folder_path, exist_ok=True)

    src_path = os.path.join(base_path, "src")
    open(os.path.join(src_path, "model.py"), 'w').close()
    open(os.path.join(src_path, "data_processing.py"), 'w').close()
    open(os.path.join(src_path, "feature_engineering.py"), 'w').close()
    open(os.path.join(src_path, "utils.py"), 'w').close()

    open(os.path.join(base_path, "README.md"), 'w').close()
    open(os.path.join(base_path, "requirements.txt"), 'w').close()
    open(os.path.join(base_path, ".gitignore"), 'w').close()
    open(os.path.join(base_path, "config.py"), 'w').close()
    open(os.path.join(base_path, ".env"), 'w').close()

    logging.warning(f"Project structure created at {base_path}")


if __name__ == "__main__":
    create_virtual_environment(os.getcwd())
