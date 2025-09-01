class landingPage():

    def __init__(self , page):
        print("into init")
        self.page = page

    def test_find_product(self):
        print("Test Start")
        shop_button = self.page.get_by_role("link", name="Pegasus. Vomero. Structure. More Choice. More Running.")
        shop_button.click()
        kids_button = self.page.locator("div.trigger-content__label").filter(has_text="Kids")
        kids_button.click()
        filter_by_boys = self.page.get_by_role("checkbox", name="Filter for Boys")
        filter_by_boys.click()

    def test_add_product_to_bag(self):
        print("Test Start")
        men_category_button = self.page.get_by_text("Men", exact=True)
        men_category_button.click()
        shoes_category_button = self.page.get_by_role("link", name="Shoes")
        shoes_category_button.click()
        running_shoes_button = self.page.get_by_alt_text("Nike Pegasus Premium Men's Road Running Shoes")
        running_shoes_button.click()
        size_shoes_button = self.page.locator('label[for="grid-selector-input-15"]')
        size_shoes_button.click()
        add_to_bag_button = self.page.get_by_role("button", name="Add to Bag")
        add_to_bag_button.click()

