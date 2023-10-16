import click
import subprocess

@click.command()
def start():
    """Start your vm"""
    vm_zone = "europe-west2-c"  # Replace with your VM's zone
    vm_name = "lewagon-data-eng-vm-tomasromeiro"  # Replace with your VM's name

    start_command = f"gcloud compute instances start --zone={vm_zone} {vm_name}"
    subprocess.run(start_command, shell=True)

@click.command()
def stop():
    """Stop your vm"""
    vm_zone = "europe-west2-c"  # Replace with your VM's zone
    vm_name = "lewagon-data-eng-vm-tomasromeiro"  # Replace with your VM's name

    stop_command = f"gcloud compute instances stop --zone={vm_zone} {vm_name}"
    subprocess.run(stop_command, shell=True)

@click.command()
def connect():
    """Connect to your vm in vscode inside your ~/code/tomasromeiro/folder """
    # your code here
    vm_ip = "35.246.100.158 "  # Replace with your VM's IP address
    path_inside_vm = "/code/tomasromeiro/folder"  # Replace with the desired path inside the VM

    connect_command = f"code --folder-uri vscode-remote://ssh-remote+username@{vm_ip}/{path_inside_vm}"
    subprocess.run(connect_command, shell=True)
