"""
Crie um código em Python que testaa se o site Pudim está acessível pelo
computador usado.
"""


import urllib
import urllib.request


try:
    site = urllib.request.urlopen("http://www.pudim.com.br")
except urllib.error.URLError:
    print("O site Pudim não está acessível no momento, tente mais tarde.")
else:
    print("O site Pudim está acessível. que pudim horrível. Renan não aprova")
    print(site.read()) # aqui você consegue ler o codigo do site
