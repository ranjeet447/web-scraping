from selenium import webdriver
from bs4 import BeautifulSoup
import requests

options = webdriver.ChromeOptions()
options.add_argument('headless')

driver = webdriver.Chrome(chrome_options=options)

url ='https://www.imdb.com/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=e31d89dd-322d-4646-8962-327b42fe94b1&pf_rd_r=901CFMAWM88FWS37FYQP&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_1'
driver.get(url)
html_doc = driver.page_source
soup = BeautifulSoup(html_doc, features="html5lib")

div = soup.find('div',class_='poster')
a = div.find('a')

url = "https://www.imdb.com"+ a['href']
print(url)

driver.get(url)

soup = BeautifulSoup(driver.page_source,features="html5lib")
all_div = soup.find_all('div',class_='pswp__zoom-wrap')
all_img = all_div[1].find_all('img')

print(all_img[1]['src'])

f= open('fimg.jpg','wb')
f.write(requests.get(all_img[1]['src']).content)
f.close()

driver.quit()


# def get_movie_list():
# 	driver.get('https://www.imdb.com/chart/top?ref_=nv_mv_250')
# 	html_doc = driver.page_source
# 	soup = BeautifulSoup(html_doc, features="html5lib")
			
# 	movie_list = []
# 	table = soup.find('table', class_= 'chart full-width')
# 	for td in table.find_all('td', class_='titleColumn'):
# 		full_title = td.text.strip().replace('\n','').replace('      ','')
# 		# print(full_title)
# 		rank = full_title.split('.')[0]
# 		# print(rank)
# 		title = full_title.split('.')[1].split('(')[0].strip()
# 		# print(title)
# 		year = full_title.split('(')[1][:-1]
# 		# print(year)
# 		a = td.find('a')
# 		# print(a['href'])
# 		# print('\n')

# 		new_movie = Movie()
# 		new_movie.rank = rank
# 		new_movie.title = title
# 		new_movie.year = year
# 		new_movie.link = a['href']

# 		movie_list.append(new_movie)

# 	driver.quit
# 	return movie_list


# movie_list = get_movie_list()

