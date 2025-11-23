from  functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    print("------------------------------------------\n")
    print("Test the first function\n")
    print("------------------------------------------\n")
    print()
    working_directory = "calculator"
    root_content = get_files_info(working_directory)
    pkg_content = get_files_info(working_directory, "pkg")
    out_content = get_files_info(working_directory, "../")
    print("Contents of calculator/:\n")
    print(root_content)
    print("Contents of calculator/pkg/:\n")
    print(pkg_content)
    print("Contents of parent directory:\n")
    print(out_content)
    print()
    print("------------------------------------------\n")
    print("Test the secound function\n")
    print("------------------------------------------\n")
    print()

    print("Reading main.py:\n")
    print(get_file_content(working_directory, "main.py"))
    print("\nReading pkg/calculator.py:\n")
    print(get_file_content(working_directory, "pkg/calculator.py"))
    print("\nAttempting to read non-existent file pkg/notexist.py:\n")
    print(get_file_content(working_directory, "pkg/notexist.py"))
    print("\nAttempting to read /bin/cat (should be denied):\n")
    print(get_file_content(working_directory, "/bin/cat"))

    # print("------------------------------------------\n")
    # print("Test the third function\n")
    # print("------------------------------------------\n")
    # print()
    # print("Overwriting calculator/lorem.txt:\n")
    # print(write_file(working_directory, "lorem.txt", "New content for lorem.txt using write_file function."))
    # print(write_file(working_directory, "pkg/morelorem.txt", "New content for lorem.txt using write_file function."))  created morelorem.txt in pkg directory.
    # print(write_file("calculator", "../outside.txt", "This should be denied."))  # attempting to write outside working directory. this should not be working
    # print(write_file("calculator", "pkg2/newdir.txt", "This should be denied.")) # attempting to write in a non-existing directory. this should create the directory and write the file.
    print("------------------------------------------\n")
    print("Test the fourth function\n")
    print("------------------------------------------\n")
    print()
    print("Running calculator/main.py:\n")
    print(run_python_file(working_directory, "main.py", ["3 + 5"]))
    print("Running calculator/pkg/calculator.py:\n")
    print(run_python_file(working_directory, "pkg/calculator.py"))
    print("Attempting to run non-Python file calculator/lorem.txt:\n")
    print(run_python_file(working_directory, "lorem.txt"))
    print("Attempting to run non-existent file calculator/notexist.py:\n")
    print(run_python_file(working_directory, "notexist.py"))
    print("Attempting to run ../outside.py (should be denied):\n")
    print(run_python_file(working_directory, "../outside.py"))

main()