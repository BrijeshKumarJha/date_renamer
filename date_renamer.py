from pathlib import Path
from datetime import datetime

def date_renamer():
    folder_input = input("Enter folder path ")
    folder_path = Path(folder_input)
    if not folder_path.exists() or not folder_path.is_dir():
        print("Invalid folder name or path ")
        return

    choice = input("Enter choice for date prefix\n1. Create time\n2. Modification time (recommended)\nEnter choice: ")
    count = 0

    for item in folder_path.iterdir():
        if item.is_file():
            file_stats = item.stat()

            if choice == "1":
                raw_time = file_stats.st_ctime
            elif choice == "2":
                raw_time = file_stats.st_mtime
            else:
                print("Invalid input, defaulting to modification time ")
                raw_time = file_stats.st_mtime

            raw_date = datetime.fromtimestamp(raw_time)
            formatted_date = raw_date.strftime("%Y-%m-%d")

            new_name = f"{formatted_date}_{item.name}"
            new_file_path = item.with_name(new_name)

            item.rename(new_file_path)
            print(f"original name: {item.name} -> new name: {new_name}")
            count += 1
            print()
    print(f"\n Succesfully renamed {count} files")

if __name__ == "__main__":
    date_renamer()

