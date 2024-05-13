def replace_bar(my_list):
    RESULT = [elem.replace('///', '-').replace('--','NO') for elem in my_list]
    return RESULT

my_list = ["BUENOS AIRES","25 de Mayo","25 de Mayo","23408","SI","SI","--","SI","SI","SI"]
resultado = replace_bar(my_list)
print(resultado)
#---->["BUENOS AIRES","25 de Mayo","25 de Mayo","23408","SI","SI","NO","SI","SI","SI"])
my_list = ["Formosa","607419", "605507","1912","///", "296810","295291","1519", "///"]
print(replace_bar(my_list))
#---->["Formosa","607419", "605507","1912","-", "296810", "295291","1519", "///]

import json
try:
    with open('libros_exception.json', 'r') as archivo:
        list=json.load(archivo)
        print(list)
except FileNotFoundError:
    print("El archivo JSON no se encontró.")
except json.decoder.JSONDecodeError:
    print("El archivo JSON está mal formateado.")
except Exception as e:
    print("Ocurrió un error:", e)