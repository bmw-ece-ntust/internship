'''

After running this code, you can install all dependecies inside requirements.txt using:
pip install -r requirements.txt

'''

import json
import subprocess
import sys

def extract_imports(notebook_path):
    """Extracts import statements from a Jupyter Notebook."""
    with open(notebook_path, 'r') as f:
        notebook = json.load(f)
    
    imports = set()
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            for line in cell['source']:
                line = line.strip()
                if line.startswith('import ') or line.startswith('from '):
                    imports.add(line)
    return imports

def get_package_version(package):
    """Gets the version of an installed package."""
    try:
        version = subprocess.check_output([sys.executable, '-m', 'pip', 'show', package])
        for line in version.decode().split('\n'):
            if line.startswith('Version:'):
                return line.split()[1]
    except subprocess.CalledProcessError:
        return None

def create_requirements_txt(imports, output_path='requirements.txt'):
    """Creates a requirements.txt file with the given imports."""
    packages = set()
    for imp in imports:
        if imp.startswith('import '):
            packages.add(imp.split()[1].split('.')[0])
        elif imp.startswith('from '):
            packages.add(imp.split()[1].split('.')[0])
    
    # Ensure 'sklearn' is replaced by 'scikit-learn'
    packages = {'scikit-learn' if pkg == 'sklearn' else pkg for pkg in packages}
    
    packages_with_versions = {}
    for package in packages:
        version = get_package_version(package)
        if version:
            packages_with_versions[package] = version
    
    with open(output_path, 'w') as f:
        for package, version in packages_with_versions.items():
            f.write(f"{package}=={version}\n")
    
    print(f"{output_path} created.")

if __name__ == "__main__":
    notebook_path = 'NTUST_Notebook.ipynb'  # Update this path if necessary
    imports = extract_imports(notebook_path)
    create_requirements_txt(imports)
    print("install all dependencies using 'pip install -r requirements.txt'")
