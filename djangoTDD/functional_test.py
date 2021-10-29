from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/usr/local/bin/chromedriver')
browser = webdriver.Chrome(service=service)
browser.get('http://localhost:8000')

assert 'successfully' in browser.title
