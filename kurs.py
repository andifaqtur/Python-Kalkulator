import data as dt
class kurs():
        def __init__(self):
            print("===============================") #judul menu
            print("====  K A L K U L A T O R  ====")
            print("====    Kurs Mata Uang     ====")
            print("=============================== \n")
        
        def Rp(self,k):                              #fungsi konversi rupiah ke mata uang lain
            teks = "\n{} IDR = {} EUR \n{} IDR = {} USD \n{} IDR = {} JPY \n---------------------".format(k,k*0.000061,k,k*0.000069,k,k*0.007766)
            print(teks)
            outputFile=dt.data()
            outputFile.dataSaver(teks)
        def USD (self,k):                            #fungsi konversi dolar ke mata uang lain
            teks = "\n{} USD = {} EUR \n{} USD = {} IDR \n{} USD = {} JPY \n---------------------".format(k,k*0.88,k,k*14544.54,k,k*112.95)
            print(teks)
            outputFile=dt.data()
            outputFile.dataSaver(teks)       
        def EURO (self,k):                           #fungsi konversi euro ke mata uang lain
            teks = "\n{} EUR = {} IDR \n{} EUR = {} JPY \n{} EUR = {} USD \n---------------------".format(k,k*16492,k,k*128.12,k,k*1.13)
            print(teks)
            outputFile=dt.data()
            outputFile.dataSaver(teks)
        def JPY (self,k):                           #fungsi konversi yen ke mata uang lain
            teks = "\n{} JPY = {} EUR \n{} JPY = {} USD \n{} JPY = {} IDR \n---------------------".format(k,k*0.0078,k,k*0.0089,k,k*129.22)
            print(teks)
            outputFile=dt.data()
            outputFile.dataSaver(teks)
def menuKurs():                                     #fungsi submenu kurs
        print("===============================")
        print("====  K A L K U L A T O R  ====")
        print("====    Kurs Mata Uang     ====")
        print("===============================")
        print('[1] US Dollar \n[2] Rupiah \n[3] Euro \n[4] Japan Yen \n[5] <<Kembali')
        pilih=int(input('Pilihan :'))
        return pilih

    



       
