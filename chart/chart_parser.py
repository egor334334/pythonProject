import requests
from bs4 import BeautifulSoup

URL=r'https://www.last.fm/charts'

class Parser:
    def __init__(self):
        self.session=requests.Session()

    def get_chart(self):
        response=self.session.get(URL)
        return response.text

    @staticmethod
    def _parse_chart(songs: list, autors: list):
        response = []
        for song, author in zip(songs, autors):
            data = {'song': song.string, 'author': author.string}
            response.append(data)
        return response

    def parse_chart(self):
        content=self.get_chart()
        soup=BeautifulSoup(content, 'html.parser')
        song_class='link-block-target'
        author_class='globalchart-track-artist-name'
        songs=soup.find_all('a', {'class':song_class})
        authors = soup.find_all('td', {'class': author_class})
        return self._parse_chart(songs, authors)

