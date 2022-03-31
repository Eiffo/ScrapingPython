from requests import get
from bs4 import BeautifulSoup
import csv

# Enter to web browser
headers = {
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    }

f = open("links.csv", 'w', newline='') # open file with links
links = csv.writer(f)
lines = open('keywords.txt', 'r')

for line in lines:
    line = line.strip()
    URL = f'http://google.com/search?q=site:searchenginejournal.com/%20{line}' # URL adress
    page = get(URL, headers=headers) # Connecting to URL addresses

    if page.status_code == 200: # if status == 200 that means request was successful
        bs = BeautifulSoup(page.content, "html.parser") # Using BS to parse and scrape
        results = []
        numb = 0
        for f in bs.find_all('div', class_="yuRUbf"): # Looping through every adresses to find and save URL
            numb += 1
            search = f.find_all('a')
            if search:
                link = search[0]['href']
                item = {
                    "link": link
                }
                results.append(item)
                links.writerow(results) # Save link to .csv doc
        # Save everything to files
        file = open("results.txt", 'a')
        file.write(f"Keyword: {line}\n")
        file.write(f"Total number of results: {str(numb)}\n")
        file.close()