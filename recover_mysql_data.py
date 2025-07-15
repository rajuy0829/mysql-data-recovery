import os
import shutil
import sys

# ======= CONFIG =======
# Set your paths here
BACKUP_FOLDER = r"D:\xampp\mysql\data_old"
TARGET_DATA_FOLDER = r"D:\xampp\mysql\data"

# Table files to recover (add more if needed)
TABLE_EXTENSIONS = [".frm", ".ibd", ".myd", ".myi", ".MRG", ".TRG", ".TRN"]

# =======================

def copy_table_files(backup_folder, target_folder):
    if not os.path.exists(backup_folder):
        print(f"❌ Backup folder does not exist: {backup_folder}")
        sys.exit(1)

    if not os.path.exists(target_folder):
        print(f"❌ Target data folder does not exist: {target_folder}")
        sys.exit(1)

    print(f"📦 Recovering MySQL table files from:\n{backup_folder}\n→ To:\n{target_folder}\n")

    files_copied = 0
    for root, dirs, files in os.walk(backup_folder):
        relative_path = os.path.relpath(root, backup_folder)
        target_subfolder = os.path.join(target_folder, relative_path)

        if not os.path.exists(target_subfolder):
            os.makedirs(target_subfolder)

        for file in files:
            if any(file.endswith(ext) for ext in TABLE_EXTENSIONS):
                source_file = os.path.join(root, file)
                dest_file = os.path.join(target_subfolder, file)

                try:
                    shutil.copy2(source_file, dest_file)
                    print(f"✅ Copied: {source_file} → {dest_file}")
                    files_copied += 1
                except Exception as e:
                    print(f"⚠️ Failed to copy {file}: {e}")

    print(f"\n✅ Done! Total files copied: {files_copied}")
    print("⚠️ Reminder: Make sure to use 'innodb_force_recovery' in my.ini if InnoDB crashes.")
    print("⚠️ Restart MySQL after recovery and remove 'innodb_force_recovery' once complete.")

if __name__ == "__main__":
    copy_table_files(BACKUP_FOLDER, TARGET_DATA_FOLDER)
