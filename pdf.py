import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def download_file(url, folder_path):
    response = requests.get(url,verify=True)
    if response.status_code == 200:
        file_name = url.split("/")[-1]
        file_path = os.path.join(folder_path, file_name)
        try:
            with open(file_path, 'wb') as f:
                f.write(response.content)
        except OSError as oserr:
            print("error in downloading file")




        print(f"Downloaded: {file_name}")
        return file_path
    else:
        print(f"Failed to download: {url}")
        return None

def scrape_and_download(url, folder_path):
    try:
        grab = requests.get(url,verify=True)
        soup = BeautifulSoup(grab.text, 'html.parser')

        for link in soup.find_all("a"):
            href = link.get("href")
            if href:
                absolute_url = urljoin(url, href)
                lower_url = absolute_url.lower()

                if any(extension in lower_url for extension in ['.pdf', '.docx', '.doc', '.txt', '.ppt', '.pptx']):
                    download_file(absolute_url, folder_path)
                else:
                    with open("non_downloadable_links.txt", "a") as non_dl_file:
                        non_dl_file.write(absolute_url + "\n")
    except requests.exceptions.RequestException as e:
        print('error in ',url)

