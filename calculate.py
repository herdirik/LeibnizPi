#Leibniz formülü ile pi hesaplama.
import threading

newPi=0
# myPi() fonksiyonu ile leibniz fomülünü kullanarak pi değerini hesaplattık.
def myPİ(n):
    global newPi
    sum=0
    deminator=0
    for i in range(n-250,n):
        deminator = (2 * (i+1) - 1)
        if ((i+1)%2==1):
            sum=sum+(1/deminator)
        else:
            sum=sum-(1/deminator)

    pi=sum*4
    newPi = newPi+ pi

#threadları oluşturduk.
thread1=threading.Thread(target=myPİ,args={250})
thread2=threading.Thread(target=myPİ,args={500})
thread3=threading.Thread(target=myPİ,args={750})
thread4=threading.Thread(target=myPİ,args={1000})
#start() fonksiyonu ile threadları başlattık.
thread1.start()
thread2.start()
thread3.start()
thread4.start()
#join() fonksiyonu ile threadları bekledik.
thread1.join()
thread2.join()
thread3.join()
thread4.join()

print(newPi)





