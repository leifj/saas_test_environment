from selenium import webdriver

__author__ = 'danielevertsson'


class TestSaaS:
    def test_login_to_idp_1(self):
        driver = webdriver.Firefox()
        driver.get("http://127.0.0.1:9087")
        driver.find_element_by_id("to_list").click()

        dropdown = driver.find_element_by_id("thelist")
        for option in dropdown.find_elements_by_tag_name('option'):
            if option.text == "My IDP NO.1":
                option.click()
                break

        driver.find_element_by_id("proceed").click()
        driver.find_element_by_name("login").clear()
        driver.find_element_by_name("login").send_keys("roland")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("dianakra")
        driver.find_element_by_name("form.submitted").click()
        display_name_cell = driver.find_elements_by_xpath('/html/body/table/tbody/tr[1]/td')
        assert display_name_cell[0].text == "P. Roland Hedberg"