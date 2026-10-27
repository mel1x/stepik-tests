from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=options)

try:
    wait = WebDriverWait(browser, 15)
    browser.get("https://suninjuly.github.io/text_input_task.html")

    browser.find_element(By.CSS_SELECTOR, ".textarea").send_keys("get()")

    browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()

    alert = wait.until(EC.alert_is_present())
    print(alert.text)
finally:
    browser.quit()
