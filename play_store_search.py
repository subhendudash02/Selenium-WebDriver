from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys  

browser = wd.Chrome()
browser.maximize_window()
browser.get("https://play.google.com/store")

browser.find_elements_by_name("q")[0].send_keys("WhatsApp")
browser.find_elements_by_tag_name("button")[0].send_keys(Keys.ENTER)

