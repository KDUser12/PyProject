import shutil
from datetime import datetime

def delete_data():
    try:
        print("Are you sure you want to delete all data from your project?")
        if input('[Y] [N]\n> ') == 'y':
            print(f"[{datetime.now()}] : Deleting data from your current project...")
            shutil.rmtree('app/cache/project_data')
            print(f"[{datetime.now()}] : Your project data has been deleted!")
    except OSError as error:
        print(f"[{datetime.now()}] : An error occurred while deleting data:", error)

if __name__ == '__main__':
    delete_data()