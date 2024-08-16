from bs4 import BeautifulSoup
import webbrowser

# Get keyword to search from the user
keyword = input("Enter job keyword to search:")

class Indeed:
    def __init__(self, keyword):
        self.url = f'https://ph.indeed.com/jobs?q={keyword}&l=Philippines'

            
    def openUrl(self):
        webbrowser.open(self.url)


aws = Indeed(keyword)
aws.openUrl()
