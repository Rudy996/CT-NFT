from random import choice
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions

from time import sleep
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument('--disable-gpu')
options.add_argument('--disable-infobars')
options.add_argument("--mute-audio")
options.add_argument("--disable-blink-features")
options.add_argument('--profile-directory=Default')
options.add_argument("--mute-audio")
options.add_extension("MetaMask.crx")

mnemonic = ("") 

def work():
    try:
        driver = webdriver.Chrome(executable_path=r"chromedriver\chromedriver.exe", options=options)
        wait = WebDriverWait(driver, 30)
        driver.switch_to.window(driver.window_handles[0])
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#initialize/welcome")
        wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@role="button"]'))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'first-time-flow__button'))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))).click()
        time.sleep(1)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'MuiInput-input'))).send_keys(mnemonic)
        wait.until(EC.element_to_be_clickable((By.ID, 'password'))).send_keys("Papsgpasgpap2125125")
        wait.until(EC.element_to_be_clickable((By.ID, 'confirm-password'))).send_keys("Papsgpasgpap2125125")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'first-time-flow__terms'))).click()
        print("h")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))).click()
        time.sleep(10)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'btn-primary'))).click()
        driver.get("chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html#settings/networks/add-network")
        time.sleep(1)
        elems = driver.find_elements(By.CLASS_NAME, "form-field__input")
        wait.until(EC.element_to_be_clickable((elems[0]))).send_keys("Matic")
        wait.until(EC.element_to_be_clickable((elems[1]))).send_keys("https://polygon-rpc.com/")
        wait.until(EC.element_to_be_clickable((elems[2]))).send_keys("137")
        wait.until(EC.element_to_be_clickable((elems[3]))).send_keys("MATIC")
        wait.until(EC.element_to_be_clickable((elems[4]))).send_keys("https://polygonscan.com/")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))).click()
        time.sleep(0.5)
        time.sleep(1)
        driver.get("https://invite.ctnft.net/I0kPuC")
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn--right-icon"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ModalNftPromo_close__HqzzV"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "ConnectWallet_connectWalletButton__5dYdY"))).click()
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[2])
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))).click()
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))).click()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(1)
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[2])
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-primary"))).click()
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)
        try:
            wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Tutorial_skip__phT5X"))).click()
        except:
            print("скипнул")
        t = 0
        while t == 0:
            try:
                try:
                    wait.until(
                        EC.element_to_be_clickable((By.CLASS_NAME, "Tutorial_skip__phT5X Tutorial_btn__G1Fsv"))).click()
                except:
                    print("скипнул")
                print("Жду кнопку: Активировать")
                wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "Button_success__TLsxK"))).click()
                try:
                    wait.until(
                        EC.element_to_be_clickable((By.CLASS_NAME, "Tutorial_skip__phT5X Tutorial_btn__G1Fsv"))).click()
                except:
                    print("скипнул")
            except:
                print()
                try:
                    wait.until(
                        EC.element_to_be_clickable((By.CLASS_NAME, "Tutorial_skip__phT5X Tutorial_btn__G1Fsv"))).click()
                except:
                    print("скипнул")


        time.sleep(500)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

work()
