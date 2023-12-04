import os
import sys

fp = open(r'./output.txt', 'w')

file_count = 0
folder_increment = 0


def find_files(dir_path, extension):
    global file_count
    global folder_increment
    # Check if the given path is a valid directory
    if not os.path.isdir(dir_path):
        print("\n#Error : Please..!! Provide Valid Path.\nThank you....:-)")
        return

    if str(extension[0]) != '.':
        print("\n#Error : Please..!! Provide Valid Extension format.\nThank you....:-)")
        return

    # Get a list of all the files and directories in the given directory
    files_and_dirs = os.listdir(dir_path)

    # Iterate over the list of files and directories
    for file_or_dir in files_and_dirs:
        # Construct the full path of the file or directory
        full_path = os.path.join(dir_path, file_or_dir)

        # If the full path is a directory, recursively call the function to find the files in that directory
        if os.path.isdir(full_path):
            folder_increment = folder_increment+1
            find_files(full_path, extension)
        else:
            # If the full path is a file that ends with extension, print its path
            if full_path.endswith(extension):
                if sys.argv[3] == "y" or sys.argv[3] == "Y":
                    fp.write(full_path + "\n")
                    file_count = file_count + 1
                    print(full_path)
                elif sys.argv[3] == "n" or sys.argv[3] == "N":
                    fp.write(file_or_dir + "\n")
                    file_count = file_count + 1
                    print(file_or_dir)
                else:
                    print("\n#Error : Needed file name with path ? Please provide input as 'Y'.\nThank you....")
                    break
    return


def print_output(file_cnt, folder_inc):
    if file_cnt == 0 and folder_inc >= 0:
        print("\nExtension not available. Try with some other extension.\nThank you....\n")
    elif file_cnt == 1:
        print("\nEureka...!!! Only 1 file is present with extension " + sys.argv[2]
              + ".\nOpen Output.txt to collect Data.\nThank you....\n")
    else:
        print("\nEureka...!!! In Total " + str(file_cnt) + " files are present with extension " + sys.argv[2]
              + ".\nOpen Output.txt to collect Data\n")


# Calling Functions
find_files(sys.argv[1], sys.argv[2])
print_output(file_count, folder_increment)
fp.close()
