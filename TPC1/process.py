import re
import json

texto = open('medicina.xml', 'r').read()

def remove_header_footer(texto):
    texto = re.sub(r'<text.* font="1">ocabulario.*<\/text>', r'###', texto)
    texto = re.sub(r'.*\n###\n.*\n', r'___', texto)
    texto = re.sub(r'<page.*\n|<\/page>\n', r'', texto)
    
    return texto

texto = remove_header_footer(texto)

def marcaE(texto):
    texto = re.sub(r'(<text.* font="3"><b>\s*((\d+)\s*(.+\S)\s+(\S))<\/b><\/text>\n)(<text.*>\s*<\/text>\n)*(<text.* font="6"><i>\s*(\S.*)<\/i><\/text>\n)', r'###C \4 ###gen \5 ###area \8\n', texto)
  
    return texto

texto = marcaE(texto)

def marcaLinguas(texto):
    texto = re.sub(r'(.*\n)(<text.* font="0">\s*(es|en|pt|la)\s*<\/text>)(\n<text.* font="7"><i>(.+\S)<\/i><\/text>)', r'###L \3 ###pal \5', texto)
    
    return texto

texto = marcaLinguas(texto)

def cleanxml(texto):
    texto = re.sub(r'.+<\/text>\n',r'',texto)

    return texto

texto = cleanxml(texto)

file = open('medicina2.txt', 'w')

file.write(texto)

dict_p = {}

patern = re.compile(r"###C\s+(.*)\s###gen\s(\S)\s###area\s(\S+)\n(###L\s(\S+)\s###pal\s(\S+)\n){1,4}")
patern2 = re.compile(r'###L\s(\S+)\s###pal\s(\S+)\n')

for match in patern.finditer(texto):
    dict_i = {}
    dict_i["genero"] = match.group(2)
    dict_i["area"] = match.group(3)
    dict_t = {}
    for match2 in patern2.finditer(match.group(0)) :
        dict_t[match2.group(1)] = match2.group(2)
    dict_i["trad"] = dict_t
    dict_p[match.group(1)] = dict_i

json_object = json.dumps(dict_p, indent = 4)

jsonfile = open('medicina2.json', 'w')

jsonfile.write(json_object)