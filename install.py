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

def build_env():
    """generate the initial .env file."""
    with open('.env', 'w') as env_file:
        env_file.write("PROVISIONING_API_URL=https://provisioning.xtremeenterprises.com/api/v1/bulk-load-sim-cards/\n")
        api_key = input("\nPlease enter your API key: ")
        env_file.write(f"PROVISIONING_API_KEY={api_key}\n")


if __name__ == '__main__':
    venv_dir = create_venv()
    install_requirements(venv_dir)
    build_env()
    print(
        """
          \n
          Installation complete. You can now run the script. 
          If you would like to edit any of the configuration settings, 
          you can do so by editing the .env file in this directory.
        """
    )