#利用Event类模拟红绿灯
import  threading
import  time

et=threading.Event()

def lighter():
    count=0
    et.set() #初始值设置为绿灯
    while True:
        if 5<count<=10:
            et.clear() #红灯，清楚标志位
            print("\33[41;1mred light is on...\033[0m")
        elif count>10:
            et.set() #绿灯，设置标志位
            count=0
        else:
            print("\33[42;1mgreen light is on...\033[0m")
        time.sleep(1)
        count+=1
def car(name):
    while True:
        if et.is_set():
            print("[%s] running..."%name)
            time.sleep(1)
        else:
            print("[%s] sees red light,waiting..."%name)
            et.wait()
            print("[%s] green light is on,start going..."%name)
light=threading.Thread(target=lighter,)
light.start()

car = threading.Thread(target=car,args=("MscCar",))
car.start()
