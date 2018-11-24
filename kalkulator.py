
import time                  #Memasukkan Package yang diperlukan
import subprocess
import aritmatika as ar
import trigonometri as tr
import kurs as kr
import bangunRuang as br


def menu():
    print("===============================")
    print("====  K A L K U L A T O R  ====") #Sebagai menu awal kalkulator
    print("====                       ====")
    print("===============================")
    print("[1] Tambah \n[2] Pengurangan \n[3] Perkalian \n[4] Pembagian \n[5] Trigonometri \n[6] Bangun Ruang \n[7] Kurs Mata Uang \n[8] Keluar")
    pilih=int(input("Pilihan :"))
    return pilih

def menuBangunRuang():
    print("===============================")
    print("====  K A L K U L A T O R  ====")
    print("====     Bangun Ruang      ====")
    print("===============================")
    print("[1] Kubus \n[2] Balok \n[3] Tabung \n[4] Kerucut")
    pilih=int(input("Pilihan :"))
    return pilih

#Program Utama


while True:
    pilih=menu()
    
    temp=subprocess.call("cls", shell=True)
    if pilih == 1 :
       op = ar.aritmatika()
       x=float(input("Bilangan Pertama :"))       #Masuk menu operasi tambah
       y=float(input("Bilangan Kedua   :"))
       print("Hasil",x,"+",y,"=",op.tambah(x,y))
       time.sleep(5)
    elif pilih == 2 :
       op = ar.aritmatika()
       x=float(input("Bilangan Pertama :"))
       y=float(input("Bilangan Kedua   :"))       #Masuk menu operasi kurang
       print("Hasil",x,"-",y,"=",op.kurang(x,y))
       time.sleep(5)
    elif pilih == 3 :
       op = ar.aritmatika()
       x=float(input("Bilangan Pertama :"))       #Masuk menu operasi kali
       y=float(input("Bilangan Kedua   :"))
       print("Hasil",x,"*",y,"=",op.kali(x,y))
       time.sleep(5)
    elif pilih == 4 :
       op = ar.aritmatika()
       x=float(input("Bilangan Pertama :"))
       y=float(input("Bilangan Kedua   :"))       #Masuk menu operasi bagi
       print("Hasil",x,":",y,"=",op.bagi(x,y))
       time.sleep(5)
    elif pilih == 5 :
       while True:                                #Masuk sub menu Trigonometri
          pilih = tr.Menu()
          temp=subprocess.call("cls", shell=True)
          if pilih == 1:
             a= tr.Msin()
             sudutS = int (input("Masukan sudut Sin ="))       #Masuk menu operasi Sin
             print("Hasil Sin",sudutS,"= ",a.siIN(sudutS),'\n')
             time.sleep(4)
    
          elif pilih == 2:
             b= tr.Mcos()
             sudutC = int (input("Masukan sudut Cos ="))       #Masuk menu operasi Cos
             print("Hasil Cos",sudutC,"= ",b.coOS(sudutC),'\n')
             time.sleep(4)
        
          elif pilih == 3:
             c= tr.Mtan()
             sudutT = int (input("Masukan sudut Tan ="))       #Masuk menu operasi Tan
             print("Hasil Tan",sudutT,"= ",c.taAN(sudutT),'\n')
             time.sleep(4)
        
          elif pilih == 4:
             break
          else:
             print('\n')
             
          temp=subprocess.call("cls", shell=True)
        
    elif pilih == 6 :
       while True:                                #Masuk sub menu Trigonometri
          pilih = br.menuBangunRuang()
          temp=subprocess.call("cls", shell=True)
          if pilih == 1:
             op= br.Volume()
             s=float(input("Masukkan Panjang Sisi Kubus (cm):"))
             print("\nKubus dengan sisi=",s,"cm \nVolumenya adalah",op.volumeKubus(s),"cm3 ","\nLuas Permukaannya adalah",op.luasKubus(s),"cm2")

             time.sleep(5)
    
          elif pilih == 2:
             op= br.Volume()
             p=float(input("Masukkan Panjang Balok(cm):"))
             l=float(input("Masukkan Lebar Balok  (cm):"))
             t=float(input("Masukkan Tinggi Balok (cm):"))
             print("Balok dengan panjang=",p,"cm, lebar=",l,"cm dan tinggi=",t,"cm \nVolumenya adalah",op.volumeBalok(p,l,t),"cm3","\nLuas Permukaannya adalah",op.luasBalok(p,l,t),"cm2")
             time.sleep(5)
        
          elif pilih == 3:
             op= br.Volume()
             r=float(input("Masukkan Panjang Jari-Jari(cm):"))
             t=float(input("Masukkan Tinggi Tabung    (cm):"))
             print("Tabung dengan jari-jari=",r,"cm dan tinggi=",t,"cm \nVolumenya adalah",op.volumeTabung(r,t),"cm3","\nLuas Permukaannya adalah",op.luasTabung(r,t),"cm2")
             time.sleep(5)
        
          elif pilih == 4:
             op= br.Volume()
             r=float(input("Masukkan Panjang Jari-Jari(cm):"))
             t=float(input("Masukkan Tinggi Kerucut   (cm):"))
             print("\nVolume Kerucut dengan jari-jari=",r,"cm dan tinggi=",t,"cm \nVolumenya adalah",op.volumeKerucut(r,t),"cm3","\nLuas Permukaannya adalah",op.luasKerucut(r,t),"cm2")
             time.sleep(5)
             
          elif pilih == 5:
             break
          else:
             print('\n')

          temp=subprocess.call("cls", shell=True)
        

    elif pilih == 7 :
       while True:
          pilih = kr.menuKurs()                        #Sub Masuk menu operasi Konversi Mata Uang
          temp=subprocess.call("cls", shell=True)
          if pilih == 1:
             b= kr.kurs()
             k = float (input("Masukan Jumlah Dollar ="))
             b.USD(k)                                  #konversi USD ke mata uang lain
             time.sleep(4)
             
    
          elif pilih == 2:
             a= kr.kurs()
             k = float (input("Masukan Jumlah Rupiah ="))
             a.Rp(k)                                   #konversi rupiah ke mata uang lain
             time.sleep(4)
             
        
          elif pilih == 3:
             c= kr.kurs()
             k = float (input("Masukan Jumlah Euro ="))
             c.EURO(k)                                 #konversi Euro ke mata uang lain
             time.sleep(4)
             
          elif pilih == 4:
             d= kr.kurs()
             k = float (input("Masukan Jumlah Yen ="))
             d.JPY(k)                                  #konversi Japan Yen ke mata uang lain
             time.sleep(4)
        
          elif pilih == 5:
             break
          else:
             print('\n')                               #penanganan jika masukan tidak sesuai pilihan
             
          temp=subprocess.call("cls", shell=True)
    elif pilih == 8 :
        break
    else:
        print(" ")

    
    temp=subprocess.call("cls", shell=True)           #membersihkan layar windows
print("T e r i m a  K a s i h .")
time.sleep(3)                                         #membekukan waktu





        
