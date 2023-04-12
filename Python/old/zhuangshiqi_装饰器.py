'''
闭包函数：
----在一个函数（外函数）中声明了另一个函数（内函数），内函数引用了外函数的变量，外函数发那会函数引用（内函数的名字）
     1内函数，函数里面还有一个函数，外函数里面有内函数
     2内函数里面会引用外函数变量
     3外函数一定要有返回内函数的引用   满足这三点就是一个闭包函数


'''
import requests
def outer():#外函数
    a = 10 #外函数的变量是10  外函数的变量也可以是形参
    def inner():#这个就是内函数
        print(a+20)#在内函数里面必须有引用外函数变量
    return inner#外函数必须要有一个return语句，返回内函数的引用
def gf(url):#普通函数
    res = requests.get(url)
    print(res.url)
    
def f1(url):#闭包函数
    def inner():
        requests.get(url)
    return inner
if __name__ =='__main__':
    gf('http://47.92.203.151:8080/woniuseales')
    gf('http://47.92.203.151:8080/woniuseales')
    gf('http://47.92.203.151:8080/woniuseales')
    gf('http://47.92.203.151:8080/woniuseales')#普通函数每访问一次就得写一次地址要不然就会报错
f = f1('http://47.92.203.151:8080/woniuseales')#闭包函数访问每次就传一次参
f()#用f（）直接就能访问
f()


'''装饰器：
----在不改变函数或者方法源码、调用方式的前提下，为函数或者方法添加新功能
----通用的装饰器 模板
    def outer(func): func表示被装饰的函数
        def wrapper(*args,**kwargs):
            res = func(*args,**kwargs)
            return res
        return wrapper
----使用：
     @装饰器名称
     def func()
         .....
    在你想要操作的函数的头上用@加上装饰器名称，这样就给函数添加了新的功能
'''
import time 
#想要统计函数f2运行所消耗的时间
def f2():
    for i in range(1000000):
        ...
def f3():
    for i in range(1000000):
        ...
if __name__ =='__main__':
    ...
    start = time.time()
    f2()
    print(time.time()-start)
    start = time.time()
    f3()
    print(time.time()-start)
#这样调用满足功能上的需求，但是改变了代码的原程序，这样使用并不是特别友好所以得写一个装饰器

def get_run_time(func):#func表示被装饰的函数
    def wrapper(*args,**kwargs):
        start = time.time()
        res = func(*args,**kwargs)
        end = time.time()
        print(end-start)
        return res
    return wrapper

def check_login(username,passwd):#
    print(4)
    def outer(func):
        def wrapper(*args,**kwargs):
            if username =='admin' and passwd=='123456'
                res = func(*args,**kwargs)#运行被装饰的函数
                return res
            else:
                print('请使用正确的账号密码登录后使用该功能')
        return wrapper
    return outer
@check_login('admin','123456')
@get_run_time#添加的装饰器,添加了装饰器以后先跑装饰器的外函数和内函数最后子再跑被装饰的函数
def f2():
    print(1)
    for i in range(100000000):
        ...
@get_run_time
def f3():
    for i in range(1000000000):
        ...
if __name__ =='__main__':
    ...
    f2()
    f3()






'''拓展
1、 普通函数我们在每次访问的时候，都必须给他传参
2、 闭包函数只用传一次参 这样内函数就可以任意调用，'''
