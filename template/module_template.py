# Cloud flare
# import cfscrape
# import requests.exceptions

# No cloudflare
import requests

from bs4 import BeautifulSoup
from ..decorators import request_exception_handler


class ClassName:
    def __init__(self, link, directory):
        self.session = requests.Session()
        self.site = "site.com"
        self.folder = directory
        self.manga_link = link
        self.base_link = "https://site.com"
        self.cover_url = None
        self.chapters = {}

    @property
    def manga_dir(self):
        return self.folder / self.series_title

    def __bool__(self):
        return True

    def __len__(self):
        return len(self.chapters)

    @request_exception_handler
    def get_main(self, title_return=False):
        '''
        Gets the main manga info like title, cover url and chapter links
        title_return=True will only get the title and return
        '''
        r = self.session.get(self.manga_link, timeout=5)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        self.cover_url = "get cover here"

        self.series_title = "find title"
        if title_return:
            return True

        self.data = "finding all chapter links in the soup"
        return True

    def get_chapters(self):
        '''
        Handles the chapter data by assigning chapter numbers
        '''
        for chapter in self.data:

            num = "finding chapter number in soup"
            try:
                num = int(num)
            except ValueError:
                num = float(num)
            link = "finding chapter link in soup"

            self.chapters[num] = {"link": link,
                                  "title": None}
        return True

    @request_exception_handler
    def get_info(self, ch):
        '''Gets the needed data abut the chapters from the site'''
        link = self.chapters[ch]["link"]

        r = self.session.get(link, timeout=5)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "html.parser")

        pages = ["list of found image links"]

        self.chapters[ch]["pages"] = pages
        return True
