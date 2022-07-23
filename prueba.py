Created on 18 abr. 2021

@author: jaume
'''
area = 1973.9208802178716

areaf = '{:,.2f}'.format(area)
areafesp =  '{:,.2f}'.format(area).replace(",", "@").replace(".", ",").replace("@", ".") # reemplaza punos y comas

print("Numero original: ", area)    # Numero original
print("Numero formateado en Ingles: ", areaf, "€")    # Numero formateado ingles
print("Numero formateado en Español: ", areafesp, "€")    # Numero formateado español
