
#
#
# class Test_Actions:
#     def setup_class(cls):
#         global driver
#         driver = webdriver.Chrome(ChromeDriverManager().install())
#         driver.maximize_window()
#         driver.get("https://atidcollege.co.il/Xamples/ex_actions.html")
#   @staticmethod
#       def teardown_class(cls):
#          driver.quit()
#
#     def test_1_drag_drop(self):
#         draggable = driver.find_element(By.ID ,"draggable")
#         droppable = driver.find_element(By.ID ,"droppable")
#         action = ActionChains(driver)
#         action.drag_and_drop(draggable, droppable).perform()
#         time.sleep(1)
#
#     def test_2_select_miltiple(self):
#         list1 = driver.find_element(By.XPATH ,"//ol[@id='select_items']/li")
#         action = ActionChains(driver)
#         action.click_and_hold(list1[0]).click_and_hold(list1[1]).perform()
#         time.sleep(1)
#
#     def test_3_double_click(self):
#         double_click_element = driver.find_element(By.ID ,"dbl_click")
#         action = ActionChains(driver)
#         action.double_click(double_click_element).perform()
#         time.sleep(1)
#         exp_result = "Hello World"
#         act_result = driver.find_element(By.ID,"demo").text
#         assert exp_result == act_result
#
#     def test_4_mouse_hover(self):
#         element = driver.find_element(By.ID,"mouse_hover")
#         action = ActionChains(driver)
#         action.move_to_element(element).perform()
#         time.sleep(1)
#         bgcolor = "background-color: rgb(255, 255, 0);"
#         driver.find_element(By.CSS_SELECTOR ,"span[style='" + bgcolor + "']").is_displayed()
#
#     def test_5_scroll(self):
#         driver.execute_script("window.scrollBy(0, 600);")
#         time.sleep(1)
#         exp_result = "This Element is Shown When Scrolled"
#         act_result = driver.find_element(By.ID ,"scrolled_element").text
#         assert exp_result == act_result