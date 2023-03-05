import subprocess

# Get user input for the name of the file to find
filename = input("Enter the name of the file to find: ")

# Use subprocess to execute find command with arguments
process = subprocess.Popen(['cats', '.', '-name', filename], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Get output and error messages from subprocess
output, error = process.communicate()

# Print output and error messages
print("Output: ", output.decode('utf-8'))
print("Errors: ", error.decode('utf-8'))
