import os
from urllib.request import urlretrieve
import requests
import http.client
import urllib.parse

# URL to be loaded
url = "https://raw.githubusercontent.com/karan-modh-5/karan-modh-5/refs/heads/main/README.md"

# Send a GET request to the URL
response = requests.get(url)

# Parse the URL
parsed_url = urllib.parse.urlparse(url)

# Create an HTTPS connection
conn = http.client.HTTPSConnection(parsed_url.netloc)

# Send a GET request
conn.request("GET", parsed_url.path)

# Get the response
response = conn.getresponse()

# Read the content
content = response.read()

# Print the content
data = content.decode('utf-8')

# Close the connection
conn.close()

# Extract lines starting with '-'
lines = data.split('\n')
project_names = [line for line in lines if line.startswith('-')]

projects = []
# Print the extracted project names
for project in project_names:
    line = project.split('- ')[1]
    project_part = line.split(':')[0]
    projects.append(project_part.lower())

#print(projects)

def download_file(url):
    script_directory = os.getcwd()  # Get the current script directory
    filename = url.split('/')[-1]  # Extract the filename from the URL
    file_path = os.path.join(script_directory, filename)
    try:
        urlretrieve(project_url, file_path)
        print(f"Downloaded {filename} successfully!")
    except Exception as e:
        print(f"Error downloading {filename}: {e}")

def generate_urls(project):
    return f"https://raw.githubusercontent.com/karan-modh-5/{project}/refs/heads/main/{project}.py"

# Download content for each URL using curl
for project in projects:
    project_url = generate_urls(project)
    print("\n",project, ": ", end="")
    print(project_url)
    download_file(project_url)

print("\nAll Projects Are Updated.")
