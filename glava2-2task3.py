from pathlib import Path

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

file_path = Path(__file__).resolve().with_name("glava2-2task3.txt")
file_path.touch(exist_ok=True)

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=options)

try:
    wait = WebDriverWait(browser, 15)
    browser.get("http://suninjuly.github.io/file_input.html")

    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("test@example.com")
    browser.find_element(By.ID, "file").send_keys(str(file_path))

    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    alert = wait.until(EC.alert_is_present())
    print(alert.text.split()[-1])
finally:
    browser.quit()
