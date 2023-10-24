from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.service import Service


print("Fake news detection by Paras Gupta")
driver = webdriver.Chrome()

times_url = "https://timesofindia.indiatimes.com/"
driver.get(times_url)
news_elements = driver.find_elements(By.CLASS_NAME,'keyword')

print(news_elements,"news_elements")

for i in news_elements:
    news_url = i.get_attribute('href')
    driver2 = webdriver.Chrome()
    driver2.get(news_url)
    find_title = driver2.find_element(By.TAG_NAME,'h1')
    print(find_title.text,"vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv")
    driver2.quit()

    