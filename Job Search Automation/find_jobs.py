from bs4 import BeautifulSoup
import webbrowser
import requests
import re

# Get keyword to search from the user
# keyword = input("Enter job keyword to search:")
keyword = 'aws'

class Indeed:
    def __init__(self, keyword):
        self.url = f'https://ph.indeed.com/jobs?q={keyword}&l=Philippines&sc=0kf%3Ajt(new_grad)%3B&sort=date&start='
        
            
    def openUrl(self):
        webbrowser.open(self.url)

    def jobTotal(self, soup):
        spans = soup.find_all("span", attrs={'class': None})
        print(spans)
        
        for list in enumerate(spans):
            print(list)
            # print(re.findall('\d', list))
            

    def scrapePage(self):
        scrapePage = requests.get(self.url)
        soup = BeautifulSoup(scrapePage.text, "lxml")
        self.jobTotal(soup)


aws = Indeed(keyword)
aws.scrapePage()