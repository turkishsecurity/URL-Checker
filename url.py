import urllib
from urllib import request
import os
import time

os.system("sudo apt-get install figlet")
os.system("clear")
print("------------------------------")
os.system("figlet XALE")
print(" ")
print("URL Durumu Kontrol Etme Aracı - URL Checker ")
print("------------------------------")
print(" ")
site = input("Hedef Site: (Örnek: google.com Veya www.google.com)>
print("[1] HTTP") 
print("[2] HTTPS")
slct = input("Hangisi? (Default: 1) ")

if slct == "1":
 target = "http://" + site

elif slct == "2":
 target = "https://" + site 

else:
 print("Yanlış Seçim , Tekrar Deneyin.")

resp = request.urlopen(target)
print(resp.code)

print("200 - Çalışıyor | 403 - Giriş Yasak | 400 - Geçersiz İstek | 404 - Bulunamadı , Sitede İndex Mevcut Değil.")
