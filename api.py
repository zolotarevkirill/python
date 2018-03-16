import pytest
import json
from api_test.module.module_page import TestHeader
from api_test.module.module_page import TestJsonScheme
from api_test.module.module_page import TestPage


class Test:

    @pytest.fixture(scope="session")
    def driver(self):
        pass
        #yield webdriver.Chrome()

    def test_menu(self):
        header = TestHeader()
        scheme = TestJsonScheme()
        page = TestPage()

        assert header.statusMenu()
        assert scheme.validateMenu()

        jsonMenu = page.getJsonMenu()

        parsed_string = json.loads(str(jsonMenu['content']).replace("'", "\""))

        if len(parsed_string) > 0:

            for item in parsed_string:
                link = item['link']
                assert header.statusLink(link)
        else:
            return False

    def test_category(self):
        page = TestPage()
        scheme = TestJsonScheme()
        jsonMenu = page.getJsonMenu()

        parsed_string = json.loads(str(jsonMenu['content']).replace("'", "\""))

        if len(parsed_string) > 0:
            for item in parsed_string:
                link = item['link']
                assert scheme.validateCategory(link)

        else:
            return False
