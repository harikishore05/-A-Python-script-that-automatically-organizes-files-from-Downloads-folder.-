import os
import shutil
from pathlib import Path
from datetime import datetime

# Automatically get the Downloads folder path
folder_path = str(Path.home() / "Downloads")

# Define file type categories
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.txt', '.pptx', '.xlsx'],
    'Audio': ['.mp3', '.wav'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Archives': ['.zip', '.rar', '.tar', '.7z'],
    'Scripts': ['.py', '.js', '.html', '.css'],
    'Others': []
}

# Loop through files in the folder
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    
    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[1].lower()
        moved = False

        for folder, extensions in file_types.items():
            if file_ext in extensions:
                target_folder = os.path.join(folder_path, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(target_folder, file))
                moved = True
                break

        if not moved:
            target_folder = os.path.join(folder_path, 'Others')
            os.makedirs(target_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(target_folder, file))

# Log when the script runs
with open(os.path.join(folder_path, "file_manager_log.txt"), "a") as log:
    log.write(f"Ran file manager at {datetime.now()}\n")

print("✅ File organization complete!")
