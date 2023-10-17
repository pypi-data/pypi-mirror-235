import click
import subprocess

@click.command()
def start():
    """Start your vm"""
    subprocess.run(["gcloud", "compute" , "instances", "start",
                "lewagon-data-eng-vm-mariamillet"])

@click.command()
def stop():
    """Stop your vm"""
    subprocess.run(["gcloud", "compute" , "instances", "stop",
                "lewagon-data-eng-vm-mariamillet"])

@click.command()
def connect():
    """Connect to your vm in vscode inside your ~/code/mariamillet/folder """
    subprocess.run(["code", "--folder-uri",
        "vscode-remote://ssh-remote+m.kosyuchenko@35.195.197.115/home/m.kosyuchenko/code/MariaMillet"])
