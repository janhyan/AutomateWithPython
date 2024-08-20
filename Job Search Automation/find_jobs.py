from bs4 import BeautifulSoup
import webbrowser
import requests
import re

# Get keyword to search from the user
# keyword = input("Enter job keyword to search:")
keyword = "aws"
headers = {
    "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}


class Indeed:
    def __init__(self, keyword):
        self.url = f"https://www.glassdoor.com/Job/philippines-aws-jobs-SRCH_IL.0,11_IN204_KO12,15.htm?seniorityType=entrylevel&remoteWorkType=1"

    def openUrl(self):
        webbrowser.open(self.url)

    def jobTotal(self, soup):
        spans = soup.find_all("span", attrs={"class": None})
        print(spans)

        for list in enumerate(spans):
            print(list)
            # print(re.findall('\d', list))

    def scrapePage(self):
        scrapePage = requests.get(self.url, headers)
        soup = BeautifulSoup(scrapePage.text, "lxml")
        self.jobTotal(soup)


aws = Indeed(keyword)
aws.scrapePage()
