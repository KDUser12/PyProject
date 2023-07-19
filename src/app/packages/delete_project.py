import shutil
from datetime import datetime
import json

def delete_data(project_directory):
    try:
        print("Are you sure you want to delete your project?")
        if input('[Y] [N]\n> ') == 'y':
            print(f"[{datetime.now()}] : Delete your project...")
            shutil.rmtree(project_directory)
            print(f"[{datetime.now()}] : Your project has been deleted!")
    except OSError as error:
        print(f"[{datetime.now()}] : An error occurred while deleting your project:", error)

def json_data(JSON_FILE):
    try:
        with open(JSON_FILE, 'r') as file:
            data_content = json.load(file)

        project_directory = data_content['project_directory']

        return project_directory
    
    except OSError as error:
        print(f"[{datetime.now()}] : An error occurred while deleting your project:", error)

        return False

if __name__ == '__main__':
    JSON_FILE = 'app/cache/project_data/project_config.json'
    project_directory = json_data(JSON_FILE)

    if not project_directory == False:
        delete_data(project_directory)