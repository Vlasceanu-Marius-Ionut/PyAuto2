import os
import shutil
import time
import schedule

SOURCE = r"C:\Users\MARIUS-PC\Desktop\python\auto-backup-source"
DESTINATION = r"C:\Users\MARIUS-PC\Desktop\python\auto-backup folder\backupfolder"

def make_backup():
    existing = os.listdir(DESTINATION)
    backup_number = len(existing) + 1
    folder_name = f"backup{backup_number}"
    target = os.path.join(DESTINATION, folder_name)

    try:
        shutil.copytree(SOURCE, target)
        print("Backup made in:", target)
    except Exception as e:
        print("Backup error:", e)

schedule.every().day.at("13:55").do(make_backup)

print("Auto backup starting...")

while True:
    schedule.run_pending()
    time.sleep(60)
