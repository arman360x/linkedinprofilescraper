from selenium import webdriver
import pickle
import time

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
input("Login manually and press Enter here...")

pickle.dump(driver.get_cookies(), open("linkedin_cookies.pkl", "wb"))
print("Cookies saved!")
driver.quit()
