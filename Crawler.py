# -*- coding: utf-8 -*-
#Crawler PM Canvas
import codecs
import urllib
from bs4 import BeautifulSoup

#html = urllib.urlopen('http://www.pmcanvasapp.com.br/projeto/modelCanvasPublic.jsp?proj=ac2728e5bb2b51b35f01bb4db88af2f9').read()
html = urllib.urlopen('Modelo do Projeto.html')
soup = BeautifulSoup(html, 'html.parser')
file = open("Info.txt", 'w')
posts = soup.find_all("span", {"data-toggle":"tooltip"})
raw_titulos = soup.find_all("img")
titulos = list()

for titulo in raw_titulos :
	x = str(titulo.text.encode("utf-8", "strict"))
	if len(x) > 2 :
		titulos.append(x)

#classes = ["areaConhecimento areaBordaLeft areaBordaTop areaJustProd","areaConhecimento areaBordaTop areaJustProd areaBordaLeft","areaConhecimento areaConhecBaixo areaBordaLeft areaObjReq","areaConhecimento areaConhecBaixo areaObjReq areaBordaLeft","areaConhecimento areaConhecBaixo areaBordaLeft areaEqEntTem areaStkPreRisEqEnt","areaConhecimento areaConhecBaixo areaEqEntTem areaStkPreRisEqEnt areaBordaLeft","areaConhecimento areaConhecBaixo areaEqEntTem areaBordaLeft"]
#repetida_1 = "areaConhecimento areaBordaTop areaBordaLeft areaStkPreRisEqEnt"
#repetida_2 = "areaConhecimento areaConhecBaixo"

#titulos_1 = ['Justificativas','Produto', 'Obj Smart', 'Requisitos', 'Equipe', 'Grupo de Entregas','Linha do Tempo','Benefícios Futuro',]
#titulos_2 = ['Restrições', 'Custos']
#titulos_3 = ['Stakeholder', 'Premissas', 'Riscos']

count = 0

#for titulo in titulos_1 :
#	print 'Titulo: ', titulo
#	posts_1 = soup.find_all('div', class_=classes[count])
#	count = count + 1
#	print count
#	for post in posts_1 :
#		print post.text
inside_posts1 = soup.find_all('span', {'data-toggle':'tooltip'})

for item in inside_posts1 : 
	for x in item : 
		print '\n', x
		print '\n', item['title'].encode("utf-8", "strict")
		file.write('\n')
		file.write(x.encode("utf-8", "strict"))
        file.write('\n')
        file.write(item['title'].encode("utf-8", "strict"))
file.close()