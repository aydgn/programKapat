import os
import time

t = time.localtime() # şu anki saat
saat = time.strftime("%H:%M", t)

programexe = input("Kapatılacak programı program.exe olarak yazın: ")
zaman = int(input("Kaç dakika sonra kapansın? : "))
sayac = zaman * 60

def programiKapat():
    os.system("TASKKILL /F /IM "+ programexe)
    print(f"Saat: {saat}. {programexe} kapatıldı.\n")

def geriSayim():
    while sayac > 0:
        print(sayac)
        sayac -=1

print(programexe,"kapatılacak.\n")
for i in range(sayac,0,-1):
    print (f"Programın kapanmasına {i} saniye.", end="\r")
    time.sleep(1)

programiKapat()