from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(10)
