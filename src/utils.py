import os
import sys
import json
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

options = Options()
options.headless = True

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

wait = WebDriverWait(driver, 200)

def do(by, element, event, string=None):
    wait_event = wait.until(EC.visibility_of_element_located((by, element)))
    if event == "send_keys":
        wait_event.send_keys(string)
    if event == "click":
        wait_event.click()
    if event == "clear_and_send_keys":
        wait_event.clear()
        wait_event.send_keys(string)

def login():
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    credentials = json.load(open(os.path.join(__location__, '../credentials.json')))
    do(By.NAME, "email", "send_keys", credentials["email"])
    do(By.NAME, "password", "send_keys", credentials["password"])
    do(By.ID, "kt_sign_in_submit", "click")
    do(By.XPATH, "//*[contains(text(), 'Ok, got it!')]", "click")


def insert_asa_and_submit():
    do(By.XPATH, "//*[contains(text(), 'Aggiungi Presenza')]", "click")
    for i in range(3, len(sys.argv)):
        do(By.NAME, sys.argv[i].split('=')[0], "clear_and_send_keys", sys.argv[i].split('=')[1])
    do(By.XPATH, "//form[@id='kt_modal_add_schedule_form']/div[3]/span/span/span", "click")
    do(By.XPATH, f"//li[text()='{sys.argv[2]}']", "click")
    do(By.XPATH, "//button[text()='Salva Presenza']", "click")

def insert_smart_permission():
    do(By.XPATH, "//*[contains(text(), 'Ferie/Permessi/SmartWorking')]", "click")
    do(By.XPATH, "//button[contains(.,' SmartWorking')]", "click")
    do(By.XPATH, "(//input[@name='giorni'])[4]", "clear_and_send_keys", sys.argv[2])
    do(By.XPATH, "(//div[@id='kt_modal_add_ferie_scroll']/div[2]/input)[4]", "click")
    do(By.XPATH, "(//div[@id='kt_modal_add_ferie_scroll']/div[2]/input)[4]", "send_keys", datetime.now().strftime("%d%m%Y"))
    do(By.XPATH, "(//div[@id='kt_modal_add_ferie_scroll']/div[2]/input)[4]", "send_keys", Keys.TAB)
    do(By.XPATH, "(//div[@id='kt_modal_add_ferie_scroll']/div[2]/input)[4]", "send_keys", sys.argv[3])
    do(By.CSS_SELECTOR, "#kt_modal_add_smart .btn-primary", "click")
