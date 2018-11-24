import math

class Msin():
    
    def __init__(self):
       print("===============================")
       print("====  K A L K U L A T O R  ====")
       print("==== mode penyelesaian sin ====")
       print("=============================== \n")
    
    def siIN(self,sudutS):
        return math.sin(sudutS)

class Mcos():
    
    def __init__(self):
       print("===============================")
       print("====  K A L K U L A T O R  ====")
       print("==== mode penyelesaian cos ====")
       print("=============================== \n")
    
    def coOS(self,sudutC):
        return math.cos(sudutC)
    
class Mtan():
    
    def __init__(self):
       print("===============================")
       print("====  K A L K U L A T O R  ====")
       print("==== mode penyelesaian tan ====")
       print("=============================== \n")
    
    def taAN(self,sudutT):
        return math.tan(sudutT)




def Menu():
    print("===============================")
    print("====  K A L K U L A T O R  ====")
    print("====     Trigonometri      ====")
    print("===============================")
    print("[1] Sin \n[2] Cos \n[3] Tan \n[4] <<Kembali")
    mm= int(input("Pilihan :"))
    return mm


       
