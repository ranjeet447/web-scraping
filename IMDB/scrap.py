from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import os


options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(chrome_options=options)

class Movie():
	"""docstring for Movie"""
	def __init__(self):
		self.rank = ""
		self.title = ""
		self.year = ""
		self.link = ""

# get list of top rated movies 
def get_movie_list():
	driver.get('https://www.imdb.com/chart/top?ref_=nv_mv_250')
	html_doc = driver.page_source
	soup = BeautifulSoup(html_doc, features="html5lib")
			
	movie_list = []
	table = soup.find('table', class_= 'chart full-width')
	for td in table.find_all('td', class_='titleColumn'):
		full_title = td.text.strip().replace('\n','').replace('      ','')
		# print(full_title)
		rank = full_title.split('.')[0]
		# print(rank)
		title = full_title.split('.')[1].split('(')[0].strip()
		# print(title)
		year = full_title.split('(')[1][:-1]
		# print(year)
		a = td.find('a')
		# print(a['href'])
		# print('\n')

		new_movie = Movie()
		new_movie.rank = rank
		new_movie.title = title
		new_movie.year = year
		new_movie.link = a['href']
		movie_list.append(new_movie)

	driver.quit
	return movie_list


# create poster folder where images will be downloaded.
if not os.path.exists('posters'):
    os.makedirs('posters')

# download posters for movies in movie_list
def download_all_poster(movie_list):
	for movie in movie_list:
		url ='https://www.imdb.com' + movie.link

		driver.get(url)
		html_doc = driver.page_source
		soup = BeautifulSoup(html_doc, features="html5lib")

		div = soup.find('div',class_='poster') 
		a = div.find('a')

		url = "https://www.imdb.com"+ a['href']
		# print(url)

		driver.get(url)

		soup = BeautifulSoup(driver.page_source,features="html5lib")
		all_div = soup.find_all('div',class_='pswp__zoom-wrap')
		all_img = all_div[1].find_all('img')

		print(all_img[1]['src'])

		with open(os.path.join('posters',movie.rank+ '. '+ movie.title+'.jpg'),'wb') as f:
			f.write(requests.get(all_img[1]['src']).content) 

	driver.quit() 



movie_list = get_movie_list()
download_all_poster(movie_list)  