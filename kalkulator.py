import time
import subprocess
class kall():
    x=0
    y=0
    def __init__ (self):
        print("==============================")
        print("===  K A L K U L A T O R  ====")
        print("==============================")    
    def tambah(self,x,y):
        return x+y
    def kurang(self,x,y):
        return x-y
    def kali(self,x,y):
        return x*y
    def bagi(self,x, y):
        return x/y

def menu():
    print("==============================")
    print("===  K A L K U L A T O R  ====")
    print("==============================")
    print("[1] Tambah \n[2] Pengurangan \n[3] Perkalian \n[4] Pembagian \n[5] Keluar")
    pilih=int(input("Pilihan :"))
    return pilih

#Program Utama


while True:
    pilih=menu()
    
    temp=subprocess.call("cls", shell=True)
    if pilih == 1 :
       op = kall()
       x=float(input("Bilangan Pertama :"))
       y=float(input("Bilangan Kedua   :"))
       print("Hasil",x,"+",y,"=",op.tambah(x,y))
    elif pilih == 2 :
       op = kall()
       x=float(input("Bilangan Pertama :"))
       y=float(input("Bilangan Kedua   :"))
       print("Hasil",x,"-",y,"=",op.kurang(x,y))
    elif pilih == 3 :
       op = kall()
       x=float(input("Bilangan Pertama :"))
       y=float(input("Bilangan Kedua   :"))
       print("Hasil",x,"*",y,"=",op.kali(x,y))
    elif pilih == 4 :
       op = kall()
       x=float(input("Bilangan Pertama :"))
       y=float(input("Bilangan Kedua   :"))
       print("Hasil",x,":",y,"=",op.bagi(x,y))
    elif pilih == 5:
        break
    else:
        print("Anda Memilih Keluar....")

    time.sleep(5)
    temp=subprocess.call("cls", shell=True)

print("Good Bye")




        
