import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager


class Test_Exm:
    @classmethod
    def setup_class(cls):
        # First
        global  price, Fname, Lname,driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.maximize_window()
        driver.get("https://atidcollege.co.il/Xamples/pizza/")
        price= driver.find_element(By.CSS_SELECTOR, "span[class='ginput_total ginput_total_5']")
        Fname = "qusai"
        Lname = "trabeh"

    def teardown_class(cls):
        driver.quit()
    @allure.step("checking")
    def test_VerifyDefaultPrice(self):
        assert price.text == "$7.50"
    @allure.step("Verify with Delivery")
    def test_VerifyPriceWithDeliveryOption(self):
        # Selecting Delivery Option
        Delivery = Select(driver.find_element(By.ID, "input_5_21"))
        Delivery.select_by_visible_text("Delivery +$3.00")
        # Printing Price after Selecting Delivery
        print("Price After Delivery:", driver.find_element(By.CSS_SELECTOR, "span[class='ginput_total ginput_total_5']").text)
        assert driver.find_element(By.CSS_SELECTOR, "span[class='ginput_total ginput_total_5']").text == "$10.50"

    @pytest.mark.depends(on=['test_VerifyPriceWithDeliveryOption'])
    def test_Alert(self):
        # Sending Information
        driver.find_element(By.ID, "input_5_22_3").send_keys(Fname)
        driver.find_element(By.ID, "input_5_22_6").send_keys(Lname)
        # iFrame
        _iframe = driver.find_element(By.CSS_SELECTOR, "iframe[src='coupon.html']")
        driver.switch_to.frame(_iframe)
        coupon = driver.find_element(By.ID, "coupon_Number").text
        driver.switch_to.default_content()
        driver.find_element(By.ID, "input_5_20").send_keys(coupon)
        driver.find_element(By.ID, "gform_submit_button_5").click()
        # Alert Validation
        Alert = driver.switch_to.alert
        popup_text = Alert.text
        print("Alert:", popup_text)
        Alert.accept()
        Expected = Fname + " " + Lname + " " + coupon
        print(popup_text)
        # Assert on The Popup Massege
        assert popup_text == Expected

        def attach_file(self):
            image = "./screen-shots/screen.png"  # need to create folder: screen-shot first
            driver.get_screenshot_as_file(image)
            allure.attach.file(image, attachment_type=allure.attachment_type.PNG)
