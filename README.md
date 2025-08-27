Auto Backup Script

This Python script automatically backs up a folder every day at a specified time.
Features
Copies all contents from a source folder to a backup folder.
Creates numbered backups (backup1, backup2, …) to avoid overwriting.
Runs daily at a scheduled time (e.g., 13:55).

How It Works
Counts existing backups in the destination folder.
Creates a new folder with the next number.
Copies the source folder into the new backup folder.
Runs continuously and checks every minute for the scheduled time.

Setup
Set SOURCE to the folder you want to back up.
Set DESTINATION to where backups should be stored.
Adjust the schedule time in the script:
schedule.every().day.at("HH:MM").do(make_backup)
