import requests
import api_test.schema.schemes as scheme
from jsonschema import validate


class ModuelPage(object):

    def __init__(self):
        self.host = 'http://guidedev01z1.o3.ru/v0/'
        self.menu = 'getmenu'

    def menu(self):
        return self.host + self.menu


class TestPage(ModuelPage):

    def __init__(self):
        super().__init__()

    def getJsonMenu(self):
        link = self.host + self.menu
        r = requests.options(link)
        result = r.json()
        return result


class TestHeader(ModuelPage):

    def __init__(self):
        super().__init__()

    def statusMenu(self):
        link = self.host + self.menu
        r = requests.options(link)
        if r.status_code == 200:
            return True
        else:
            return False

    def statusLink(self, link):
        link = self.host + link
        r = requests.options(link)
        if r.status_code == 200:
            return True
        else:
            return False


class TestJsonScheme(ModuelPage):

    def __init__(self):
        super().__init__()

    def validateMenu(self):
        link = self.host + self.menu

        r = requests.options(link)
        json_response = r.json()
        json_scheme = scheme.menu

        error = validate(json_response, json_scheme)

        if error is None:
            return True

    def validateCategory(self, link):
        link = link.replace("/", "")
        link = link + '/'
        url = self.host + link
        r = requests.options(url)
        json_response = r.json()
        json_scheme = scheme.categories

        error = validate(json_response, json_scheme)

        if error is None:
            return True
