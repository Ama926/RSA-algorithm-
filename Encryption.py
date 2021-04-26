
# coding: utf-8

# In[17]:


#KAHDSE201F-011

class Encrypt:

    def main():
        #get file names into an array
        fileArray = []
        encrypt = "EncryptionKey"
        fileArray.append(encrypt)
        
        plain = "plainText"
        fileArray.append(plain)

        cipher = "cipher"
        fileArray.append(cipher)
        
        print('File arrray', fileArray)
        
        #Encrypt.readEncryptFile(encrypt,plain,cipher)
        Encrypt.readEncryptFile(fileArray)
        
        
    def readEncryptFile(fileArray):
        encrypt=fileArray[0]
        plain=fileArray[1]
        cipher=fileArray[2]
    
        Encryptfile = open(encrypt +".txt", 'r')
        
        #print("Encrypte key file: ", Encryptfile)
        for line in Encryptfile:
            fields = line.split(",")
            e=fields[0]
            n=fields[1]
            
        #converi=ting into array because it already in string format
        eInt = int(e)
        nInt = int(n)
        print("e is: ",eInt)
        print("n is: ",nInt)
        
        Encrypt.readPlainText(plain, cipher, eInt, nInt)
        
        
    def readPlainText(plain, cipher, eInt, nInt):

        file = open(plain+".txt", 'r')
        for line in file: 
            #separate into words
            splitedLine = line.split()
            
        letters=[]
        texts=[]
        
        for i in range (0,len(splitedLine)):
            #separate into letters
            sli = splitedLine[i]

            for k in range (0,len(sli)):
                letters = list(sli)
                texts.append(letters[k])
     
        print("letters: ", texts)
        length = len(texts)
        Encrypt.encryption(cipher,length,texts,eInt,nInt)
   

    
    def encryption(cipher,length,texts,eInt,nInt):

        numberCode =[]
        for i in range(0,length):
            #converting to ascii
            code=ord(texts[i])
            numberCode.append(code)
            
        print("letters is ascii: ",numberCode)
        
        x=[]
        for y in range(0,len(numberCode)):
            
            Encryption = (numberCode[y]**eInt)%nInt
            binaryEncryptCode = bin(Encryption)
            x.append(binaryEncryptCode)
            
            g = str(x[y])
            
            #writing ciphered text to file
            with open(cipher + ".txt", 'a') as cipherText:
                cipherText.write(g)
                cipherText.write(",")
                

        cipherText.close() 
            
        print(x)
        
        
Encrypt.main()       

