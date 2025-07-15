import os
import shutil

# Set the source (backup) and target (active MySQL) directories
source_dir = r"D:\xampp\mysql\data_old"   # <- Change this if your backup folder is different
target_dir = r"D:\xampp\mysql\data"

# Extensions and filenames to copy
valid_files = ['.frm', '.ibd', '.MYD', '.MYI', '.opt']
specific_files = ['ib_logfile0', 'ib_logfile1', 'ibdata1']

def copy_files():
    if not os.path.exists(source_dir):
        print(f"Source directory not found: {source_dir}")
        return

    if not os.path.exists(target_dir):
        print(f"Target directory does not exist: {target_dir}")
        os.makedirs(target_dir)
        print(f"Created target directory: {target_dir}")

    # Copy files from root of data_old (like ibdata1, ib_logfile*)
    for file in os.listdir(source_dir):
        src_path = os.path.join(source_dir, file)
        dst_path = os.path.join(target_dir, file)

        if os.path.isfile(src_path) and (
            any(file.endswith(ext) for ext in valid_files) or file in specific_files
        ):
            try:
                shutil.copy2(src_path, dst_path)
                print(f"Copied: {file}")
            except Exception as e:
                print(f"Failed to copy {file}: {e}")

    # Copy database folders and their contents
    for db_dir in os.listdir(source_dir):
        src_db_path = os.path.join(source_dir, db_dir)
        dst_db_path = os.path.join(target_dir, db_dir)

        if os.path.isdir(src_db_path):
            if not os.path.exists(dst_db_path):
                os.makedirs(dst_db_path)

            for file in os.listdir(src_db_path):
                if any(file.endswith(ext) for ext in valid_files):
                    try:
                        shutil.copy2(os.path.join(src_db_path, file), os.path.join(dst_db_path, file))
                        print(f"Copied: {db_dir}/{file}")
                    except Exception as e:
                        print(f"Failed to copy {db_dir}/{file}: {e}")

    print("✅ Done copying MySQL files.")

if __name__ == "__main__":
    copy_files()
