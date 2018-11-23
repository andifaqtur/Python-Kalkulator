import time
import subprocess
import aritmatika as ar
import trigonometri as tr
import kurs as kr


def menu():
    print("===============================")
    print("====  K A L K U L A T O R  ====")
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
       x=float(input("Bilangan Pertama :"))
       y=float(input("Bilangan Kedua   :"))
       print("Hasil",x,"+",y,"=",op.tambah(x,y))
       time.sleep(5)
    elif pilih == 2 :
       op = ar.aritmatika()
       x=float(input("Bilangan Pertama :"))
       y=float(input("Bilangan Kedua   :"))
       print("Hasil",x,"-",y,"=",op.kurang(x,y))
       time.sleep(5)
    elif pilih == 3 :
       op = ar.aritmatika()
       x=float(input("Bilangan Pertama :"))
       y=float(input("Bilangan Kedua   :"))
       print("Hasil",x,"*",y,"=",op.kali(x,y))
       time.sleep(5)
    elif pilih == 4 :
       op = ar.aritmatika()
       x=float(input("Bilangan Pertama :"))
       y=float(input("Bilangan Kedua   :"))
       print("Hasil",x,":",y,"=",op.bagi(x,y))
       time.sleep(5)
    elif pilih == 5 :
       while True:
          pilih = tr.Menu()
          temp=subprocess.call("cls", shell=True)
          if pilih == 1:
             a= tr.Msin()
             sudutS = int (input("Masukan sudut Sin ="))
             print("Hasil Sin",sudutS,"= ",a.siIN(sudutS),'\n')
             time.sleep(4)
    
          elif pilih == 2:
             b= tr.Mcos()
             sudutC = int (input("Masukan sudut Cos ="))
             print("Hasil Cos",sudutC,"= ",b.coOS(sudutC),'\n')
             time.sleep(4)
        
          elif pilih == 3:
             c= tr.Mtan()
             sudutT = int (input("Masukan sudut Tan ="))
             print("Hasil Tan",sudutT,"= ",c.taAN(sudutT),'\n')
             time.sleep(4)
        
          elif pilih == 4:
             break
          else:
             print('\n')
             
          temp=subprocess.call("cls", shell=True)
        
    elif pilih == 6 :
       pass
    elif pilih == 7 :
       while True:
          pilih = kr.menuKurs()
          temp=subprocess.call("cls", shell=True)
          if pilih == 1:
             a= kr.kurs()
             k = int (input("Masukan Jumlah Rupiah ="))
             a.Rp(k)
             time.sleep(4)
    
          elif pilih == 2:
             b= kr.kurs()
             k = int (input("Masukan Jumlah Dollar ="))
             b.USD(k)
             time.sleep(4)
        
          elif pilih == 3:
             c= kr.kurs()
             k = int (input("Masukan Jumlah Euro ="))
             c.EURO(k)
             time.sleep(4)
             
          elif pilih == 4:
             d= kr.kurs()
             k = int (input("Masukan Jumlah Yen ="))
             d.JPY(k)
             time.sleep(4)
        
          elif pilih == 5:
             break
          else:
             print('\n')
             
          temp=subprocess.call("cls", shell=True)
    elif pilih == 8 :
        break
    else:
        print("Anda Memilih Keluar....")

    
    temp=subprocess.call("cls", shell=True)

print("Good Bye")




        
