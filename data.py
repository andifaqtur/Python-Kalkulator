class data:
    def dataSaver(self,text):
        file=open("data.txt", "w")
        file.write(text)
        file.close()
    def dataReader(self):
        file=open("data.txt", "r")
        text=file.read()
        print(text)
                  
