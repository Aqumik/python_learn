from threading import Thread
from time import sleep


process_port_list = [50301,50302,50303,50304]
def run(name):
    for x in range(10):
        print("helo "+name)
        sleep(1)
def run1():
    for x in range(5):
        print("hi")
        sleep(1)

def run3():
    for x in range(5):
        print("hiiii")
        sleep(1)

T=Thread(target=run,args=("Ayla",))
T1=Thread(target=run1)
T3=Thread(target=run3)



T.start()
sleep(0.2)
T1.start()
sleep(0.2)
T3.start()
sleep(0.2)
T.join()
T1.join()
T3.join()
print("Bye")