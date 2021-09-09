
## Paralelizacija generisana prostih brojeva

#Centralna funkcija koja generiše proste brojeve
from multiprocessing import Process, Queue, process
import queue

def generator_prostih_brojeva(n, queue):
    if n % 2 == 0:
        n+=1
    
    while True:
        for i in range(3, int(n**0.5+1), 2):
            if n%i ==0:
                break
        else:
            queue.put(n)
        
        n+=2

def multi_proces_generacije(jezgra, nfinal):
    q = Queue()
    procesi = []
    for number in range(1, jezgra+1):
        start =10**14//number
        process=Process(target=generator_prostih_brojeva, args=(start,q))
        process.start()
        procesi.append(process)
    prosti_brojevi = []
    while len(prosti_brojevi)<nfinal:
        prosti_brojevi.append(q.get())
    for process in procesi:
        process.terminate()
    return prosti_brojevi

#obezbedjivanje serijskog raspodela, preko funkcije koja se koristi u kriptografiji, uzima rezultat jedne funkcije i modifikuje ga

def proizvod_prostih(inqueue, outqueue):
    while True:
        prime_a=inqueue.get()
        prime_b=inqueue.get()
        outqueue.put(prime_a*prime_b)

def serial(jezgra, nfinal):
    procesi = []
    q1 = Queue()
    q2 = Queue()
    for number in range(1, jezgra+1):
        start =10**14//number
        process=Process(target=generator_prostih_brojeva, args=(start,q1))
        process.start()
        procesi.append(process)
    
    process = Process(target=proizvod_prostih, args=(q1,q2))
    process.start()
    procesi.append(process)

    output = []
    while len(output)<nfinal:
        output.append(q2.get())
    for process in procesi:
        process.terminate()
    return output
if __name__=='__main__':
    prosti = multi_proces_generacije(2,10)
    print('dva jezgra:',prosti)
    print(40*'==')
    prosti_serial = serial(2,10)
    print('serijski proces dva jezgra', prosti_serial)

# output:

# dva jezgra: [50000000000053, 100000000000031, 50000000000099, 100000000000067, 50000000000113, 50000000000117, 100000000000097, 50000000000143, 50000000000161, 100000000000099]
# ================================================================================
# serijski proces dva jezgra [5000000000006850000000001643, 5000000000013250000000006633, 2500000000011500000000013221, 5000000000019150000000013871, 5000000000021050000000015939, 5000000000024350000000023541, 2500000000024100000000057681, 5000000000033250000000036557, 5000000000035150000000045123, 5000000000040050000000056547]
    