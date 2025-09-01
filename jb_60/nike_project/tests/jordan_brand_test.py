import time

from jb_60.nike_project.pages.jordan_brand_page import jordanPage


class TestNikeJordan():

    def test_find_jordan_product(self, setup_nike):
        print("Test find jordan product Start")
        page = setup_nike
        jordan_page = jordanPage(page)
        jordan_page.go_to_air_jordan()
        jordan_page.find_jordan_shoes()
        assert page.url=="https://www.nike.com/il/t/jordan-flight-chicago-corduroy-trousers-DFszLS/HV0526-010","url not correct"

    def test_jordan_fleece_by_price(self, setup_nike):
        print("Test jordan product by price Start")
        page = setup_nike
        jordan_page = jordanPage(page)
        jordan_page.go_to_air_jordan()
        jordan_page.find_jordan_fleece_by_price()
        assert page.url == "https://www.nike.com/il/t/jordan-rare-air-fleece-pullover-hoodie-48nf2X/IB3003-673", "url not correct"