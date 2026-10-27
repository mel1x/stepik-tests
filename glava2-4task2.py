import math

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--window-size=1920,1080")
options.add_experimental_option("excludeSwitches", ["enable-logging"])

browser = webdriver.Chrome(options=options)

try:
    wait = WebDriverWait(browser, 15)
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element(By.ID, "book").click()

    x_element = wait.until(
        EC.visibility_of_element_located((By.ID, "input_value"))
    )
    y = calc(x_element.text)

    browser.find_element(By.ID, "answer").send_keys(y)
    wait.until(EC.element_to_be_clickable((By.ID, "solve"))).click()

    alert = wait.until(EC.alert_is_present())
    print(alert.text.split()[-1])
finally:
    browser.quit()
