# **********************************************************************************************************************/
#  DISCLAIMER
# **********************************************************************************************************************/
#  The Python tool provided herein is for informational and educational purposes only.
#  It is not intended for use in production environments or for critical operations.
#  The author(s) of this tool make no representations or warranties of any kind,
#  express or implied, about the completeness, accuracy, reliability, suitability,
#  or availability with respect to the tool or the information, products, services,
#  or related graphics contained on the tool for any purpose. Any reliance you place
#  on such information is therefore strictly at your own risk. In no event will the
#  author(s) be liable for any loss or damage including without limitation, indirect
#  or consequential loss or damage, or any loss or damage whatsoever arising from
#  loss of data or profits arising out of, or in connection with, the use of this tool.
# **********************************************************************************************************************/

# ***********************************************************************************************************************
#   REVISION HISTORY
#   --------------------------------------------------------------------------------------------------------------------
#   Version    Date        File Name             Description
#   --------------------------------------------------------------------------------------------------------------------
#   01.00.00   2023-12-04  filenameExtension.py  extract the file name with/without file location based on extension
# *********************************************************************************************************************/


# --------------------------------------------------------------------------------------
# Import Python Libraries
# --------------------------------------------------------------------------------------
import os
import sys

# Open File
fp = open(r'./output.txt', 'w')

# Get the file/folder count
file_count = 0
folder_increment = 0


# --------------------------------------------------------------------------------------
# Function Name : find_files
# Description   : Search the file with given extension and generate the output.txt
# --------------------------------------------------------------------------------------
def find_files(dir_path, extension):
    # make the count as global count
    global file_count
    global folder_increment

    # Check if the given path is a valid directory
    if not os.path.isdir(dir_path):
        print("\n#Error : Please..!! Provide Valid Path.\nThank you....:-)")
        return
    # Check if the given extension is a valid extension
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
            folder_increment = folder_increment + 1
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


# --------------------------------------------------------------------------------------
# Function Name : print_output
# Description   : Evaluate the final output and inform User
# --------------------------------------------------------------------------------------
def print_output(file_cnt, folder_inc):
    if file_cnt == 0 and folder_inc >= 0:
        print("\nExtension not available. Try with some other extension.\nThank you....\n")
    elif file_cnt == 1:
        print("\nEureka...!!! Only 1 file is present with extension " + sys.argv[2]
              + ".\nOpen Output.txt to collect Data.\nThank you....\n")
    else:
        print("\nEureka...!!! In Total " + str(file_cnt) + " files are present with extension " + sys.argv[2]
              + ".\nOpen Output.txt to collect Data\n")


# --------------------------------------------------------------------------------------
# Calling Functions
# --------------------------------------------------------------------------------------
find_files(sys.argv[1], sys.argv[2])
print_output(file_count, folder_increment)

# Close file
fp.close()
