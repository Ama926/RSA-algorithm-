
# coding: utf-8

# In[13]:


#KAHDSE201F-011

class Decrypt:
    
    def main():
        fileArray = []
        
        decryptKey = "DecryptionKey"
        fileArray.append(decryptKey)
        print(fileArray)
        
        cipher = "cipher"
        fileArray.append(cipher)

        decipherText = "deciphere"
        fileArray.append(decipherText)
        
        print('File arrray', fileArray)
        
        #passing file names to other functions
        Decrypt.readDecryptKey(decryptKey,cipher,decipherText)
        
        
    def readDecryptKey(decryptKey,cipher,decipherText):
        
        decryptFile = open(decryptKey + ".txt", 'r')
        for line in decryptFile:
            fields = line.split(",")
            d=fields[0]
            n=fields[1]
 
        dInt = int(d)
        nInt = int(n)
        print("d is: ", dInt)
        print("n is : ", nInt)
        
        Decrypt.readCipher(cipher,decipherText,dInt,nInt)

    def readCipher(cipher,decipherText,dInt,nInt):
        
        with open(cipher+".txt", 'r') as file:
            for line in file: 
                #separating each binary codes between in commas
                splitedLines = line.split(",")
                
        lenSL = len(splitedLines)
        Decrypt.decryption(decipherText, splitedLines, lenSL, dInt, nInt)
        
        
    def decryption(decipherText, sl, lenSL, dInt, nInt):
        
        with open(decipherText+".txt", 'a') as textDeciphered:
            numcode =[]
            for i in range(0,(lenSL - 1)):
                strCode = int(sl[i],2)
                numcode.append(strCode)

            x=[]
            print("deciphered code: ")
            for y in range(0,len(numcode)):

                m=(numcode[y]**dInt)%nInt
                x.append(m)

                code=chr(x[y])
                
                print(code)
                textDeciphered.write(code)
                
            textDeciphered.close() 
        
Decrypt.main()
        
        

