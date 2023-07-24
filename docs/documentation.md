# Documentation
> Here is the complete documentation of PyProject.

## Code Structuring
### Create a Project
By entering the `create project` command you will have to enter several information about your project, then the program will create a `project_data` folder and then create a JSON `project_config.json` file containing the information you entered before.

Then the program will launch the `build_project.py` file that will create the project.
It will then retrieve the information from the `project_config.json` file and then use it to create the project.

### Create a Backup
When the `create backup` command is launched, the program retrieves information from the `project_config` file and creates a `backup_value.pickle` file in order to store the `backup_value` variable.

After it will copy the project directory to be able to paste it into a folder named `backup_{backup_value}` then it will create a `backup_{backup_value}.json` containing the backup information.

### Load a Backup
After entering the `load backup` command and the backup number, the program will retrieve the backup information using the `backup_{backup_value}.json` file.

It will then retrieve the project directory and copy it to move it to an `archive` folder and then replace the project with backup.

### Delete All Data
After entering the `delete data` command, the program will simply delete the `project_data` file that contains all the project information.

### Delete a Project
By entering the `delete project` command, the program will simply retrieve the project directory using the `project_config.json` file and then delete the project.

### Delete a Backup
After entering the `delete backup` command and entering the backup number, the program will retrieve the backup information using the `backup_{backup_value}.json` file for after deleting it.