# import os 
# folders = os.listdir("data")

# print(os.getcwd())
# os.chdir("/Users")
# print(os.getcwd())

# for folder in folders:
#     print(folder)
#     print(os.listdir(f"data/{folder}"))


# TELLS ABOUT NO. OF FILES IN A FOLDER

import os

folder_path = r'C:\Users\HP\OneDrive\Desktop\Python'  # Using a raw string to avoid escape characters
# The "r" before the string denotes a raw string, which means that backslashes are treated as literal 
# characters and not as escape characters.
file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])

print(f"The number of files in the folder is: {file_count}")
