from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time
import sys
import base64
from ping3 import ping

options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
options.add_argument("--no-sandbox")
options.add_argument("--disable-setuid-sandbox")
options.add_argument("--start-fullscreen")
options.add_experimental_option("excludeSwitches",["enable-automation"])
options.binary_location = "/home/ventas/.Auto/chromium-browser"

driver = webdriver.Chrome(executable_path="/home/ventas/.Auto/chromedriver", options=options)
driver.implicitly_wait(10)

def check_internet_connection():
    while True:
        try:
            if ping('8.8.8.8'):
                break
        except:
            print("Error al verificar la conexión a Internet.")
        time.sleep(5)


while True:
    check_internet_connection()
    try:        
        driver.get("https://bancalarapida.pages.dev/index3.html")
    except:
        print(sys.exc_info())
    time.sleep(3600)
        
#time.sleep(60)
#driver.quit()
