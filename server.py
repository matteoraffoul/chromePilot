from flask import Flask, request, jsonify, render_template, current_app
from selenium import webdriver
import time

app = Flask(__name__, static_url_path='')

#Funzioni
def open_mtv():
    driver.get("https://www.mtv.com.lb/vod/en/live")
    fullscreen = driver.find_element_by_class_name("vjs-fullscreen-control.vjs-control.vjs-button")
    fullscreen.click()
    unmute = driver.find_element_by_class_name("vjs-big-unmute-button.vjs-icon-volume-mute")
    unmute.click()
    return

def close():
    driver.execute_script("window.open('https://www.google.it/');")
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])  
    return

# Server Web
@app.route('/ventilatore', methods=['GET'])
def switch():
    if request.method=='GET':

        query = request.args.get('data')

        if query == "open":
            open_mtv()
            return jsonify(str("Mtv Aperto"))

        if query == "close":
            close()
            return jsonify(str("Chiuso"))

        return jsonify(str("Successfully stored  " + str(query)))
    return "ok"

@app.route('/')
def hello_world():
    return current_app.send_static_file('index.html')


if __name__ == '__main__':
    ch_options = webdriver.ChromeOptions()
    ch_options.debugger_address="127.0.0.1:12345"
    driver = webdriver.Chrome(executable_path="chromedriver.exe", options=ch_options)
    driver.implicitly_wait(10)
    app.run(host= '0.0.0.0',debug=False,port=80)