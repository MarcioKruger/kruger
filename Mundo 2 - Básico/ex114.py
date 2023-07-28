import urllib
import urllib.request

print('===' * 15)
print('       --- O SITE ESTÁ NO AR? ---')
print('===' * 15)

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('Deu erro')
else:
    print('Deu certo!')
