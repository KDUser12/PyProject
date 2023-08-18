# User Manual
> Here is the user manual to follow in order to start well on PyProject.

## Installing
We recommend that you follow the steps to install the document [installation](https://github.com/KDUser12/PyProject/blob/main/docs/installation.md).

## Launch of the program
To start running the `main.exe` file that is the default in the `C:\Program Files\PyProject` directory or the `PyProject` shortcut on your desktop.

## Project
### Create a Project
To create a new project, enter the `create project` command and enter the following information :

- Project Name
- Product Name
- Version
- Description
- Authors
- Project Directory
- Backup Directory

After entering all this information, congratulations ! You have just created a project!

**Attention**: The current version of the program does not allow to create several projects at once.

### Delete a Project
To delete your project, enter the `delete project` command and your project will be deleted.

**Attention**: This action cannot be reversed.

## Backup
### Create a Backup
Enter the `create backup` command and... that’s it!
You have just created a backup of your entire project, if you want to access this backup then you will have to go to the directory you have designated as the backups directory.

### Load a Backup
Enter the `load backup` command and enter the number of your backup which is 1 to inf.

After doing this, your project will be put in a folder `C:\Program Files\PyProject\app\cache\project_data\project_archive` and your project will be replaced by backup.

### Delete a Backup
To delete a backup, use the `delete backup` command and enter your backup number.

**Attention**: If you delete a backup you will not be able to go back.

## Delete all Data

To delete all data from your project (including backup) enter the command `delete data`.
If you want to delete your project enter first the [`delete project`](https://github.com/KDUser12/PyProject/main/docs/user_manual.md#delete-a-project) command.

**Attention**: This action cannot be reversed.

## Other
To learn more, enter the `help`, `license` and `credits`commands.

And if you want to quit the program enter the command `shutdown`.s