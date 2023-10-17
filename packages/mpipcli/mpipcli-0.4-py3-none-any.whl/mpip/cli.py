import argparse
import requests
import os

# MPIP_URL = "http://127.0.0.1:8000/api"
MPIP_URL = "https://api.a2zai.in/api"
VERSION = "0.4"


ALLOWED_EXTENSION = ".mojopkg"
MAX_FILE_SIZE = 2 * 1024 * 1024


def valid_file(file_path):
    if os.path.getsize(file_path) > MAX_FILE_SIZE:
        print(f"File size exceeds the allowed limit of {MAX_FILE_SIZE} bytes")
        return False

    _, file_extension = os.path.splitext(file_path)
    if file_extension.lower() != ALLOWED_EXTENSION:
        print(f"Invalid file extension. Allowed extension is '{ALLOWED_EXTENSION}'")
        return False
    return True


def download_package(package_path):
    url = f"{MPIP_URL}/packages/{package_path}/download/"
    response = requests.get(url)
    if response.status_code == 200:
        with open(f"{package_path}.mojopkg", "wb") as f:
            f.write(response.content)
        print(f"{package_path} downloaded successfully.")
    else:
        print(f"Failed to download {package_path}.")


def upload_package(token=None, package_path=None, description=None, version=None):
    if not os.path.exists(package_path):
        print("File not found.")
        return None
    if not valid_file(package_path):
        print("Invalid file")
        return None
    files = {"package": open(package_path, "rb")}
    url = f"{MPIP_URL}/add-package/"

    headers = {"Authorization": f"Token {token}"}
    data = {
        "name": package_path.split(".")[0].split("/")[-1],
        "description": description,
        "version": 0.1,
    }

    response = requests.post(url, headers=headers, data=data, files=files)

    if response.status_code == 200:
        print("Package added to MPIP")
    else:
        print(f"Failed to upload package, {response.json().get('message')}")


def main():
    parser = argparse.ArgumentParser(description="mpip: A custom package manager.")
    parser.add_argument("command", choices=["get", "post"], help="Command to execute.")
    parser.add_argument("package_path", nargs="?", help="Name of the package.")
    parser.add_argument("-t", "--token", help="API token for authentication.")
    parser.add_argument("-d", "--description", help="Description of the package.")
    # parser.add_argument("-V", "--package_version", help="Package version number.")

    parser.add_argument(
        "-v", "--version", action="version", version=f"mpip version {VERSION}"
    )

    args = parser.parse_args()

    if args.command == "get":
        if args.package_path:
            download_package(args.package_path)
        else:
            print("Error: Package name missing.")

    elif args.command == "post":
        if not args.package_path:
            print("Error: Package path missing")
            return None
        if not args.description:
            print("Error: Package description missing")
            return None
        # if not args.package_version:
        #     print("Error: Package version missing")
        #     return None

        upload_package(
            args.token,
            args.package_path,
            args.description
            # args.package_version
        )

    else:
        print('Invalid command. Use "mpip get/post".')


if __name__ == "__main__":
    main()
