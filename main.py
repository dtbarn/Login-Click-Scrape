# Login Click Scrape Exercise 
# user:automated  pw:automatedautomated

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
  #options to make browsing easier
  options = webdriver.ChromeOptions()
  #info-bars may pop up and confuse cursor location
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/login")
  return driver

def clean_text(text):
  '''Extract the temperature from the element'''
  output = float(text.split(": ")[1])
  return output

def main():
  driver = get_driver()
  #xpath can be found by using inspect on the 
  #web page to locate the item of interest
  driver.find_element(by="id", value="id_username").send_keys("automated")
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  time.sleep(2)
  # click 'home' button
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
  element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
  time.sleep(2)
  return clean_text(element.text)

print(main())


