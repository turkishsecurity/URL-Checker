import sys
import urllib
import requests

site = sys.argv[2]

if sys.argv[1] in ['-u']:
	resp = requests.get(site)

print(resp.status_code)
print("200 - Çalışıyor | 403 - Giriş Yasak | 400 - Geçersiz İstek | 404 - Bulunamadı , Sitede İndex Mevcut Değil.")
