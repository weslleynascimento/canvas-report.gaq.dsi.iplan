# -*- coding: utf-8 -*-
#PM Canvas - Gerador de HTML

# write-html.py

import webbrowser
import json
import io

def buildCanvasHTML( ):

    strBuilJSON =""
    strHTML =""
    fh = open('canvas.json')
    for line in fh:
        strBuilJSON = strBuilJSON + line

    json_object = json.loads(strBuilJSON)

    
    
    strHTML = strHTML + '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'
    strHTML = strHTML + '<html><head><TDCLASS="DETALHES">'
    strHTML = strHTML + '<meta content="text/html; charset=UTF-8" http-equiv="content-type"><title>canva-crawled</title>'
  
    strHTML = strHTML + '<style type="text/css">'
    strHTML = strHTML + '        .categoria {background-color: white; text-align: center; font-weight: bold; font-size: 14pt; font-family: "Segoe UI"; "sans-serif" ; color: gray;}'
    strHTML = strHTML + '        .post-it {background-color: rgb(245, 245, 245); text-align: center;  color: gray; font-size: 12pt; font-family: "Segoe UI"; "sans-serif";}'
    strHTML = strHTML + '        .detalhes {background-color: rgb(245, 245, 245); text-align: center; color: gray; font-style: italic; font-size: 10pt; font-family: "Segoe UI"; "sans-serif" ; }'
    strHTML = strHTML + '</style>'
    strHTML = strHTML + '</TDCLASS="DETALHES"></head><body>'
    strHTML = strHTML + '<br>'

    strHTML = strHTML + '<table class="table table-bordered table-hover table-condensed">'
    strHTML = strHTML + '    <tbody>'
    strHTML = strHTML + '    <tr>'
    
    strHTML = strHTML + '       <td class="categoria"  colspan="1" rowspan="' + str(len(json_object['JUSTIFICATIVAS'])) + '"> <img style="width: 40px; height: 23px;" alt=""src="images/justificativas.jpg">Justificativas</td>'
    
    
    cont = 0
    if json_object['JUSTIFICATIVAS'] == []:
        strHTML = strHTML + 'No Data to JUSTIFICATIVAS \n'
    else:
        for rows in json_object['JUSTIFICATIVAS']:
            if cont == 1:
                strHTML = strHTML + '    <tr>'
            strHTML = strHTML + '       <td class="post-it">' + rows['postitTitle'] + '</td>'
            strHTML = strHTML + '       <td class="detalhes">' + rows['postitDetail'] + '</td>'
            strHTML = strHTML + '   </tr>'
            cont = cont + 1

    strHTML = strHTML + '<tr>'
    strHTML = strHTML + '<td colspan="3" rowspan="1" style="vertical-align: top;"><br>'
    strHTML = strHTML + '</td>'
    strHTML = strHTML + '</tr>'

    
    strHTML = strHTML + '<tr>'
    strHTML = strHTML + '  <td class="categoria" colspan="1" rowspan="' + str(len(json_object['OBJETIVO SMART'])) + '"> <img style="width: 40px; height: 23px;" alt=""src="images/objetivo.jpg">Objetivo SMART<br></td>'
    
    
    cont = 0            
    if json_object['OBJETIVO SMART'] == []:
        strHTML = strHTML + 'No Data to OBJETIVO SMART! \n'
    else:
        for rows in json_object['OBJETIVO SMART']:
            if cont == 1:
                strHTML = strHTML + '    <tr>'
            strHTML = strHTML + '<td class="post-it">' + rows['postitTitle'] + '</td>'
            strHTML = strHTML + '<td class="detalhes">' + rows['postitDetail'] + '</td>'
            strHTML = strHTML + '   </tr>'
            cont = cont + 1


    strHTML = strHTML + '<tr>'
    strHTML = strHTML + '<td colspan="3" rowspan="1" style="vertical-align: top;"><br>'
    strHTML = strHTML + '</td>'
    strHTML = strHTML + '</tr>'


    strHTML = strHTML + '<tr>'
    strHTML = strHTML + '  <td class="categoria" colspan="1" rowspan="' + str(len(json_object['PRODUTO'])) + '"> <img style="width: 40px; height: 23px;" alt=""src="images/produto.jpg">PRODUTO<br></td>'
    
    
    cont = 0            
    if json_object['PRODUTO'] == []:
        strHTML = strHTML + 'No Data to PRODUTO! \n'
    else:
        for rows in json_object['PRODUTO']:
            if cont == 1:
                strHTML = strHTML + '    <tr>'
            strHTML = strHTML + '<td class="post-it">' + rows['postitTitle'] + '</td>'
            strHTML = strHTML + '<td class="detalhes">' + rows['postitDetail'] + '</td>'
            strHTML = strHTML + '   </tr>'
            cont = cont + 1
   
   
    strHTML = strHTML + '<tr>'
    strHTML = strHTML + '<td colspan="3" rowspan="1" style="vertical-align: top;"><br>'
    strHTML = strHTML + '</td>'
    strHTML = strHTML + '</tr>'


    strHTML = strHTML + '<tr>'
    strHTML = strHTML + '  <td class="categoria" colspan="1" rowspan="' + str(len(json_object['REQUISITOS'])) + '"> <img style="width: 40px; height: 23px;" alt=""src="images/requisitos.jpg">REQUISITOS<br></td>'
    
    
    cont = 0            
    if json_object['REQUISITOS'] == []:
        strHTML = strHTML + 'No Data to REQUISITOS! \n'
    else:
        for rows in json_object['REQUISITOS']:
            if cont == 1:
                strHTML = strHTML + '    <tr>'
            strHTML = strHTML + '<td class="post-it">' + rows['postitTitle'] + '</td>'
            strHTML = strHTML + '<td class="detalhes">' + rows['postitDetail'] + '</td>'
            strHTML = strHTML + '   </tr>'
            cont = cont + 1
   

    strHTML = strHTML + '<tr>'
    strHTML = strHTML + '<td colspan="3" rowspan="1" style="vertical-align: top;"><br>'
    strHTML = strHTML + '</td>'
    strHTML = strHTML + '</tr>'


    strHTML = strHTML + '<tr>'
    strHTML = strHTML + '  <td class="categoria" colspan="1" rowspan="' + str(len(json_object['BENEFICIOS FUTURO'])) + '"> <img style="width: 40px; height: 23px;" alt=""src="images/beneficios.jpg">BENEFICIOS FUTURO<br></td>'
    
    
    cont = 0            
    if json_object['BENEFICIOS FUTURO'] == []:
        strHTML = strHTML + 'No Data to REQUISITOS! \n'
    else:
        for rows in json_object['BENEFICIOS FUTURO']:
            if cont == 1:
                strHTML = strHTML + '    <tr>'
            strHTML = strHTML + '<td class="post-it">' + rows['postitTitle'] + '</td>'
            strHTML = strHTML + '<td class="detalhes">' + rows['postitDetail'] + '</td>'
            strHTML = strHTML + '   </tr>'
            cont = cont + 1



   
    strHTML = strHTML + '        </tbody>'
    strHTML = strHTML + '    </table>'
    strHTML = strHTML + '</body></html>'
    
    return strHTML


message =  buildCanvasHTML ()
    #f = open('helloworld.html','w')
with io.open('helloworld.html','w',encoding='utf8') as f:
    f.write(message)

f.close()
webbrowser.open_new_tab('helloworld.html')

#print message

'''
f.write(message)
f.close()
webbrowser.open_new_tab('helloworld.html')
'''