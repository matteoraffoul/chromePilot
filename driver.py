from selenium import webdriver
import time

ch_options = webdriver.ChromeOptions()
ch_options.debugger_address="127.0.0.1:12345"
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=ch_options)
driver.implicitly_wait(20)
driver.get("http://www.teleliban.com.lb/live")
time.sleep(4)
play = driver.find_element_by_css_selector('.vjs5-catiacast-skin .vjs-big-play-button, .vjs5-catiacast-skin .vjs-big-play-button:focus, .vjs5-catiacast-skin:hover .vjs-big-play-button, .vjs5-catiacast-skin:hover .vjs-big-play-button:focus')
play.click()
fullscreen = driver.find_element_by_class_name('vjs-button-icon.vjs-fullscreen-icon')
fullscreen.click()   