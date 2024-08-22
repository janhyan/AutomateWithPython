from bs4 import BeautifulSoup
import requests
import random

headers = {
    "User-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}

class Category:
    def __init__(self) -> None:
        self.categoryUrl = "https://github.com/public-apis/public-apis"
        self.scrapeCategory = requests.get(self.categoryUrl, headers)
        self.soup = BeautifulSoup(self.scrapeCategory.text, 'lxml')

    def listCategories(self):
        self.finalList = []

        for target in self.soup.find_all("tr"):
            self.categoriesList = target.find_all("a")
            for target in self.categoriesList:
                self.finalList.append(target.text)
        
        return self.finalList
            

    def chooseRandom(self, list):
        random.shuffle(list)
        print(list[0])

tmp = Category()
tmp.chooseRandom(tmp.listCategories())
        