#exception handling
def divide_numbers(num1,num2):
    try:
        result = num1/num2
        print("Result: ", result)

    except ZeroDivisionError:
        print("Error :Cannot divide by zero!")
    except TypeError:
        print("Error :Invalid operand types for division!")
    except Exception as e:
        print("An error occcured:", str(e))

#valid division
divide_numbers(10,2)

#division by zero
divide_numbers(10,0)

#invalid operand
divide_numbers("10",2)

#other error
divide_numbers(10,"2")


#with file handling
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print("File contents:\n", contents)
    except FileNotFoundError:
        print(f"Error: File not found. Could not locate the file at '{file_path}'.")
    except PermissionError:
        print(f"Error: Permission denied. You don't have sufficient permissions to access the file at '{file_path}'.")
    except IOError:
        print(f"Error: Input/output error occurred while reading the file at '{file_path}'.")
    except IsADirectoryError:
        print(f"Error: The specified path '{file_path}' points to a directory, not a file.")
    except UnicodeDecodeError:
        print(f"Error: Unable to decode the file contents. It may not be a text file.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file at '{file_path}': {str(e)}")

# Example usage
# Case 1: Valid file path
read_file("sample.txt")

# Case 2: File not found
read_file("nonexistent.txt")

# Case 3: Permission denied
read_file("/root/important.txt")

# Case 4: Input/output error
read_file("corrupted_file.txt")

# Case 5: Path is a directory
read_file("my_directory/")

# Case 6: Unable to decode file contents
read_file("binary_file.bin")
