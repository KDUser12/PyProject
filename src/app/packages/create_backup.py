# V1.0.0

import json
import os
from datetime import datetime
import pickle
import shutil

def json_data(JSON_FILE):
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, 'r') as file:
            data_content = json.load(file)

        project_directory = data_content['project_directory']
        backup_directory = data_content['backup_directory']

        return project_directory, backup_directory

class CreateBackup:
    def create_backup(project_directory, backup_directory):
        try:
            print(f"[{datetime.now()}] : Creation of the backup in progress...")
            BACKUP_VALUE_PATH = 'app/cache/project_data/backup_value.pickle'
            if os.path.exists(BACKUP_VALUE_PATH):
                with open(BACKUP_VALUE_PATH, 'rb') as file:
                    backup_value = pickle.load(file)
            else:
                backup_value = 1

            shutil.copytree(project_directory, f'{backup_directory}/project_backup/backup_{backup_value}')

            backup_content = f"""

{{
    "backup_name": "{backup_value}",
    "backup_directory": "{backup_directory}/project_backup/backup_{backup_value}",
    "project_directory": "{project_directory}"
}}

"""
            os.makedirs('app/cache/project_data/backups_data')
            with open(f'app/cache/project_data/backups_data/backup_{backup_value}.json', 'w') as file:
                file.write(backup_content)

            backup_value = backup_value + 1
            with open(BACKUP_VALUE_PATH, 'wb') as file:
                pickle.dump(backup_value, file)

            print(f"[{datetime.now()}] : Creation of the backup completed!")

        except OSError as error:
            print(f"[{datetime.now()}] : An error occurred when creating the backup :", error)

    def check_directory(project_directory, backup_directory):
        try:
            if os.path.exists(project_directory):
                if os.path.exists(backup_directory):
                    return True
        except OSError as error:
            print(f"[{datetime.now()}] : An error occurred during the project check :", error)
            return False

if __name__ == '__main__':
    JSON_FILE = 'app/cache/project_data/project_config.json'
    project_directory, backup_directory = json_data(JSON_FILE)

    if CreateBackup.check_directory(project_directory, backup_directory):
        CreateBackup.create_backup(project_directory, backup_directory)