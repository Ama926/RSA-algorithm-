
# coding: utf-8

# In[8]:


#KAHDSE201F-011

import random

class rsaAlgo:

    def main():
        rsaAlgo.generateKey()

    def generateKey():
        
        #generating random large prime number
        randomList = []
        for i in range(0,50):
            n = random.randint(10,100)
            if rsaAlgo.isPrime(n) == True:    
                randomList.append(n)
        #print(randomList)
        
        #seelct 2 prime numbers for p and q    
        p = random.choice(randomList)
        print('p is: ',str(p))
        q = random.choice(randomList)
        print('q is: ',str(q))
        
        
        n = p * q
        #Eular's theorem
        phy = (p-1)*(q-1)
        print('n is: ',n)
        print('Phy is: ',phy)

        
        while True:
            #generating e
            for i in range(0,phy):
                if(1<i<phy):
                    if rsaAlgo.isPrime(i)== True:
                        if rsaAlgo.coPrime(i,phy)== True:
                            e=i
                            break

        
            if rsaAlgo.gcd(e, phy) == 1:
                break

        #calculaiting d
        d = rsaAlgo.findModInverse(e, phy)
        
        #assigning to public key and private key
        publicKey = e,n
        privateKey = d,n
    
        print('Public key: ', publicKey)
        print('Private key: ', privateKey)
        
        #invoke writefile function with passing e,d and n
        rsaAlgo.writeFiles(e,n,d)

    #checking gcd
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a


    def egcd(a, b):
        if a==0:
            return(b,0,1)
        g,y,x = rsaAlgo.egcd(b%a, a)
        return (g,x -(b//a)* y,y)

    #calculating modular invertion for find d
    def findModInverse(a, m):
        g,x,y = rsaAlgo.egcd(a, m)
        if g != 1:
            raise Exception('There\'s no any modular inverse')
        return x%m


    #checking whether it is a prime number
    def isPrime(a):
        if(a==2):
            return True
        
        elif((a<2) or ((a%2)==0)):
            return False
        
        elif(a>2):
            for i in range(2,a):
                if not(a%i):
                    return False

        return True

    #checking the number is co-prime
    def coPrime(x,y):
        return rsaAlgo.gcd(x, y) == 1


    def writeFiles(e,n,d):
        
        #converting to string, because writing into a file should be in string
        encrypt = str(e)
        decrypt = str(d)
        n = str(n)
        
       #write public key to EncryptionKey text file
        with open('EncryptionKey.txt', 'w') as encryptFile:
            encryptFile.write(encrypt)
            encryptFile.write(",") 
            encryptFile.write(n)
            encryptFile.write(",")
            encryptFile.close()
            
        #write private key to DecryptionKey text file
        with open('DecryptionKey.txt', 'w') as decryptFile:
            decryptFile.write(decrypt)
            decryptFile.write(",")
            decryptFile.write(n)
            decryptFile.write(",")
            decryptFile.close()

rsaAlgo.main()

