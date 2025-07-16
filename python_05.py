import os
def create_file():
    filename = input("Enter filename to create: ")
    with open(filename, "w") as f:
        print(f"✅ File {filename} created successfully. ")

def write_file():
    filename = input("Enter filename to write: ")
    if os.path.exists(filename):
        content = input("Enter text to file into file. ")
        with open(filename, "a") as f:
            f.write(content + "\n")
        print("✅ Content written successfully.")
    else:
        print("❌ File does not exist.")

def read_file():
    filename = input("Enter filename to read: ")
    if os.path.exists(filename):
        with open(filename, "r") as f:
            print(f"\n 📝 File Content: ")
            print(f.read())
    else:
        print("❌ file not found. ")

def delete_file():
    filename = input("Enter filename to delete: ")
    if os.path.exists(filename):
        os.remove(filename)
        print(f"🗑️ File '{filename}' deleted successfully. ")
    else:
        print("❌ not found. ")

def rename_file():
    oldfile = input("Enter old filename: ")
    currentfile = input("Enter new filename: ")
    if os.path.exists(oldfile):
        os.rename(create_file, currentfile)
        print(f"✅ File rename to '{currentfile}'. ")
    else:
        print("❌ Original file doesn't exist. ")

def list_file():
    files = os.listdir()
    print("\n 📂 Files in current directory: ")
    for f in files:
        print(f"•", f)

def file_manager():
    while True:
        print("\n" + "="*35)
        print("📁 PYTHON TERMINAL FILE MANAGER")
        print("-" * 35)
        print("="*35)
        print("1. Create File")
        print("2. Write to File")
        print("3. Read File")
        print("4. Delete File")
        print("5. Rename File")
        print("6. List Files")
        print("7. Exit")
        print("-"*35)

        choice = input("Choose option: ")
        if choice == "1":
            create_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            read_file()
        elif choice == '4':
            delete_file()
        elif choice == "5":
            rename_file()
        elif choice == "6":
            list_file()
        elif choice == "7":
            print("👋 Exiting... Thank you!")

        else:
            print("❌ Invalid option! Please choose between 1 to 7.")
file_manager()