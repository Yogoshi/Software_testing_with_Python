from selenium import webdriver
import time
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/wait1.html")
    browser.implicitly_wait(5)

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

    browser.get("http://suninjuly.github.io/cats.html")
    browser.find_element_by_id("button")

finally:
    time.sleep(5)
    browser.quit()