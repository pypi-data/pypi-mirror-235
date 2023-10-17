import click
import subprocess

#@click,comman() defines a function as a command in the CLI application. I am telling click that this function should be treated as a command, and it can be invoked from the command line
@click.command()
def start():
    """Start your vm"""
    start_command = "gcloud compute instances start --zone=europe-west1-b lewagon-data-eng-vm-verdi92"
    # Run the (external) command in the shell.
    subprocess.run(start_command, shell=True)

@click.command()
def stop():
    """Stop your vm"""
    stop_command = "gcloud compute instances stop --zone=europe-west1-b lewagon-data-eng-vm-verdi92"
    subprocess.run(stop_command, shell=True)

@click.command()
def connect():
    """Connect to your vm in vscode inside your ~/code/verdi92/folder """
    connect_command = "code --folder-uri vscode-remote://ssh-remote+verdianameloni@34.79.92.66/code/verdi92/"
    subprocess.run(connect_command, shell=True)

if __name__ == '__main__':
    # Run the 'start', 'stop', and 'connect' functions when the script is executed
    start()  # Starts the VM
    stop()   # Stops the VM
    connect() # Connects the VM
