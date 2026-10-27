from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

link = "http://suninjuly.github.io/registration1.html"

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=options)

try:
    wait = WebDriverWait(browser, 15)
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input").send_keys("test@example.com")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "h1"), "successfully registered"))

    print(browser.find_element(By.TAG_NAME, "h1").text)
finally:
    browser.quit()
