from multiprocessing import Process
class A(object):
    def __init__(self):
        print('创建了一个A类')
    def f(self):
        print('方法')

a=A()
def fun():
    a.f()

if __name__ =="__main__":
    for i in range(5):
        p=Process(target=fun)
        p.start()
        p.join()