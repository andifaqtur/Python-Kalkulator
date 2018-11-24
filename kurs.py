class kurs():
        def __init__(self):
            print("===============================") #judul menu
            print("====  K A L K U L A T O R  ====")
            print("====    Kurs Mata Uang     ====")
            print("=============================== \n")
        
        def Rp(self,k):                              #fungsi konversi rupiah ke mata uang lain
            print ('\n')
            euro=0.000061
            usd=0.000069
            print (k,'IDR','=',k*euro,'EUR')
            print (k,'IDR','=',k*usd,'USD')
            print (k,'IDR','=',k*0.007766,'JPY')
            
        def USD (self,k):                            #fungsi konversi dolar ke mata uang lain
            print ('\n')
            print (k,'USD','=',k*0.88,'EUR')
            print (k,'USD','=',k*14544.54,'IDR')
            print (k,'USD','=',k*112.95,'JPY')
            
        def EURO (self,k):                           #fungsi konversi euro ke mata uang lain
            print ('\n')
            print (k,'EUR','=',k*16492,'IDR')
            print (k,'EUR','=',k*128.12,'JPY')
            print (k,'EUR','=',k*1.13,'USD')
            
        def JPY (self,k):                           #fungsi konversi yen ke mata uang lain
            print ('\n')
            print (k,'JPY','=',k*0.0078,'EUR')
            print (k,'JPY','=',k*0.0089,'USD')
            print (k,'JPY','=',k*129.22,'IDR')
def menuKurs():                                     #fungsi submenu kurs
        print("===============================")
        print("====  K A L K U L A T O R  ====")
        print("====    Kurs Mata Uang     ====")
        print("===============================")
        print('[1] US Dollar \n[2] Rupiah \n[3] Euro \n[4] Japan Yen \n[5] <<Kembali')
        pilih=int(input('Pilihan :'))
        return pilih

    



       
