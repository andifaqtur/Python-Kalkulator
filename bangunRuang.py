class luasPermukaan():           #kelas Induk

    def luasKubus(self,s):
        return 6*s*s

    def luasBalok(self,p,l,t):
        return 2*(p*l)+2*(p*t)+2*(l*t)

    def luasTabung(self,r,t):
        return 2*3.14*(r*r)+2*3.14*r*t

    def luasKerucut(self,r,t):
        return 3.14*r*(r+t)
                    

class Volume(luasPermukaan): #Kelas turunan
    def __init__(self):
        print("===============================")
        print("====  K A L K U L A T O R  ====")
        print("====     Bangun Ruang      ====")
        print("=============================== \n")
    def volumeKubus(self,s):
        return s*s*s
        
    def volumeBalok(self,p,l,t):
        return p*l*t
        
    def volumeTabung(self,r,t):
        return 3.14*r*r*t

    def volumeKerucut(self,r,t):
        return 3.14*r*r*t*1/3
        
        
def menuBangunRuang():
    print("===============================")
    print("====  K A L K U L A T O R  ====")
    print("====     Bangun Ruang      ====")
    print("===============================")
    print("[1] Kubus \n[2] Balok \n[3] Tabung \n[4] Kerucut \n[5] <<Kembali")
    pilih=int(input("Pilihan :"))
    return pilih


        
    
        
