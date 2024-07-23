import argparse
import os
import subprocess
import sys
import venv
import shutil

class VenvManager:
    def __init__(self, venv_path='venv'):
        self.venv_path = venv_path
        self.pip_executable = os.path.join(self.venv_path, 'bin', 'pip') if os.name != 'nt' else os.path.join(self.venv_path, 'Scripts', 'pip')
        self.python_executable = os.path.join(self.venv_path, 'bin', 'python') if os.name != 'nt' else os.path.join(self.venv_path, 'Scripts', 'python')

    def create_venv(self):
        """Create a virtual environment if it doesn't exist."""
        if not os.path.exists(self.venv_path):
            venv.EnvBuilder(with_pip=True).create(self.venv_path)
            print(f"Created virtual environment at {self.venv_path}.")
        else:
            print(f"Virtual environment already exists at {self.venv_path}.")

    def install_requirements(self, requirements_file):
        """Install requirements using pip."""
        subprocess.run([self.pip_executable, 'install', '-r', requirements_file])

    def install_packages(self, packages):
        """Install packages with pip."""
        subprocess.run([self.pip_executable, 'install'] + packages)

    def resolve_dependencies(self, packages):
        """Resolve and install the dependencies, ensuring compatibility."""
        subprocess.run([self.pip_executable, 'install', 'pip-tools'])
        with open('temp_requirements.in', 'w') as f:
            f.write("\n".join(packages))
        subprocess.run([self.pip_executable, 'compile', 'temp_requirements.in', '--output-file', 'temp_requirements.txt'])
        self.install_requirements('temp_requirements.txt')
        os.remove('temp_requirements.in')
        os.remove('temp_requirements.txt')
        print("Installed packages with resolved dependencies.")

    def smart_install(self, packages, requirements_file):
        """Smart install packages and/or requirements.txt"""
        self.create_venv()

        if requirements_file:
            self.install_requirements(requirements_file)
        
        if packages:
            self.resolve_dependencies(packages)
        
        print("All packages installed successfully.")

def main():
    parser = argparse.ArgumentParser(description="SmartVenv: A Smarter Virtual Environment and Dependency Management Tool")
    parser.add_argument('--venv', type=str, default='venv', help='Path to the virtual environment directory')
    parser.add_argument('-r', type=str, help='Path to the requirements.txt file')
    parser.add_argument('install', nargs='*', help='List of packages to install')
    
    args = parser.parse_args()
    
    manager = VenvManager(args.venv)

    if args.r or args.install:
        manager.smart_install(args.install, args.r)
    else:
        print("Please provide either -r or install packages.")
        parser.print_help()

if __name__ == '__main__':
    main()

