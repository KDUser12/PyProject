import shutil
from datetime import datetime
import json
import os

def json_data(JSON_FILE):
    try:
        with open(JSON_FILE, 'r') as file:
            data_content = json.load(file)

        backup_directory = data_content['backup_directory']

        return backup_directory
    
    except OSError as error:
        print(f"[{datetime.now()}] : An error occurred while deleting your backup:", error)

        return False

def delete_backup(backup_directory, backup_value):
    try:
        print("Are you sure you want to delete your backup?")
        if input('[Y] [N]\n> ') == 'y':
            print(f"[{datetime.now()}] : Deleting data from your backup...")
            shutil.rmtree(backup_directory)
            os.remove(f'app/cache/project_data/backups_data/backup_{backup_value}.json')
            print(f"[{datetime.now()}] : Your backup has been deleted!")

    except OSError as error:
        print(f"[{datetime.now()}] : An error occurred while deleting backup:", error)

if __name__ == '__main__':
    backup_value = input('Enter your backup number :\n> ')
    backup_directory = json_data(JSON_FILE=f'app/cache/project_data/backups_data/backup_{backup_value}.json')
    
    delete_backup(backup_directory, backup_value)