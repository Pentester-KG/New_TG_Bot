import httpx
from parsel import Selector


class HouseCrawler:
    MAIN_URL = "https://www.house.kg/snyat"
    BASE_URL = "https://www.house.kg"

    def get_page(self):
        response = httpx.get(self.MAIN_URL)
        self.page = response.text

    def get_title(self):
        html = Selector(self.page)
        title = html.css("title::text").get()
        return title

    def get_house_links(self):
        html = Selector(self.page)
        links = html.css(".title a::attr(href)").getall()
        full_links = list(map(lambda x: self.BASE_URL + x, links))
        return full_links[:5]


# def get_house_data():
#     crawler = HouseCrawler()
#     crawler.get_page()
#     title = crawler.get_title()
#     house_links = crawler.get_house_links()
#     return title, house_links
if __name__ == "__main__":
    crawler = HouseCrawler()
    def send_link():
        crawler.get_page()
        house_links = crawler.get_house_links()
        for link in house_links:
            print(f'Apartments in Bishkek: {link} ')




