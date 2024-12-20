import os
import sys
import subprocess

def create_venv():
    """Create a virtual environment if it doesn't exist."""
    venv_dir = os.path.join(os.getcwd(), '.venv')
    if not os.path.exists(venv_dir):
        print("Creating virtual environment...")
        subprocess.check_call([sys.executable, '-m', 'venv', venv_dir])
    return venv_dir

def install_requirements(venv_dir):
    """Install requirements from requirements.txt into the virtual environment."""
    print("Installing dependencies from requirements.txt...")
    pip_path = os.path.join(venv_dir, 'Scripts', 'pip') if os.name == 'nt' else os.path.join(venv_dir, 'bin', 'pip')
    subprocess.check_call([pip_path, 'install', '-r', 'requirements.txt'])

def install_api_key():
    """Save the API key to a .env file."""
    with open('.env', 'w') as env_file:
        api_key = input("\nPlease enter your API key: ")
        env_file.write(f"API_KEY={api_key}\n")

if __name__ == '__main__':
    venv_dir = create_venv()
    install_requirements(venv_dir)
    install_api_key()
    print("\nInstallation complete.")