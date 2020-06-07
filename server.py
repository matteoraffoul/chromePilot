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

def open_noursat():
    driver.get("https://player.l1vetv.com/noursat1/")
    start = driver.find_element_by_class_name("vjs-big-play-button")
    start.click()
    fullscreen = driver.find_element_by_class_name("vjs-fullscreen-control.vjs-control.vjs-button")
    fullscreen.click()
    return

def close():
    driver.execute_script("window.open('https://www.google.it/');")
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])  
    return


# Server Web
@app.route('/open', methods=['GET'])
def open_route():
    if request.method=='GET':

        action = request.args.get('action')
        channel = request.args.get('channel')

        if action == "open":
            if channel == "mtv":
                open_mtv()
                return jsonify(str("Mtv Aperto"))
            if channel == "noursat":
                open_noursat()
                return jsonify(str("Noursat Aperto"))
    return "ok"
    

@app.route('/close', methods=['GET'])
def close_route():
    if request.method=='GET':
        close()
        return jsonify(str("Chiuso"))
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