import os
import json
import pickle
import shutil

def json_data(JSON_FILE_PATH):
    with open(JSON_FILE_PATH, 'r') as json_file:
        data = json.load(json_file)

    directory = data['directory']

    return directory

class CreateBackup():
    def check_folder(directory):
        try:
            if os.path.exists(directory):
                return True
            else: 
                raise OSError(f"[ The project folder is not found : {directory} ]")
        except OSError as error:
            print("An error occurred during the project check :", error)
            return error
    
    def create_backup(directory):
        backup_number = 1

        try:
            with open("app/cache/data/backup_number.pickle", 'rb') as file:
                backup_number = pickle.load(file)

            destination_directory = input("Choose a destination directory :\n> ")
            shutil.copytree(directory, f"{destination_directory}project_backup/backup_{backup_number}")

            backup_number += 1
            with open("app/cache/data/backup_number.pickle", 'wb') as file:
                pickle.dump(backup_number, file)
        
        except OSError as error:
            print("An error occurred during the project check :", error)

if __name__ == "__main__":
    JSON_FILE_PATH = 'app/cache/project-config.json'
    directory = json_data(JSON_FILE_PATH)

    if CreateBackup.check_folder(directory):
        CreateBackup.create_backup(directory)