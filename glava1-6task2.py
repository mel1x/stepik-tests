import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "http://suninjuly.github.io/find_link_text"

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=options)

try:
    wait = WebDriverWait(browser, 15)
    browser.get(link)

    text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    browser.find_element(By.LINK_TEXT, text).click()

    browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    alert = wait.until(EC.alert_is_present())
    print(alert.text.split()[-1])
finally:
    browser.quit()
