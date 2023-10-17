import click
import subprocess

@click.command()
def start():
    """Start your vm"""
    subprocess.run(["gcloud", "compute", "instances", "start", "--zone=europe-west1-b", "lewagon-data-eng-vm"])

@click.command()
def stop():
    """Stop your vm"""
    subprocess.run(["gcloud", "compute", "instances", "stop", "--zone=europe-west1-b", "lewagon-data-eng-vm"])

@click.command()
def connect():
    """Connect to your vm in vscode inside your ~/code/<user.lower_github_nickname>/folder """
    subprocess.run(["code", "--folder-uri", "vscode-remote://ssh-remote+mitya@34.78.101.51/home/mitya/code/selectcoma/"])
