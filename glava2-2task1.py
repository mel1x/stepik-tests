import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

link = sys.argv[1] if len(sys.argv) > 1 else "https://suninjuly.github.io/selects1.html"

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=options)

try:
    wait = WebDriverWait(browser, 15)
    browser.get(link)

    num1 = int(browser.find_element(By.ID, "num1").text)
    num2 = int(browser.find_element(By.ID, "num2").text)
    answer = str(num1 + num2)

    dropdown = Select(browser.find_element(By.ID, "dropdown"))
    dropdown.select_by_value(answer)

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    alert = wait.until(EC.alert_is_present())
    print(alert.text.split()[-1])
finally:
    browser.quit()
