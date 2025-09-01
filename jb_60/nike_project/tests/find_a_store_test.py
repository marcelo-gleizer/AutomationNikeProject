import time

from jb_60.nike_project.pages.find_a_store_page import findStore


class TestNikeLocation():

    def test_find_store(self, setup_nike):
        page = setup_nike
        find_a_store_page = findStore(page)
        find_a_store_page.go_to_find_store_page()
        find_a_store_page.test_find_store_near_me()
        assert page.url == "https://www.nike.com/il/retail", "url not correct"

    def test_find_store_in_london(self, setup_nike):
        page = setup_nike
        find_a_store_page = findStore(page)
        find_a_store_page.go_to_find_store_page()
        find_a_store_page.test_find_store_in_london()
        assert page.url == "https://www.nike.com/il/retail", "url not correct"
