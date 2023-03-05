import subprocess

# Get user input for the CATS arguements
contract = "--contract="+input("Enter the name of the .yml file of the contract (ex: openapi.yml): ")
token = "Authorization="+input("Enter your access token to the API: ")
server = "--server="+input("Enter the URL of the API (ex: https://openai.com/api): ")


# Use subprocess to execute the command with arguments
process = subprocess.Popen(['cats', contract, "-H", token, server, "-b -k"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# cats --contract=openapi.yml -H "Authorization=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" --server=https://openai.com/api -b -k


# Get output and error messages from subprocess
output, error = process.communicate()

# Print output and error messages
print("Output: ", output.decode('utf-8'))
print("Errors: ", error.decode('utf-8'))


import subprocess

# Prompt user for arguments
contract = input("Enter contract file path: ")
authorization = input("Enter authorization token: ")
server = input("Enter server URL: ")
b_flag = input("Include -b flag? (y/n): ").lower() == "y"
k_flag = input("Include -k flag? (y/n): ").lower() == "y"

# Construct command
command = ["cats", "--contract={}".format(contract), "-H", "Authorization={}".format(authorization), "--server={}".format(server)]
if b_flag:
    command.append("-b")
if k_flag:
    command.append("-k")

# Execute command
subprocess.run(command)