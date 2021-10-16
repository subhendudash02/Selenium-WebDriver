from selenium import webdriver

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.wikipedia.org/")

browser.execute_script("document.getElementById('searchInput').setAttribute('value', 'Steve Jobs')")
browser.execute_script("document.getElementsByTagName('button')[0].click()")