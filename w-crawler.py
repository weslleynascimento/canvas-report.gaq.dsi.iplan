# -*- coding: utf-8 -*-
#Crawler PM Canvas
import codecs
import urllib
from bs4 import BeautifulSoup

#html = urllib.urlopen('http://www.pmcanvasapp.com.br/projeto/modelCanvasPublic.jsp?proj=ac2728e5bb2b51b35f01bb4db88af2f9').read()
html = open('Modelo do Projeto.html')
soup = BeautifulSoup(html, 'html.parser')
file = open("Info.json", 'w')


def post_and_details():
    inside_posts1 = soup.find_all('span', {'data-toggle':'tooltip'})
    #strText = inside_posts1
    #strText = strText.replace("<\soan>", "</span> \n").strip()
    strPostIt = ""
    strDetail = ""
    for myspan in inside_posts1:
        strDetail =  myspan.get('data-original-title').encode("utf-8", "strict") 
        strPostIt =  myspan.text.encode("utf-8", "strict")
        
        title = '{"postitTitle":'+'"'+ strPostIt.replace('\n', '') +'"'
        file.write(title)
        file.write(',')
        details = '"postitDetail":'+'"'+ strDetail.replace('\n', '') +'"}'
        file.write(details)
        file.write(',')
        file.write('\n')
    
post_and_details()
file.close()

