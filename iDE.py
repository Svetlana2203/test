from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


s=Service('F:/Проги/Новая папка/chromedriver_win32/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://qahacking.guru/")
driver.set_window_size(1920, 982)
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".uk-navbar-nav > li:nth-child(1) > a").click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,977)", "");
driver.find_element(By.ID, "firstName").click()
driver.find_element(By.ID, "lastName").send_keys("Atyaksheva")
time.sleep(1)
driver.find_element(By.ID, "userEmail").send_keys("Lsoul39@ya.ru")
time.sleep(1)
driver.find_element(By.ID, "sex-1").click()
driver.find_element(By.ID, "userNumber").send_keys("+79374444444")
driver.find_element(By.ID, "date").click()
driver.find_element(By.CSS_SELECTOR, ".uk-section-default:nth-child(5)").click()
driver.find_element(By.ID, "date").send_keys("11-12-2023")
driver.find_element(By.CSS_SELECTOR, ".subjects-auto-complete__placeholder").click()
time.sleep(1)
driver.find_element(By.ID, "subjects-label").click()
driver.find_element(By.ID, "hobbies-checkbox-1").click()
driver.find_element(By.ID, "hobbies-checkbox-2").click()
driver.find_element(By.CSS_SELECTOR, ".col-md-9:nth-child(6) #hobbies-checkbox-1").click()
driver.find_element(By.ID, "currentAddress").click()
driver.find_element(By.ID, "currentAddress").send_keys("test")
driver.find_element(By.ID, "submit").click()
print("тест успешно завершен")
