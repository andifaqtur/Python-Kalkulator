class rumus :
    def menu(self):
        print '''
        =====BANGUN RUANG=====
        ======================
        1.LINGKARAN
        2.PERSEGI
        3.PERSEGI PANJANG
        4.BALOK
        ======================
        '''
        pil = input('Masukan Pilihan Anda : ')
        print '\n'
        if (pil==1):
            print '=======LINGKARAN======'
            bangun.lingkaran()
            bangun.ulang()
        elif (pil==2):
            print '=======PERSEGI======='
            bangun.persegi()
            bangun.ulang()
        elif (pil==3):
            print '=======PERSEGI PANJANG======='
            bangun.persegi panjang()
            bangun.ulang()
        elif (pil==4):
            print '=======BALOK======='
            bangun.balok()
            bangun.ulang()
        else :
            print 'Pilihan tidak tersedia'
    def ulang(self):
        print 'n/==================================='
        ulang = raw_input('apakah anda ingin mencoba lagi [Y/N] : ')
        print '=====================================/n'
        if (ulang=='Y' or ulang=='N'):
            bangun.menu()
        elif (ulang=='n' or ulang=='N'):
            print 'Thank you !'
            quit()
        else :
            print 'pilih [Y/N]'
            bangun.ulang()
    def Lingkaran(self):
        r = float(input('Masukan Nilai Jari-jari : '))
        LuasL = 3.14*r*r
        print 'Luas Lingkaran dengan jari-jari',r,'adalah'luasL

    def Persegi(self):
        s = input('Masukan Nilai sisi Persegi : '))
        LuasP = s*s
        print 'Luas dari persegi dengan sisi',s,'adalah'LuasP

    def Persegi Panjang(self):
        P = input('Masukan Nilai Panjang : ')
        l = input('Masukan Nilai Lebar : ')
        LuasPP =P*l
        print 'Luas dari persegi panjang',p,'dan lebar',1,'adalah',luasPP
 
    def Balok(self):
        p = input('Masukan Nilai Panjang  : ')
        l = input('Masukan Nilai Lebar    : ')
        t = input('Masukan Nilai Tinggi   : ')
        LuasB = p*l*t
        print 'Nilai Balok dengan Panjang'
        print ',lebar' ,1,
        print ',tinggi' ,t,
        print 'adalah' ,luasB


    Bangun = rumus()
    bangun.menu()
    bangun.lingkaran()
    bangun.persegi()
    bangun.persegi panjang()
    bangun.balok()
        
    
        
