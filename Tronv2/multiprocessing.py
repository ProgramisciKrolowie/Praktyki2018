import multiprocessing
import threading
import time



def a(event):
    time.sleep(3)
    print("a")
    event.set()



def b(event):
    event.wait()
    print(b)
    event.clear()


if __name__ == '__main__':
    event = threading.Event()
    processes = []
    t = multiprocessing.Process(target=a(event), args= ( ) )
    processes.append(t)
    t.start()
    x = multiprocessing.Process(target=b(event), args= ( ) )
    processes.append(x)
    x.start()

    for one_process in processes:
        one_process.join()
    print("Czemu mnie ranisz")
