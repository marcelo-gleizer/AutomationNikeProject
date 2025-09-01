import time


class findStore():

    def __init__(self , page):
        print("into init")
        self.page = page

    def go_to_find_store_page(self):
        print("start go to find store page test")
        find_store_button = self.page.locator("[href='https://www.nike.com/il/retail']")
        find_store_button.click()


    def test_find_store_near_me(self):
        time.sleep(15)
        #store_near_me = self.page.locator("[class='pt6-sm pl8-sm pb6-sm pr7-sm border-bottom u-cursor-pointer']").all()
        store_near_me = self.page.locator("[class*='pt6-sm pl8-sm']").all()
        print(f" stores: {len(store_near_me)}")
        print(f"store near me: {store_near_me[0].text_content()}")


    def test_find_store_in_london(self):

        search_location = self.page.locator("[id='ta-Location_input']")
        search_location.fill("London")
        time.sleep(5)
        self.page.keyboard.press("Enter")
        time.sleep(15)
        store_by_location = self.page.locator("[class*='pt6-sm pl8-sm']").all()
        print(f"store: {len(store_by_location)}")
        store_by_location_text = store_by_location[0].text_content()
        print(f"store in london: {store_by_location_text}")

