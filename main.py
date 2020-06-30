from flask import Flask, request, jsonify, render_template, current_app
from selenium import webdriver
import time, os, socket, pyautogui

app = Flask(__name__, static_url_path='')

#----------------------------------------------------------------------------------Function------------------------------------------------------------------------------------------------------------------------#

def open_mtv():
    driver.get("https://www.mtv.com.lb/vod/en/live")
    time.sleep(5)
    pyautogui.press('f')
    pyautogui.press('m')
    try:
        driver.find_element_by_class_name("vjs-big-unmute-button.vjs-icon-volume-mute")
    except:
        return
    else:
        pyautogui.press('m')
        return
    return

def open_noursat():
    driver.get("https://player.l1vetv.com/noursat4/")
    time.sleep(5)
    pyautogui.click(960,540)
    pyautogui.press('m')
    try:
        driver.find_element_by_class_name("vjs-big-unmute-button.vjs-icon-volume-mute")
    except:
        return
    else:
        pyautogui.press('m')
        return
    

def open_mbc2():
    driver.implicitly_wait(20)
    driver.get("http://shls-mbc2-prod.shahid.net/mbc2-prod_1.m3u8")
    time.sleep(1)
    fullscreen = driver.find_element_by_css_selector('.media-control[data-media-control] .media-control-layer[data-controls] button.media-control-button[data-fullscreen]')
    fullscreen.click()
    return
    

def open_teleliban():
    driver.get("http://www.teleliban.com.lb/live")
    time.sleep(4)
    play = driver.find_element_by_css_selector('.vjs5-catiacast-skin .vjs-big-play-button, .vjs5-catiacast-skin .vjs-big-play-button:focus, .vjs5-catiacast-skin:hover .vjs-big-play-button, .vjs5-catiacast-skin:hover .vjs-big-play-button:focus')
    play.click()
    fullscreen = driver.find_element_by_class_name('vjs-button-icon.vjs-fullscreen-icon')
    fullscreen.click()   
    return

def close():
    driver.get("https://www.google.it") 
    return

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

#----------------------------------------------------------------------------------Server Web----------------------------------------------------------------------------------------------------------------------#

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
            if channel == "mbc2":
                open_mbc2()
                return jsonify(str("MBC2 Aperto"))
            if channel == "teleliban":
                open_teleliban()
                return jsonify(str("LBCI Aperto"))
    return "ok"
  

@app.route('/close', methods=['GET'])
def close_route():
    if request.method=='GET':
        close()
        return jsonify(str("Chiuso"))
    return "ok"


@app.route('/')
def hello_world():
    return render_template('index.html', name=get_ip())

#----------------------------------------------------------------------------------Main----------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    if os.name == "nt":
        print("On Windows")
        ch_options = webdriver.ChromeOptions()
        ch_options.debugger_address="127.0.0.1:12345"
        driver = webdriver.Chrome(executable_path="chromedriver.exe", options=ch_options)
        driver.implicitly_wait(10)
        app.run(host= '0.0.0.0',debug=True,port=8000)
    elif os.name == "posix":
        print("On Linux")
        ch_options = webdriver.ChromeOptions()
        ch_options.debugger_address="127.0.0.1:12345"
        driver = webdriver.Chrome(executable_path="/home/garot/Desktop/chromePilot/chromedriver", options=ch_options)
        driver.implicitly_wait(10)
        app.run(host= '0.0.0.0',debug=True,port=8000)

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#