import shutil
import os

def copy_file(source_path, destination_path):
    shutil.copy(source_path, destination_path)
    print(f"File copied successfully from {source_path} to {destination_path}")

def move_file(source_path, destination_path):
    shutil.move(source_path, destination_path)
    print(f"File moved successfully from {source_path} to {destination_path}")

def remove_file(file_path):
    os.remove(file_path)
    print(f"File {file_path} removed successfully")

def create_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)
    print(f"Folder {folder_path} created successfully")

def main():
    while True:
        # Ask the user for the action (copy, move, remove, create, or exit)
        action = input("Choose an action (copy, move, remove, create, or exit): ").lower()

        if action == 'exit':
            break
        elif action == 'create':
            # Ask for the folder path if the action is create
            folder_path = input("Enter the folder path to create: ")
            create_folder(folder_path)
        else:
            # Ask for the file path
            source_path = input("Enter the source file/folder path: ")

            if action in ['copy', 'move']:
                # Ask for the destination path if the action is copy or move
                destination_path = input("Enter the destination file/folder path: ")

                if action == 'copy':
                    copy_file(source_path, destination_path)
                elif action == 'move':
                    move_file(source_path, destination_path)
            elif action == 'remove':
                # Perform the remove action
                remove_file(source_path)
            else:
                print("Invalid action. Please choose copy, move, remove, create, or exit.")

        # Ask the user if they want to perform another action or exit
        another_action = input("Do you want to do anything else? (yes/no): ").lower()
        if another_action != 'yes':
            break

if __name__ == "__main__":
    main()
