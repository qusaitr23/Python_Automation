import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from webdriver_manager.chrome import ChromeDriverManager


class Test_HoodieShop:
    @classmethod
    def setup_class(cls):

        global driver, price_average
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://thegithubshop.com/")
        driver.implicitly_wait(5)
        price_average = "$10.00"

    def test_SearchingHoodie(self):
        search_box = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[3]/div[1]/form/input")
        search_box.click()
        search_box.send_keys("Hoodie")
        search_box.send_keys(Keys.ENTER)

    def test_CheckPrice(self):
        prices = driver.find_elements(By.CSS_SELECTOR, "span[class='product-thumbnail__price__cost']")
        for i in range(len(prices)):

            if (prices[i].text != price_average):
                pass
            else:
                AssertionError : print("Error")


    def test_Invertocat_Hoodie_Click(self):
        Hoodie = driver.find_element(By.CSS_SELECTOR, "h3[class='product-thumbnail__title']")
        Hoodie.click()
        Quantity = driver.find_element(By.CSS_SELECTOR, "input[type='number']").get_attribute("value")
        assert int(Quantity) == 1

    def teardown_class(cls):
        driver.quit()
