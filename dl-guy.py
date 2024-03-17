#!/usr/bin/env python3
import os
import sys
import subprocess
import urllib.request
from urllib.parse import urlparse

def print_help():
    print("Usage: dl-guy <command> [<args>]")
    print("\nCommands:")
    print("  --dl <url>        Download a file from a URL")
    print("  --setup           Setup dl-guy")
    print("  --update          Update dl-guy")
    print("  --info            Display information about dl-guy")
    print("  --version         Display the version of dl-guy")
    print("  --help            Display this help message")

def download_file(url):
    try:
        parsed_url = urlparse(url)
        filename = parsed_url.path.split('/')[-1]
        urllib.request.urlretrieve(url, filename)
        print(f"Download {filename} erfolgreich")
    except Exception as e:
        print(f"Fehler beim Herunterladen: {e}")

def main():
    script_dir = "/usr/share/dl-guy/src"
    if not os.path.isdir(script_dir):
        print(f"The Path {script_dir} does not exist")
        return

    if len(sys.argv) < 2 or sys.argv[1] == "--help":
        print_help()
        return

    if sys.argv[1] == "--dl":
        if len(sys.argv) < 3:
            print("Please provide a URL after --dl.")
            return
        else:
            url = sys.argv[2]
            download_file(url)
            return

    if sys.argv[1] == "--setup":
        setup_script_path = os.path.join(script_dir, "setup.py")
        if not os.path.isfile(setup_script_path):
            print("The setup.py script is not found.")
            return
        subprocess.run(["python3", setup_script_path])
        return

    # Handling other commands
    if sys.argv[1] == "--update":
        # Update command
        return
    elif sys.argv[1] == "--info":
        # Info command
        return
    elif sys.argv[1] == "--version":
        # Version command
        return
    else:
        print("Unknown command. Use --help for usage instructions.")
        return

if __name__ == "__main__":
    main()
