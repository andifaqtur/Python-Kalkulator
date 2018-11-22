import math
class Trigonometri:
      pass          

class Msin(Trigonometri):
    
    def __init__(self):
       print ("mode penyelesaian sin")
    
    def siIN(self,sudut):
        return math.sin(sudutS)

class Mcos(Trigonometri):
    
    def __init__(self):
       print ("mode penyelesaian cos")
    
    def coOS(self,sudutC):
        return math.cos(sudutC)
    
class Mtan(Trigonometri):
    
    def __init__(self):
       print ("mode penyelesaian tan")
    
    def taAN(self,sudutT):
        return math.tan(sudutT)




def Menu():
    print("*"*5,"kalkulator Trigonometri",5*"*")
    print("a). Sin\nb). Cos \nc). Tan\nd). Quit")
    mm= input("pilih menu :")
    return mm.lower()
while True:
    pilih = Menu()
    if pilih == 'a':
        a= Msin()
        sudutS = int (input("Masukan sudut Sin ="))
        print(" hasil Sin",sudutS,"= ",a.siIN(sudutS))
        
    elif pilih == 'b':
        b= Mcos()
        sudutC = int (input("Masukan sudut Cos ="))
        print(" hasil Cos",sudutC,"= ",b.coOS(sudutC))
        
    elif pilih == 'c':
        c= Mtan()
        sudutT = int (input("Masukan sudut Tan ="))
        print(" hasil Tan",sudutT,"= ",c.taAN(sudutT))
        
    elif pilih == 'd':
        break
    else:
        print(" anda memilih keluar")

       
