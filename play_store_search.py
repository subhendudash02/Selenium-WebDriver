from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys  

browser = wd.Chrome()
browser.maximize_window()
browser.get("https://play.google.com/store")

app_name = input("Which app you want to open?")

browser.find_elements_by_name("q")[0].send_keys(app_name)
browser.find_elements_by_tag_name("button")[0].send_keys(Keys.ENTER)

browser.refresh()

browser.execute_script("document.getElementsByClassName('WsMG1c nnK0zc')[0].click()") # Selecting the top result
