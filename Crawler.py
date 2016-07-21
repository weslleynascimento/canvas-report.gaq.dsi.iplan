# -*- coding: utf-8 -*-
#Crawler PM Canvas
import codecs
import urllib
from bs4 import BeautifulSoup

#html = urllib.urlopen('http://www.pmcanvasapp.com.br/projeto/modelCanvasPublic.jsp?proj=ac2728e5bb2b51b35f01bb4db88af2f9').read()
html = open('Modelo do Projeto.html')
soup = BeautifulSoup(html, 'html.parser')
file = open("Info.json", 'w')
posts = soup.find_all("span", {"data-toggle":"tooltip"})
raw_titulos = soup.find_all("img")
titulos = list()
def titulos():
	for titulo in raw_titulos :
		x = str(titulo.text.encode("utf-8", "strict"))
		if len(x) > 2 :
			titulos.append(x)


def post_and_details():
	inside_posts1 = soup.find_all('span', {'data-toggle':'tooltip'})
	for string_detalhes in inside_posts1 : 
		for post_title in string_detalhes :
			print '\n', post_title
			print '\n', string_detalhes['title'].encode("utf-8", "strict")

			title = '{"postitTitle":'+'"'+ post_title.replace('\n', '').encode("utf-8", "strict")+'"'
			file.write(title)
			file.write(',')
			details = '"postitDetail":'+'"'+string_detalhes['title'].replace('\n', '').encode("utf-8", "strict")+'"}'
			file.write(details)
			file.write(',')
			file.write('\n')


post_and_details()

file.close()