import requests
from bs4 import BeautifulSoup

from compumedic.services.ProductDataScrapperService import IScrapperQuery, ProductScrapped


class FarmaciaUniversalQueryImp(IScrapperQuery):
    url = None
    query = None

    def __init__(self, query="acetaminofen"):
        super().__init__(query)
        self.query = query

    def execute_query(self):
        import requests
        url = "https://farmaciauniversal.com/buscador"
        querystring = {"term": self.query}

        payload = ""
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/116.0.0.0 Safari/537.36"}
        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        self.url = "http://farmaciauniversal.com/" + response.json()[0].get('url')
        pass

    def get_result(self) -> ProductScrapped:
        print("scrapping > " + self.url)
        html_content = requests.get(self.url).content
        soup = BeautifulSoup(html_content, 'html.parser')
        title = soup.find("meta", property="og:title")
        img = soup.find("meta", property="og:image")
        price = soup.findAll('p', {'class': 'texto azul precio izquierda talla25 em4'})[0].get_text().replace('S/', '')
        return ProductScrapped(name=title["content"], price=price, store_id=6, photo=img)
