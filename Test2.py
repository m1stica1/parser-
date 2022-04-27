from cgitb import text
from unicodedata import name
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get("https://galaxystore.ru/catalog/smartfony/") # => "Ссылка сайта"
driver.title # => "Google"
soup = BeautifulSoup(driver.page_source, 'html.parser')

elem = driver.find_element(By.CSS_SELECTOR, "div.card-list.catalog__cards") #какой div приминяется для поиска нужно элемента
items = elem.find_elements(By.XPATH, '//div[@class="card"]') #какой класс находится в div и нужна информация
cards = soup.find_all("div",{"class":"card"})
#print(len(cards))
#name_set = set()
#titles_count = 0
for card in cards:
    title_element = card.find_all("a",{"class":"card__name g-text"})[0]
    title = title_element.string
    print("Название: " +title)

    price_element = card.find_all("p",{"class":"card__price g-text gm-bold gm-m gm-ff2"})[0]
#    price = price_element.descendants
    price = price_element.contents[0].strip()
    print("Цена: " +price)
#    print(price.strip())
#    new_price = price_element.find_element(By.CLASS_NAME, "card__oldPrice g-text g-text-old-pay")
#    price = price_element.find()[0].text
#    print(price)
#    print(len(price_element.findChildren()))
#    print(price_element.contents[0].strip())

# card__price g-text gm-bold gm-m gm-ff2

#    /html/body/div[2]/div[2]/main/div[2]/div[1]/div[2]/div[2]/div[2]/p/text()  | /html/body/div[2]/div[2]/main/div[2]/div[1]/div[2]/div[2]/div[2]/p/text()
#    price = price_element.text
#    print("Цена: " +price)

#print(titles_count == len(name_set))
#print(titles_count)
#print(len(name_set))