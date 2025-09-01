from datetime import time


class jordanPage():

    def __init__(self , page):
        print("into init")
        self.page = page

    def go_to_air_jordan(self):
        print("start go to air jordan test")
        air_jordan_button = self.page.locator("[href='https://www.nike.com/il/jordan']")
        air_jordan_button.click()

    def find_jordan_shoes(self):
        find_releases_button = self.page.locator("[href='https://www.nike.com/il/w/new-jordan-37eefz3n82y']")
        find_releases_button.click()
        find_jordan_shoes = self.page.locator('a[aria-label="Jordan Flight Chicago"]')
        find_jordan_shoes.click()

    def find_jordan_fleece_by_price(self):
        find_releases_button = self.page.locator("[href='https://www.nike.com/il/w/new-jordan-37eefz3n82y']")
        find_releases_button.click()
        filter_by_price = self.page.get_by_role("button", name="Shop By Price")
        filter_by_price.click()
        price_option = self.page.get_by_role("checkbox", name="Filter for ₪ 519.9 - ₪ 709.9")
        price_option.click()
        choose_shoes_button = self.page.locator('a[aria-label="Jordan Rare Air"]')
        choose_shoes_button.click()
        choose_color_button = self.page.locator("[href='/il/t/jordan-rare-air-fleece-pullover-hoodie-48nf2X/IB3003-673']")
        choose_color_button.click()
        choose_size_button = self.page.locator('div[data-testid="pdp-grid-selector-item"] >> label[for="grid-selector-input-M"]')
        choose_size_button.click()
        add_to_bag = self.page.get_by_role("button", name="Add to Bag")
        add_to_bag.click()
