
import json

#strJSON = '{"JUSTIFICATIVAS":[{"postitTitle":"primeiro post-it", "postitDetail":"texto primeiro post-it"},{"postitTitle":"segundo post-it", "postitDetail":"texto segundo post-it"},    {"postitTitle":"terceiro post-it", "postitDetail":"texto terceiro post-it"}]}'


#strBuilJSON = '{   "JUSTIFICATIVAS":[       {"postitTitle":"primeiro post-it", "postitDetail":"texto primeiro post-it"},        {"postitTitle":"segundo post-it", "postitDetail":"texto segundo post-it"},        {"postitTitle":"terceiro post-it", "postitDetail":"texto terceiro post-it"}    ]}'


strBuilJSON =""
fh = open('canvas.json')
for line in fh:
    strBuilJSON = strBuilJSON + line



json_object = json.loads(strBuilJSON)


if json_object['JUSTIFICATIVAS'] == []:
    print 'No Data!'
else:
    print '-----------JUSTIFICATIVAS-----------'
    for rows in json_object['JUSTIFICATIVAS']:
        print 'Title:' + rows['postitTitle']
        print 'Detail:' + rows['postitDetail']
        print ''


        
if json_object['Obj. SMART'] == []:
    print 'No Data!'
else:
    print '-----------Obj. SMART-----------'
    for rows in json_object['Obj. SMART']:
        print 'Title:' + rows['postitTitle']
        print 'Detail:' + rows['postitDetail']
        print ''


#print j["JUSTIFICATIVAS"][1]["postitTitle"]
#print j[0]

'''
data["maps"][0]["id"]  # will return 'blabla'
data["masks"]["id"]    # will return 'valore'
data["om_points"]      # will return 'value'
'''

'''
#print j
print json.dumps(j)
'''