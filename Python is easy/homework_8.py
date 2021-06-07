import os.path
import sys


file_name = input("Enter a file name: " )
if os.path.isfile(file_name) == False:
    print(f"{file_name} does not exist on the file system")
    write_to_file = input(f"Enter the text to be written to {file_name} : ")
    with open(file_name, "w") as f:
        f.write(write_to_file)
else:
    print(f"{file_name} exists on the filesystem")
    action = input(f"What action do you want to perform on {file_name}\nEnter r to Read, d to Delete and start over, a to append and rl to replace a line\nAction: ")
    if action == "r":
        with open(file_name, "r") as f:
          print(f.read())
    elif action == "d":
        os.remove(f"{file_name}")
        open(file_name, "w") 
    elif action == "a":
        added_text = input("Enter text to be appended\nText: ")
        with open(file_name, "a") as f:
            f.write("\n" + added_text)
    elif action == "rl":
        line_to_update = int(input("Enter a line to update\nLine: "))
        new_text = input("Enter new text\nText: ")
        with open(file_name, "r") as f:
            lines_edit = f.readlines()
            lines_edit[line_to_update-1] = new_text + "\n"
        with open(file_name, "w") as f:
            f.writelines(lines_edit)
