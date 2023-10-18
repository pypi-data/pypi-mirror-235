import click
import subprocess

@click.command()
def start():
    """Start your vm"""
    subprocess.run("gcloud compute instances start lewagon-data-eng-vm-mattrousseau")

@click.command()
def stop():
    """Stop your vm"""
    subprocess.run("gcloud compute instances stop lewagon-data-eng-vm-mattrousseau")

@click.command()
def connect():
    """Connect to your vm in vscode inside your ~/code/mattrousseau/folder """
    subprocess.run("code --folder-uri vscode-remote://ssh-remote+matthieurousseau86@35.246.76.175/home/matthieurousseau86/code/mattrousseau")
