import requests
from bs4 import BeautifulSoup


class solution:
    

    def get(self, currency_name):
        p = requests.get(
            "https://google.com/search?q=site%3Acoinmarketcap.com+" + currency_name + "&ie=utf-8&oe=utf-8")
        soup = BeautifulSoup(p.content, 'html.parser')
        return soup.find_all("h3")


a = solution()
l = a.get("bitcoin")

for i in l:
    print(i.find("div").get_text())