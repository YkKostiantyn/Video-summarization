import os

def remove_file(*filenames):
    for filename in filenames:
        if filename and os.path.exists(filename):
            os.remove(filename)
            print(f"{filename} removed from memory.")
        else:
            print(f"{filename} not found")