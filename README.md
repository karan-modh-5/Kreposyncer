# Kreposyncer - GitHub Projects Downloader

This script allows you to automatically download all your GitHub project files from their respective repositories. It is specifically designed to work with repositories listed in a remote `README.md` file, where each repository is specified in a bullet point format.

## Features

- Fetches a remote `README.md` file containing a list of repositories.
- Parses the repository names from the `README.md` file.
- Generates URLs to download project files directly from the `main` branch.
- Downloads project files to the current working directory.
- Provides feedback for each download process.

## Prerequisites

- Python 3.x

## Required Python Modules

The script uses the following built-in Python modules:
- `os`
- `urllib.request`
- `requests`
- `http.client`
- `urllib.parse`

No external modules are required for this script.

## Setup Instructions

1. Clone or copy this script to your local machine.
2. Ensure you have Python 3.x installed.

## Usage

1. Edit the script to point to the correct remote `README.md` file by modifying the `url` variable:
   ```python
   url = "https://raw.githubusercontent.com/your-username/your-repo/refs/heads/main/README.md"
   ```
   Replace `your-username` and `your-repo` with the appropriate GitHub username and repository.

2. Run the script using the following command:
   ```bash
   python kproject-updater.py
   ```

3. The script will:
   - Fetch the remote `README.md` file.
   - Parse the project names from the file.
   - Generate download URLs for each project.
   - Download the respective `.py` files into the current working directory.

## Script Logic

1. Fetches the remote `README.md` file using the provided URL.
2. Parses the file to extract lines starting with a dash (`-`) to identify project names.
3. Generates download URLs for each project based on a consistent naming convention.
4. Downloads the project files using `urlretrieve`.
5. Saves each file to the current script directory.

## Example Output

- Displays the generated URLs for each project.
- Confirms successful download or reports errors for individual files.

Example:
```bash
project1 : https://raw.githubusercontent.com/username/project1/refs/heads/main/project1.py
Downloaded project1.py successfully!

project2 : https://raw.githubusercontent.com/username/project2/refs/heads/main/project2.py
Downloaded project2.py successfully!

All Projects Are Updated.
```

## Limitations

- Assumes all repositories use the same naming convention for their `.py` files (i.e., `<repository_name>.py`).
- Relies on the structure and format of the remote `README.md` file.

## Customization

To customize the script:
1. Modify the `url` variable to point to your own `README.md` file.
2. Update the `generate_urls` function if your project file naming conventions differ.
