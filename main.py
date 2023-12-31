import requests
from bs4 import BeautifulSoup
import csv
from pdf import scrape_and_download
import os

links = [
    "https://ukmt.org.uk/current-past-papers/jsf/jet-engine:free-past-papers/tax/challenge-type:70/",
    "https://bmos.ukmt.org.uk/home/bmo.shtml"
]

for row in links:
    website = row.strip("/")
    if website.startswith("http://") or website.startswith("www.") or website.startswith("https://"):
            # print(website)

            # pass
        try:
            grab = requests.get(website, verify=False)
            soup = BeautifulSoup(grab.text, 'html.parser')

                # Extract all links
        except requests.exceptions.RequestException as e:
            print('error in ', website)
        links = [link.get('href') for link in soup.find_all("a")]

        for link in links:
            if link and not link.startswith("#") and not link.startswith("http://") and not link.startswith(
                        "https://") and not link.startswith("mailto:"):
                root_folder = 'uk'
                website_url = website + '/' + link.strip("/")
                print("downloading from " + website_url)
                if not os.path.exists(root_folder):
                    os.makedirs(root_folder)
                output_folder = root_folder + "/" + website.strip("https://")
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)
                scrape_and_download(website_url, output_folder)





    else:
        print("website not in ", website)
