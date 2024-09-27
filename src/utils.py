import os
import subprocess
import venv


def create_virtual_environment():
    venv_path = os.path.join(os.getcwd(), "venv")

    # Créer l'environnement virtuel
    venv.EnvBuilder(with_pip=True).create(venv_path)
    print(f"Virtual environment created at {venv_path}")

    # Chemin vers l'exécutable Python de l'environnement virtuel
    python_executable = os.path.join(
        venv_path, "Scripts" if os.name == "nt" else "bin",
        "python")

    # Mettre à jour pip dans l'environnement virtuel
    subprocess.call(
        [python_executable, "-m", "pip", "install", "--upgrade", "pip"])

    print("Pip has been upgraded.")


if __name__ == "__main__":
    create_virtual_environment()
