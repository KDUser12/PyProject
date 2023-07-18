import os
from datetime import datetime
import json
import shutil

class loadBackup:
    def load_backup(backup_value):
        print(f"[{datetime.now()}] : Loading the backup in progress...")
        with open(f'app/cache/project_data/backups_data/backup_{backup_value}.json', 'r') as file:
            data_content = json.load(file)

        project_directory = data_content['project_directory']
        backup_directory = data_content['backup_directory']

        shutil.copytree(project_directory, f'app/cache/project_data/project_archive/archive_{backup_value}')
        shutil.rmtree(project_directory)
        shutil.copytree(backup_directory, project_directory)

        print(f"[{datetime.now()}] : Loading the backup completed !")

    def check_backup(backup_value):
        try:
            if os.path.exists(f'app/cache/project_data/backups_data/backup_{backup_value}.json'):
                return True
        except OSError as error:
            print(f"[{datetime.now()}] : An error occurred while checking your backup:", error)

if __name__ == '__main__':
    backup_value = input('Enter your backup number :\n> ')

    if loadBackup.check_backup(backup_value):
        loadBackup.load_backup(backup_value)