def clear ():
    import os
    os.system('cls')



def KonversiUang():
    print ("")
    print ("")
    print ("\tProgram Konversi Mata Uang")
    print ("\n=================================================")
    print ("")
    print ("\nPilihan :")
    for MataUang in ("1. Rupiah","2. Dollar US","3. Euro","4. Yen","5. exit"):
        print (MataUang)
    print ("")
 

class kurs():
    
        def Rp(self,k):
            print (k,'IDR','=',k*0.000083,'EUR')
            print (k,'IDR','=',k*0.00011,'USD')
            print (k,'IDR','=',k*0.012,'JPY')
            
        def USD (self,k):
            print ("k",'USD','=',k*0.7566,'EUR')
            print ("k",'USD','=',k*9107.47,'IDR')
            print ("k",'USD','=',k*118.36,'JPY')
            
        def EUR (self,k):
            print ("k",'EUR','=',k*12037,'IDR')
            print ("k",'EUR','=',k*156.44,'JPY')
            print ("k",'EUR','=',k*1.32,'USD')
            
        def JPY (self,k):
            print ("k",'JPY','=',k*0.006,'EUR')
            print ("k",'JPY','=',k*0.008,'USD')
            print ("k",'JPY','=',k*76.94,'IDR')


    

p = input ("Masukan Pilihan : ")
if (p == "1"):
        k = input ("Masukan nilai Rupiah : ")
        hasil = kurs()
        hasil.Rp(k)
        print (k,'IDR','=',k*0.000083,'EUR')
        print (k,'IDR','=',k*0.00011,'USD')
        print (k,'IDR','=',k*0.012,'JPY')
        print ("\n=================================================")
        print ("")
        
elif (p == "2"):
        k = input ("Masukan nilai Dollar : ")
        hasil = kurs()
        hasil.USD(k)
        print ("\n=================================================")
        print ("")
        
elif (p == "3"):
        k = input ("Masukan nilai Euro : ")
        hasil = kurs()
        hasil.EUR(k)
        print ("\n=================================================")
        print ("")
        
elif (p== "4"):
        k = input ("Masukan nilai Yen :  ")
        hasil = kurs()
        hasil.JPY (k)
        print ("\n=================================================")
        print ("")
        
elif (p == "5"):
        exit


       
