import tkinter as tk
from tkinter import filedialog
import subprocess

# Create the Tkinter app
app = tk.Tk()
app.title("CATS")

# Define function to execute command
def execute_command():
    # Get user inputs
    contract = contract_entry.get()
    authorization = auth_entry.get()
    server = server_entry.get()
    b_flag = b_var.get()
    k_flag = k_var.get()

    # Construct command
    command = ["cats", "--contract={}".format(contract), "-H", "Authorization={}".format(
        authorization), "--server={}".format(server)]
    if b_flag:
        command.append("-b")
    if k_flag:
        command.append("-k")

    # Open terminal window and execute command
    subprocess.Popen(['gnome-terminal', '-x'] + command)

# Define function to select contract file
def select_contract():
    contract_file = filedialog.askopenfilename()
    contract_entry.delete(0, tk.END)
    contract_entry.insert(0, contract_file)

# Create contract label and entry
contract_label = tk.Label(app, text="Contract File:")
contract_label.pack(side=tk.TOP)
contract_entry = tk.Entry(app)
contract_entry.pack(side=tk.TOP)
contract_button = tk.Button(app, text="Select contract", command=select_contract)
contract_button.pack(side=tk.TOP)

# Create authorization label and entry
auth_label = tk.Label(app, text="Authorization Token:")
auth_label.pack()
auth_entry = tk.Entry(app)
auth_entry.pack()

# Create server label and entry
server_label = tk.Label(app, text="Server URL:")
server_label.pack()
server_entry = tk.Entry(app)
server_entry.pack()

# Create checkboxes for flags
b_var = tk.BooleanVar()
b_checkbox = tk.Checkbutton(app, text="-b flag", variable=b_var)
b_checkbox.pack()
k_var = tk.BooleanVar()
k_checkbox = tk.Checkbutton(app, text="-k flag", variable=k_var)
k_checkbox.pack()

# Create button to execute command
execute_button = tk.Button(app, text="Execute", command=execute_command)
execute_button.pack()

# Start the Tkinter event loop
app.mainloop()
