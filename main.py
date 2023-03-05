import subprocess

# Prompt user for arguments
contract = input("Enter contract file path: ")
authorization = input("Enter authorization token: ")
server = input("Enter server URL: ")
b_flag = input("Include -b flag? (y/n): ").lower() == "y"
k_flag = input("Include -k flag? (y/n): ").lower() == "y"

# Construct command
command = ["cats", "--contract={}".format(contract), "-H", "Authorization={}".format(
    authorization), "--server={}".format(server)]
if b_flag:
    command.append("-b")
if k_flag:
    command.append("-k")

# Execute command
subprocess.run(command)

# cats --contract=openapi.yml -H "Authorization=?????" --server=https://openai.com/api -b -k
