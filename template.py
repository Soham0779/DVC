import os

# Define the folder and file structure
folders = [
    'data/raw',
    'data/processed',
    'notebooks',
    'src/data',
    'src/features',
    'src/models',
    'scripts',
    'tests'
]

files = [
    '.gitignore',
    'README.md',
    'requirements.txt'
]

init_files = [
    'data/__init__.py',
    'notebooks/__init__.py',
    'src/data/__init__.py',
    'src/features/__init__.py',
    'src/models/__init__.py',
    'scripts/__init__.py',
    'tests/__init__.py'
]

def create_folders_and_files():
    # Create folders
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f'Created folder: {folder}')
    
    # Create files
    for file in files:
        with open(file, 'w') as f:
            pass  # Create empty file
        print(f'Created file: {file}')

    # Create __init__.py files
    for init_file in init_files:
        with open(init_file, 'w') as f:
            pass  # Create empty __init__.py file
        print(f'Created file: {init_file}')

if __name__ == "__main__":
    create_folders_and_files()
    print("Project structure created successfully!")
    