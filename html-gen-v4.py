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
    strHTML = strHTML + '<meta content="text/html; charset=UTF-8" http-equiv="content-type"><title>PMC - FGF</title>'
  
    strHTML = strHTML + '<link href="style-canvas.css" rel="stylesheet">'
    
    strHTML = strHTML + '</TDCLASS="DETALHES"></head><body>'
    strHTML = strHTML + '<br>'

    strHTML = strHTML + '<table class="table table-bordered table-hover table-condensed">'
    strHTML = strHTML + '    <tbody>'
    strHTML = strHTML + '    <tr>'
    
    
    strHTML = strHTML + '<tr>'
    strHTML = strHTML + '<td class="classificacao-why" colspan="3" rowspan="1" style="vertical-align: top;">WHY?'
    strHTML = strHTML + '</td>'
    strHTML = strHTML + '</tr>'
    
    
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
    
    strHTML = strHTML + '<tr>'
    strHTML = strHTML + '<td colspan="3" rowspan="1" style="vertical-align: top;"><br>'
    strHTML = strHTML + '</td>'
    strHTML = strHTML + '</tr>'
    
    
    strHTML = strHTML + '<tr>'
    
    strHTML = strHTML + '<tr>'
    strHTML = strHTML + '<td class="classificacao-what" colspan="3" rowspan="1" style="vertical-align: top;">WHAT?'
    strHTML = strHTML + '</td>'
    strHTML = strHTML + '</tr>'
    
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
    
    strHTML = strHTML + '<tr>'
    strHTML = strHTML + '<td class="classificacao-who" colspan="3" rowspan="1" style="vertical-align: top;">WHO?'
    strHTML = strHTML + '</td>'
    strHTML = strHTML + '</tr>'
    
    strHTML = strHTML + '  <td class="categoria" colspan="1" rowspan="' + str(len(json_object['STAKEHOLDERS'])) + '"> <img style="width: 40px; height: 23px;" alt=""src="images/fatores-externos.jpg">STAKEHOLDERS<br></td>'
    
    
    cont = 0            
    if json_object['STAKEHOLDERS'] == []:
        strHTML = strHTML + 'No Data to STAKEHOLDERS! \n'
    else:
        for rows in json_object['STAKEHOLDERS']:
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
    strHTML = strHTML + '  <td class="categoria" colspan="1" rowspan="' + str(len(json_object['EQUIPE'])) + '"> <img style="width: 40px; height: 23px;" alt=""src="images/equipe.jpg">EQUIPE<br></td>'
    
    
    cont = 0            
    if json_object['EQUIPE'] == []:
        strHTML = strHTML + 'No Data to EQUIPE! \n'
    else:
        for rows in json_object['EQUIPE']:
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
    
    strHTML = strHTML + '<tr>'
    strHTML = strHTML + '<td class="classificacao-how" colspan="3" rowspan="1" style="vertical-align: top;">HOW?'
    strHTML = strHTML + '</td>'
    strHTML = strHTML + '</tr>'
    
    strHTML = strHTML + '  <td class="categoria" colspan="1" rowspan="' + str(len(json_object['PREMISSAS'])) + '"> <img style="width: 40px; height: 23px;" alt=""src="images/premissas.jpg">PREMISSAS<br></td>'
    
    
    cont = 0            
    if json_object['PREMISSAS'] == []:
        strHTML = strHTML + 'No Data to PREMISSAS! \n'
    else:
        for rows in json_object['PREMISSAS']:
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
    
            
    strHTML = strHTML + '  <td class="categoria" colspan="1" rowspan="' + str(len(json_object['GRUPO DE ENTREGAS'])) + '"> <img style="width: 40px; height: 23px;" alt=""src="images/entregas.jpg">GRUPO DE ENTREGAS<br></td>'
    
    
    cont = 0            
    if json_object['GRUPO DE ENTREGAS'] == []:
        strHTML = strHTML + 'No Data to GRUPO DE ENTREGAS! \n'
    else:
        for rows in json_object['GRUPO DE ENTREGAS']:
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
    
            
    strHTML = strHTML + '  <td class="categoria" colspan="1" rowspan="' + str(len(json_object['RESTRICOES'])) + '"> <img style="width: 40px; height: 23px;" alt=""src="images/restricoes.jpg">RESTRICOES<br></td>'
    
    
    cont = 0            
    if json_object['RESTRICOES'] == []:
        strHTML = strHTML + 'No Data to RESTRIÇÕES! \n'
    else:
        for rows in json_object['RESTRICOES']:
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
    strHTML = strHTML + '<td class="classificacao-how-much-when" colspan="3" rowspan="1" style="vertical-align: top;">HOW MUCH & WHEN?'
    strHTML = strHTML + '</td>'
    strHTML = strHTML + '</tr>'
    
    strHTML = strHTML + '  <td class="categoria" colspan="1" rowspan="' + str(len(json_object['RISCOS'])) + '"> <img style="width: 40px; height: 23px;" alt=""src="images/riscos.jpg">RISCOS<br></td>'
    
    
    cont = 0            
    if json_object['RISCOS'] == []:
        strHTML = strHTML + 'No Data to RISCOS! \n'
    else:
        for rows in json_object['RISCOS']:
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
    
            
    strHTML = strHTML + '  <td class="categoria" colspan="1" rowspan="' + str(len(json_object['LINHA DO TEMPO'])) + '"> <img style="width: 40px; height: 23px;" alt=""src="images/linha-tempo.jpg">LINHA DO TEMPO<br></td>'
    
    
    cont = 0            
    if json_object['LINHA DO TEMPO'] == []:
        strHTML = strHTML + 'No Data to LINHA DO TEMPO! \n'
    else:
        for rows in json_object['LINHA DO TEMPO']:
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
    
            
    strHTML = strHTML + '  <td class="categoria" colspan="1" rowspan="' + str(len(json_object['CUSTOS'])) + '"> <img style="width: 40px; height: 23px;" alt=""src="images/custos.jpg">CUSTOS<br></td>'
    
    
    cont = 0            
    if json_object['CUSTOS'] == []:
        strHTML = strHTML + 'No Data to RESTRIÇÕES! \n'
    else:
        for rows in json_object['CUSTOS']:
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






    
    
    
    
    


   
    strHTML = strHTML + '        </tbody>'
    strHTML = strHTML + '    </table>'
    strHTML = strHTML + '</body></html>'
    
    return strHTML


message =  buildCanvasHTML ()
with io.open('index.html','w',encoding='utf8') as f:
    f.write(message)

f.close()
webbrowser.open_new_tab('index.html')
