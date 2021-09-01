
import urllib
from urllib import request
import os
import time

os.system("sudo apt-get install figlet")
print("------------------------------")
os.system("figlet XALE")
print(" ")
print("URL Durumu Kontrol Etme Aracı - URL Checker ")
print("------------------------------")
print(" ")
site = input("Hedef Site: ")

resp = request.urlopen(site)
print(resp.code)
print("200 - Çalışıyor | 403 - Giriş Yasak | 400 - Geçersiz İstek | 404 - Bulunamadı , Sitede İndex Mevcut Değil.")
