from selenium import webdriver
import time

ch_options = webdriver.ChromeOptions()
ch_options.debugger_address="127.0.0.1:12345"
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=ch_options)
driver.implicitly_wait(10)
driver.get("https://www.mtv.com.lb/vod/en/live")
fullscreen = driver.find_element_by_class_name("vjs-fullscreen-control.vjs-control.vjs-button")
fullscreen.click()
unmute = driver.find_element_by_class_name("vjs-big-unmute-button.vjs-icon-volume-mute")
unmute.click()