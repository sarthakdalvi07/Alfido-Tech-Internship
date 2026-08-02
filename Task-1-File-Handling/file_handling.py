# Task 1: Python File Handling & Automation
# Author: Sarthak Dalvi

import os
import shutil

try:
    
    with open("sample.txt", "r") as file:
        content = file.read()

    print("Original File Content:")
    print(content)

    with open("output.txt", "w") as file:
        file.write(content)
        file.write("\nThis line was added automatically.")

    print("\nContent copied to output.txt")


    os.rename("output.txt", "new_output.txt")
    print("File renamed to new_output.txt")

    if not os.path.exists("Backup"):
        os.mkdir("Backup")
    shutil.move("new_output.txt", "Backup/new_output.txt")
    print("File moved to Backup folder")

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except Exception as e:
    print("Unexpected Error:", e)