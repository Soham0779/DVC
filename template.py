import os

# Define the folder and file structure
folders = [
    'data/raw',
    'notebooks',
    'src/data',
    'src/features',
    'src/models',
    'tests'
]

files = [
    '.gitignore',
    'requirements.txt'
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

if __name__ == "__main__":
    create_folders_and_files()
    print("Project structure created successfully!")
