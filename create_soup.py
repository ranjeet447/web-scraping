from selenium import webdriver

from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)

driver.get('http://python.org')
html_doc = driver.page_source
# print(html_doc)

soup = BeautifulSoup(html_doc, features="html5lib")
# print(soup.prettify())

first_p_tag = soup.find('p')
print(first_p_tag)

all_i_tag = soup.find_all('i')

print(all_i_tag)


driver.quit()