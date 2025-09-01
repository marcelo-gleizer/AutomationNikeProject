import time

from jb_60.nike_project.pages.buy_product_page import landingPage


class TestBuyProduct():

    def test_find_product(self, setup_nike):
        print("Test Start")
        page = setup_nike
        landing_page = landingPage(page)
        landing_page.test_find_product()
        assert page.url == "https://www.nike.com/il/w/boys-road-running-shoes-1onraz3qxw3zy7ok", "url not correct"

    def test_add_product_to_bag(self, setup_nike):
        print("Test Start")
        page = setup_nike
        landing_page = landingPage(page)
        landing_page.test_add_product_to_bag()
        print("Test end")
        assert page.url == "https://www.nike.com/il/t/pegasus-road-running-shoes-0K269H/II6308-600", "url not correct"


