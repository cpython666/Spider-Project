from multiprocessing import Process
import multiprocessing
from time import sleep

def fun(num):
    sleep(2)
    print('Process',num)

if __name__=="__main__":
    for i in range(5):
        p=Process(target=fun,args=(i,))
        p.start()

    for p in multiprocessing.active_children():
            print('Child process name: ' + p.name + ' id: ' + str(p.pid))



    print('Process Ended')
