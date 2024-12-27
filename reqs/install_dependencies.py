import subprocess
import sys

def install_dependencies():
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
        
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
        
        print("All dependencies installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing dependencies: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()