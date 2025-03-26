# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error! Division by zero."
#     return a / b

# def main():
#     while True:
#         print("\n Simple Calculator")
#         print("1. Add")
#         print("2. Subtract")
#         print("3. Multiply")
#         print("4. Divide")
#         print("5. Exit")
        
#         choice = input("Enter your choice: ")

        
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == "1":
#                 print("Result:", add(num1, num2))
#         elif choice == "2":
#                 print("Result:", subtract(num1, num2))
#         elif choice == "3":
#                 print("Result:", multiply(num1, num2))
#         elif choice == "4":
#                 print("Result:", divide(num1, num2))
        
#         elif choice == "5":
#             print(" Exiting... Goodbye!")
#             break
#         else:
#             print(" Invalid choice! Please select a number between 1-5.")

# if __name__ == "__main__":
#     main()
import os

def list_files():
    """Lists all files in the current directory"""
    files = os.listdir()
    if files:
        print("\n Files in Directory:")
        for file in files:
            print(f"- {file}")
    else:
        print("\n No files found.")

def create_file():
    """Creates a new file"""
    filename = input("Enter file name: ")
    if os.path.exists(filename):
        print(" File already exists!")
    else:
        with open(filename, "w") as file:
            print(f" File '{filename}' created successfully!")

def write_to_file():
    """Writes content to a file"""
    filename = input("Enter file name to write to: ")
    if os.path.exists(filename):
        content = input("Enter content: ")
        with open(filename, "w") as file:
            file.write(content)
        print(f"Content written to '{filename}'.")
    else:
        print(" File not found!")



def read_file():
    """Reads content from a file"""
    filename = input("Enter file name to read: ")
    if os.path.exists(filename):
        with open(filename, "r") as file:
            print("\n File Content:\n")
            print(file.read())
    else:
        print(" File not found!")

def delete_file():
    """Deletes a file"""
    filename = input("Enter file name to delete: ")
    if os.path.exists(filename):
        os.remove(filename)
        print(f" File '{filename}' deleted.")
    else:
        print(" File not found!")

def main():
    """Main function to run the CLI tool"""
    while True:
        print("\n File Manager CLI")
        print("1. List Files")
        print("2. Create File")
        print("3. Write to File")
        print("4. Read File")
        print("5. Delete File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            list_files()
        elif choice == "2":
            create_file()
        elif choice == "3":
            write_to_file()
        elif choice == "4":
            read_file()
        elif choice == "5":
            delete_file()
        elif choice =="6":
            print(" Exiting... Have a great day!")
            break
        else:
            print(" Invalid choice! Please enter a number between 1-6.")

if __name__ == "__main__":
    main()
