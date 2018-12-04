
import time                  #Memasukkan Package yang diperlukan
import subprocess
import aritmatika as ar
import trigonometri as tr
import kurs as kr
import bangunRuang as br
import data as dt


def menu():
    print("===============================")
    print("====  K A L K U L A T O R  ====") #Sebagai menu awal kalkulator
    print("====                       ====")
    print("===============================")
    print("        Data Terakhir          ")
    dataTerakhir=dt.data()
    dataTerakhir.dataReader()
    print("[1] Tambah \n[2] Pengurangan \n[3] Perkalian \n[4] Pembagian \n[5] Trigonometri \n[6] Bangun Ruang \n[7] Kurs Mata Uang \n[8] Keluar")
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
       teks="\nHasil {} + {} adalah {} \n---------------------".format(x,y,op.tambah(x,y))
       print(teks)
       outputFile=dt.data()
       outputFile.dataSaver(teks)
       time.sleep(5)
    elif pilih == 2 :
       op = ar.aritmatika()
       x=float(input("Bilangan Pertama :"))
       y=float(input("Bilangan Kedua   :"))       #Masuk menu operasi kurang
       teks="\nHasil {} - {} adalah {} \n---------------------".format(x,y,op.kurang(x,y))
       print(teks)
       outputFile=dt.data()
       outputFile.dataSaver(teks)
       time.sleep(5)
    elif pilih == 3 :
       op = ar.aritmatika()
       x=float(input("Bilangan Pertama :"))       #Masuk menu operasi kali
       y=float(input("Bilangan Kedua   :"))
       teks="\nHasil {} x {} adalah {} \n---------------------".format(x,y,op.kali(x,y))
       print(teks)
       outputFile=dt.data()
       outputFile.dataSaver(teks)
       time.sleep(5)
    elif pilih == 4 :
       op = ar.aritmatika()
       x=float(input("Bilangan Pertama :"))
       y=float(input("Bilangan Kedua   :"))       #Masuk menu operasi bagi
       teks="\nHasil {} : {} adalah {} \n---------------------".format(x,y,op.bagi(x,y))
       print(teks)
       outputFile=dt.data()
       outputFile.dataSaver(teks)
       time.sleep(5)
    elif pilih == 5 :
       while True:                                #Masuk sub menu Trigonometri
          pilih = tr.Menu()
          temp=subprocess.call("cls", shell=True)
          if pilih == 1:
             a= tr.Msin()
             sudutS = int (input("Masukan sudut Sin ="))       #Masuk menu operasi Sin
             teks="\nHasil sin {} adalah {} \n---------------------".format(sudutS,a.siIN(sudutS))
             print(teks)
             outputFile=dt.data()
             outputFile.dataSaver(teks)
             time.sleep(4)
    
          elif pilih == 2:
             b= tr.Mcos()
             sudutC = int (input("Masukan sudut Cos ="))       #Masuk menu operasi Cos
             teks="\nHasil cos {} adalah {} \n---------------------".format(sudutC,b.coOS(sudutC))
             print(teks)
             outputFile=dt.data()
             outputFile.dataSaver(teks)
             time.sleep(4)
        
          elif pilih == 3:
             c= tr.Mtan()
             sudutT = int (input("Masukan sudut Tan ="))       #Masuk menu operasi Tan
             teks="\nHasil tan {} adalah {} \n---------------------".format(sudutT,c.taAN(sudutT))
             print(teks)
             outputFile=dt.data()
             outputFile.dataSaver(teks)
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
             teks="\nKubus dengan sisi = {} cm \nVolume Kubus = {} cm3 \nLuas Permukaan Kubus = {} cm2 \n---------------------".format(s,op.volumeKubus(s),op.luasKubus(s))
             print(teks)
             outputFile=dt.data()
             outputFile.dataSaver(teks)
             time.sleep(5)
    
          elif pilih == 2:
             op= br.Volume()
             p=float(input("Masukkan Panjang Balok(cm):"))
             l=float(input("Masukkan Lebar Balok  (cm):"))
             t=float(input("Masukkan Tinggi Balok (cm):"))
             teks="\nBalok dengan panjang = {} cm, lebar = {} cm ,dan tinggi= {} cm\nVolume Balok = {} cm3 \nLuas Permukaan Balok = {} cm2 \n---------------------".format(p,l,t,op.volumeBalok(p,l,t),op.luasBalok(p,l,t))
             print(teks)
             outputFile=dt.data()
             outputFile.dataSaver(teks)
             time.sleep(5)
        
          elif pilih == 3:
             op= br.Volume()
             r=float(input("Masukkan Panjang Jari-Jari(cm):"))
             t=float(input("Masukkan Tinggi Tabung    (cm):"))
             teks="\nTabung dengan jari-jari = {} cm dan tinggi = {} cm \nVolume Tabung = {} cm3 \nLuas Permukaan Tabung = {} cm2 \n---------------------".format(r,t,op.volumeTabung(r,t),op.luasTabung(r,t))
             print(teks)
             outputFile=dt.data()
             outputFile.dataSaver(teks)
             time.sleep(5)
        
          elif pilih == 4:
             op= br.Volume()
             r=float(input("Masukkan Panjang Jari-Jari(cm):"))
             t=float(input("Masukkan Tinggi Kerucut   (cm):"))
             teks="\nKerucut dengan jari-jari = {} cm dan tinggi = {} cm\nVolume Kerucut = {} cm3 \nLuas Permukaan Kerucut = {} cm2 \n---------------------".format(r,t,op.volumeKerucut(r,t),op.luasKerucut(r,t))
             print(teks)
             outputFile=dt.data()
             outputFile.dataSaver(teks)
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





        
