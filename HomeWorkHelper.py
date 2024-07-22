import requests
from bs4 import BeautifulSoup
import urllib.parse

class HomeWorkHelper:
    def __init__(self):
        self.brainly_links = []

    def get_brainly_links(self, question, repeats):
        self.question = "brainly " + str(question)
        self.url = "https://www.bing.com/search?q=" + urllib.parse.quote(self.question)
        self.repeats = repeats

        for _ in range(self.repeats):
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')

            for link in links:
                href = link.get('href')
                if href and 'brainly.com/question/' in href and href not in self.brainly_links:
                    self.brainly_links.append(href)
        
        links = self.brainly_links
        self.brainly_links = []
        return links

# Example usage:
helper = HomeWorkHelper()
result = helper.get_brainly_links("Pythagorean theorem", 1)
print(result)
