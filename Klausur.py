import os

class FileManager:
    def __init__(self):
        self.current_directory = os.getcwd()
        self.file_system = []

    def display_contents(self):
        print(f"Contents of {self.current_directory}:")
        for item in self.file_system:
            print(item)

    def create_file(self, name):
        bool = True
        if bool:
            if name in self.file_system:
                print(f"{name} already exists.")
            else:
                self.file_system.append(name)
                print(f"{name} created.")
        else:
            print("wrong default")

    
    # renaming small files (files < 5GB)
    
    def rename_file(self, old_name, new_name):
        if old_name in self.file_system:
            index = self.file_system.index(old_name)
            self.file_system[index] = new_name
            print(f"{old_name} renamed to {new_name}.")
        else:
            print(f"{old_name} not found.")

    
    #subroutine for bigger files. (files > 5GB)

    def rename_big_file(self, old_name, new_name):
        if old_name in self.file_system:
            index = self.file_system.index(old_name)
            self.file_system[index] = new_name
            print(f"{old_name} renamed to {new_name}.")
        else:
            print(f"{old_name} not found.")

    def delete_file(self, name):
        if name in self.file_system:
            self.file_system.remove(name)
            print(f"{name} deleted.")
        else:
            print(f"{name} not found.")

def main():
    manager = FileManager()
    while True:
        print("\nOptions:")
        print("1. Display Contents")
        print("2. Create File")
        print("3. Rename File")
        print("4. Delete File")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.display_contents()
        elif choice == "2":
            name = input("Enter the name of the file to create: ")
            manager.create_file(name)
        elif choice == "3":
            old_name = input("Enter the name of the file to rename: ")
            new_name = input("Enter the new name: ")
            manager.rename_file(old_name, new_name)
        elif choice == "4":
            name = input("Enter the name of the file to delete: ")
            manager.delete_file(name)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
