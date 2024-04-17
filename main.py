 
from selenium import webdriver
from selenium.webdriver.common.by import By

# Start a new Chrome browser session
driver = webdriver.Chrome()

# URL of the website you want to visit
url = 'https://asunnot.oikotie.fi/vuokra-asunnot'

# Navigate to the URL
driver.get(url)



# Verify title
search_results = driver.find_elements(By.CSS_SELECTOR, "search-result-cards-v2 > div > div > card-v2")

for card in search_results[:3]:
    address_element = card.find_element(By.CSS_SELECTOR, "div.card-v2-text-container__wrapper > div:first-child")
    housetype_element = card.find_element(By.CSS_SELECTOR, "div.card-v2-text-container__wrapper > div:nth-child(2) > div:first-child")
    additionals_element = card.find_element(By.CSS_SELECTOR, "div.card-v2-text-container__wrapper > div:nth-child(2) > div:last-child")
    price_element = card.find_element(By.CSS_SELECTOR, "div.card-v2-text-container > div:nth-child(2) > div:first-child > h2")
    size_element = card.find_element(By.CSS_SELECTOR, "div.card-v2-text-container > div:nth-child(2) > div:last-child > h2")

    address = address_element.get_attribute('innerHTML')
    housetype = housetype_element.get_attribute('innerHTML')
    additionals = additionals_element.get_attribute('innerHTML')
    price = price_element.get_attribute('innerHTML')
    size = size_element.get_attribute('innerHTML')
    print(address, housetype, additionals, price, size)

    




# Close the browser
driver.quit()
