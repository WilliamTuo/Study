
# class B:
#     a = 10
#     def __init__(self):
#         self.b = 20
#     def f(self):
#         print(123)
# class A:
#     def __init__(self,obj):
#         self.obj = obj
#     def fa(self):
#         print(self.obj.a)
#         print(self.obj.b)
#         self.obj.f()
# obj_b = B()
# obj_a = A(obj_b)
# obj_a.fa()
# class C:
#    gh = 78
#    def f1(self):
#        print(12345)
#    def f2(self,obj):
#        obj.f9()
# class D:
#    def f9(self):
#        print(67890)
#    def f2(self,obj):
#        obj.f1()
#    def f3(self,obj):
#        obj.f1()
# class E:
#    def f9(self):
#        print(67)
# d = D()
# c = C()
# e = E()
# d.f3(c)
# #c.f2(d)
# c.f2(e)



# class HuMan:
#     name = ''
#     height = 1.5
#     weight = 60
#     sex = 0
#     def gaiMing(self, newName):
#         self.name = newName
#     def __str__(self) -> str:
#         return ' '.join(('%s' % item for item in self.__dict__.values()))

# h = HuMan()
# h.name = "张飞"
# h.height = 1.8
# h.weight = 60
# h.sex = 0
# print(h)

# h.gaiMing("积分龙")
# print(h)







# 有时间搞
# '''图书管理系统
# 公共方法:登录、注册
# 普通用户：借阅图书、查询图书、查询借阅信息、归还图书
# 管理员：借阅图书、查询图书、查询借阅信息、归还图书、添加图书、删除图书
# 0000P:先实现类再把每个类需要的方法写出来，再根据业务流程把对应的方法，对象，实例化过后调7.50分没有听清楚用中写出对应的属性'''

# class Public:  #公共方法
#     def login(self):#登录方法，
#         user = input('用户名')
#         pwd = input('密码')
#         if user and pwd #检查用户名与密码是否正确
#             return '当前登录用户的角色'
#     def reg(self):#注册方法
#         pass
# class Ordinary:#普通用户
#     def __init__(self):
#         self.service = {'1':self.borrow,'2':self.back,'3':self.query_book,'4':self.query_borrow_info}#创建一个service属性,不能加括号加了表示调用方法
#     def borrow(self):#借阅方法
#         print('借书')
#     def back(self):#查询图书
#         print('还书')
#     def query_book(self):#查询借阅信息
#         pass 
#     def query_borrow_info(self):#归还图书
#         pass
# class Administrator(Ordinary):#继承普通用户并且在后面添加管理员权限方法
#      def __init__(self):
#         self.service = {'1':self.borrow,'2':self.back,'3':self.query_book,'4':self.query_borrow_info,
#                         '5':self.add,'6':self.delete}#创建一个service属性,不能加括号加了表示调用方法
#     def add(self):#添加图书
#         pass
#     def delete(self):#删除图书
#         pass
# if __name__ == '__main__':#不懂main是什么意思
#     pub = Public()#实例化公共方法这个类，注意实例化的格式
#     if input('1-登录 2-注册：') == '1':
#         role = pub.login()#，返回现在登录的角色
#     else:
#         pub.reg() #登录
#     role = '管理员'
#     if role == '普通用户':#判断是不是普通用户，（是普通用户就实例化普通用户，否则实例化管理员用户）
#         ord == Ordinary()#实例化普通用户
#         print('1-借书 2-还书 3-查询图书 4-查询借阅信息')#打印一下
#         server = input('请选择服务：')
#         ord.service[server]()#通过ord这个对象访问service这个属性
#     else:
#         admin = Administrator()#实例化管理员用户
#         print('1-借书 2-还书 3-查询图书 4-查询借阅信息 5-添加图书 7-删除图书')#打印一下
#         server = input('请选择服务：')
#         admin.service[server]()

#老虎和羊的游戏
# '''分析
# 对象有哪些--饲养员、老虎、羊、房间
# 饲养员：属性（描述类的静态特征：有类属性（在方法外部声明 ，类的每个对象都有，并且值相同通过类名或者对象都能访问）、
# 实例属性（在方法内部声明，类的每个对象都有但值可能不同，只能通过对象访问）属性-姓名
# 方法（描述类的动态特征，：类方法，实例方法默认带一个self参数，静态方法
# 老虎：
# 羊
# 房间'''
# #先写类
# import random,time 
# class Tiger:#老虎类1
#     def __init__(self,name,weight=500):#老虎的基本属性weight默认500
#         self.name = name
#         self.weight = weight
#     def food(self,f):#老虎要吃东西但是不知道饲养员喂什么就给一个形参f表示食物的类型
#         if f == '肉':#判断老虎吃的是不是肉，是的话就加10斤不是就减掉10斤
#             self.weight += 10
#         else:
#             self.weight -= 10
#     def call(self):#定义一个叫唤的方法
#         print('嗷嗷嗷')#老虎要叫唤饲养员才知道是什么动物
#         self.weight -= 5#叫唤消耗体力所以要-5
# class Sheep:#羊
#     def __init__(self,name,weight=200):#羊的基本属性
#         self.name = name
#         self.weight = weight
#     def food(self,f):#老虎要吃东西但是不知道饲养员喂什么就给一个形参f表示食物的类型
#         if f == '草':#判断羊吃的是不是草，是的话就加10斤不是就减掉10斤
#             self.weight += 10
#         else:
#             self.weight -= 10
#     def call(self):#定义一个叫唤的方法
#         print('绵绵绵')#羊要叫唤饲养员才知道是什么动物
#         self.weight -= 5#叫唤消耗体力所以要-5
# class Breeder:#饲养员类
#     def knock(self,animal):#animal为老虎或者羊类的对象，方法需要调用的对象（animal传到实例方法中）
#         mark = input('敲门请按1,否则请按其它键：')
#         if mark == '1':
#             #饲养员选择敲门，则调用动物类的call方法（叫唤的方法）方法通过对象调用
#             animal.call()#调用call方法用对象animal调用
#     def food(self,animal):#喂食的方法,animl同上
#         mark = input('1-肉 2-草')#选择喂他吃啥
#         '''字典可以帮我们少写很多if，else，为什么不懂'''
#         #饲养员喂食，调用动物类的food吃东西方法知道是什么动物然后喂他吃东西
#         if mark == '1':
#             f = '肉'
#         else:
#             f = '草'
#         animal.food(f)#因为不同动物吃的东西不同所以要传参
# class Room:#房间
#     def __init__(self,no,animal):#为啥要用init,no 房间号
#         self.no = no 
#         self.animal = animal#animal是老虎或者羊类的对象
# '''把animl对象传到room类的构造方法里 不懂不懂'''
# #类写好了主程序要要开始了
# if __name__ == '__main__':#这是啥不懂不懂不懂
#     #111111、生成10个房间。在每个房间中随机放入老虎或者羊
#     rooms = []         #保存10个房间 ，要导入random和time模块 不懂他们是干啥的不懂不懂不懂不懂
#     for i in range(10):        #生成10个房间（创建10个room类的对象）{{循环10次每循环一次随机创建一个老虎或者羊的对象问问问}}
#         if random.randint(0,1) == 1:       #生成0或者1之间的一个数如果等于一就创建一个如下
#             animal = Tiger(f'胖虎{i}')    #（创建老虎类的对象）启动她需要名字这些为什么要这些东西不能就一个括号吗不懂不懂不懂
#         else:
#             animal = Sheep(f'小羊{i}')      #创建sheep羊对象
#         room = Room(i+1,animal)         #创建房间类对象，实现房间与动物的绑定
#         rooms.append(room)         #将生成的room类对象保存在rooms列表中不懂不懂不懂
#     # for i in rooms:
#     #     print(i.no,i.animal)这是干啥的不懂不懂
#     #222222饲养员喂食
#     breeder = Breeder()#创建饲养员类对象，实例化
#     start = time.time()#????????
#     while time.time() - start <= 60:
#         r = random.choice(rooms) #随机生成一个房间
#         print(f'当前房间号：{r.no}') 
#         breeder.knock(r.animal)#饲养员选择是否敲门
#         breeder.food(r.animal)#饲养员喂食
#     #输出结果
#     print('*'*30)
#     for i in rooms:#i就是每个房间内的对象
#         print(f'房间：{i.no:2}\t动物:{i.animal.name}\t体重:{i.animal.weight}')#打印出每个房间动物的类型,为啥是i

    

# '''士兵进行射击训练，统计在一分钟内的射击次数、总成绩（每次射击成绩在8-10环）
# 枪的弹夹容量为10，换弹夹需要三秒
# 没次射击后随机调整一到三秒才能开下一枪
# 枪（属性：名称、子弹数量：方法--开枪，装弹）
# 士兵（属性==姓名、射击次数、成绩  方法--开火、装弹）'''
# import random ,time #需要计算时间和需要随机数所以得倒入这两个模块
# class GUn:#先声明两个类
#     def __init__(self,name,bullet=10):#定义方法传进两个实例属性
#         self.name = name
#         self.bullet = bullet#声明实例属性 bullet子弹
#     def fire(self):#  开火的方法
#         if self.bullet > 0: #子弹数量大于0
#             self.bullet -= 1 #每调用一次fire方法子弹数量减一
#     def add(self):#换子弹方法
#         self.bullet = 10 #每调用一次子弹变成10
# class Soldier:#士兵类
#     def __init__(self,name,gun):#属性定义难道一定要用init吗？定义属性和方法的区别不懂不懂不懂
#         self.name= name 
#         self.gun = gun #枪类的对象类的方法就用小写吗？gun为啥能代表Gun类的对象
#         self.count = 0#射击的次数
#         self.score = 0#射击的总成绩，为什么init括号里面没有score和count不应该写进去吗不懂 不懂不懂
#     def fire(self):#士兵的方法
#         if self.gun.bullet >0:
#             self.gun.fire()#调用枪类fire的方法进行射击
#             self.count += 1#更新射击次数
#             result  = random.randint(8,10)#更新射击总成绩不懂不懂不懂
#             self.score += result#10.50秒的时候重新看
#             print(f'射击次数：{self.count:2}\t成绩:{result}环')
#             time.sleep(random.randint(1.3))#每次射击过后要调整一到三秒，他说可以放在外面但是我放这里就错了
#         else:
#             self.add()#没有子弹了要调用装弹的方法#为啥可以直接调用不应该说明在枪类里写成self.gun.add（）这样


#         pass#需要调用枪的方法
#     def add(self):
#         self.gun.add()#调用枪类的add方法添加子弹
#         print('更换弹夹',end='')
#         for i in range(10):#循环10次每次添加一个子弹吗？子弹一共有10颗
#             print('.',end='')
#             time.sleep(0.3)#时间需要三秒
# #实例化他们
# if __name__ == '__main__':
#     gun = GUn('AK47')#实例化枪类
#     soldier = Soldier('张三',gun)#实例化士兵类
#     start = time.time()
#     print('训练开始'.center(30,'*'))
#     while time.time()- start <=60:
#         soldier.fire()#在小于等于六十的时候一直调用士兵类的方法
#     print('训练结束'.center(30,'*'))
#     print(f'姓名：{soldier.name}\n枪械:{gun.name}\n射击次数:{soldier.count}\n成绩:{soldier.score}')



# '''玩家与怪物
# 任意一方血量为0则战斗结束
# 对战开始后玩家先手攻击，怪物掉血。。。。。。。。
# 血量：2000-3500之间
# 攻击：300--450之间
# '''
# import random,time #倒入两个模块
# class Player:
#     def __init__(self,name):#定义他们的属性
#         self.name = name
#         self.hp = random.randint(2000,3500)#随机生成的血量
#         self.att = random.randint(300,450)#攻击值
#         self.defense = random.randint(150,250)#防御值
#     def attack(self,mon):#玩家的攻击方法
#         mon.hp = self.att-mon.defense#玩家的攻击值-怪物的防御值，为每次攻击给怪物造成的伤害
#         print(f'')
# class Monster:
#     def __init__(self,name):#定义他们的属性
#         self.name = name
#         self.hp = random.randint(2000,3500)#随机生成的血量
#         self.att = random.randint(300,450)#攻击值
#         self.defense = random.randint(150,250)#防御值
#     def attack(self,ply):#玩家的攻击方法
#         ply.hp = self.att-ply.defense#怪物攻击值-玩家的防御值，为每次攻击给玩家造成的伤害
# if __name__ == '__main__':
#     mon = Monster('小怪兽')
#     ply = Player('迪迦')
#     while True:
#         if mon.hp > 0:#怪物血量大于0的情况下，玩家继续攻击
#             ply.attack(mon)
#             if mon.hp <= 0:
#                 print(f'{ply.name}获胜')
#         if ply.hp > 0:
#             mon.attack

# import threading #这是什么模块
# import time 
# class Public:
#     def login(self,user,pwd):
#         print('登录中',end='')
#         for i in range(10):
#             print(','end='')
#             time.sleep(0.2)
#             print('')
#         if user == 'admin'and  pwd == '123456':#检查用户名与密码是否正确
#             print('success')
#         else:
#             print('Fail')
# if __name__ == '__main__':
#     put= Public()#实例化
#     th = threading.Thread(target=pub.login,args=('admin','123456'))#这个子线程的任务就是调用子线程执行loging这个函数，longing需要两个形参user，pwd
#     th1 = threading.Thread(target=pub.login,args=('admin1','123456'))#第二个子线程，可以创建多个子线程
#     th.setDaemon(True)#线程守护，如果要做线程守护那每个子线程都要做，不然是没有任何效果的
#     th1.setDaemon(True)
#     th.start()#启动子线程
#     th1.start()
#     th1.join()#线程阻塞
# '''脚本本身算一个主线程，th和th1算子线程，当子线程运行启动以后就和主线程没有任何关系了'''
#     print('主线程结束') #这句话代表主线程结束，子线程没有

# import random,time 
# class Gun:
#     def __init__(self,name,bullet=10):#属性子弹和子弹数量弹夹容量是10
#         self.name =  name 
#         self.bullet = bullet 
#     def fire(self):#开火
#         if self.bullet>0:#当子弹大于0的时候开火
#             self.bullet -= 1#每调用一次子弹减一
#     def add(self):#装弹
#         self.bullet = 10
# class Soldier:
#     def __init__(self,name,gun):
#         self.name = name
#         self.gun = gun #枪类对象
#         self.count = 0#射击次数
#         self.score = 0#射击总成绩
#     def fire(self):
#         if self.gun.fire>0:
#             self.gun.fire()
#             self.count += 1#更新射击次数
#             self.score += random.randint(8,10)#射击总成绩
#             self.score += result
#             print(f'射击次数：{self.count:2}\t\t成绩:{result:2}环')
#             time.sleep(random.randint(1,3))
#         else:
#             self.add()
#     def add(self):
#         self.gun.add()#调用枪类的add方法添加子弹
#         print('更换弹夹',emd='')
#         for i in range(10):
#             print(',',end='')
#             time.sleep(0.3)
#         print('')
# if __name__ == '__main__':
#     gun = Gun('AK47')
#     soldier = Soldier('张三',gun)
#     start = time.time()
#     print('训练开始'.center(30,"*"))
#     while time.time()-start <= 60:
#         soldier.fire()
#     print('训练结束'.center(30,"*"))
#     print(f'姓名：{soldier.name}\n枪械:{gun.name}\n射击次数:{soldier.count}\n成绩:{soldier.score}')
    




# import threading,time,random
# class Player:
#     def __init__(self,name,rate):
#         self.name = name
#         self.rate =rate#命中率
#         self.count = 0#训练次数
#         self.hit = 0#命中数
#         self.tmp = [1 if i<self.rate*100 else 0 for i in range(10000)]
#     def shoot(self):
#         r = '未命中'
#         self.count += 1
#         result = random.choice(self.tmp)
#         if result == 1:
#             self.hit += 1
#             r = '命中'
#         print(f'第{self.count:2} 次投篮----{r}')
#     def mock_rate(self):
#         for i in range(10000):
#             if i <self.rate*100:
#                 self.tmp.append(1)
#             else:
#                 self.tmp.append(0)
# def main(ply_info):
#     p = Player(ply_info[0],ply_info[1])
#     start = time.time()
#     print('训练开始'。center(30,'*'))
#     while time.time() - start <= 30:
#         p.shoot()
#         time.sleep(random.randint(1,3))
# if __name__ =='__main__':
#     players = [('姚明，78.92')]






# print('训练结束'.center(30,'*'))
# print(f'姓名{p.name}\n投篮次数:{p.count}\n命中率:{p.hit}')
# print(f'命中率：{p.hit*100/p.count:.2f}%')


# '''正则表达式，用于对字符串的复杂控制
# ---模块：re
# ---常用方法
#   1） split（pattern，string），使用与规则pattern匹配的内容将字符串string分割，返回一个列表
#   2）sub（pattern，new，string）将字符串中与规则pattern匹配内容替换，返回一个新的字符串
#   3）findall（pattern，str，控制字符），以列表返回字符串中与规则pattern匹配的内容，没有匹配的返回空列表
#      控制字符：re.I，忽略大小写；re.S，使元字符。可以匹配包括换行符（\n）在内所有字符
#   4）match(),从字符串的开头进行匹配，匹配到则返回一个对象，否则返回Nome
#   5)search(),从整个字符串的进行匹配，匹配到则返回一个对象，否则返回None

#      1 \d,匹配1个数字字符
#     2 \D,匹配1个非数字字符
#     3)\w,匹配一个单词字符（字母、数字。下划线）
#     4）\W,匹配一个非单词字符
#     5）\s,匹配一个空字符（空格、\t、\n)
#     6)\S,匹配一个非空字符'''  
# 3
# import re
# s = 'qwe1234ds4dg44%dish17df98qwe'
# print(re.split('\d+',s))
# s = re.sub('\D','',s)
# print(s)
# print(re.findall('\d',s))
# print(re.findall('\D',s))
# print(re.match('e123',s))#从字符串的开头进行匹配，匹配到则返回一个对象，否则返回Nome
# print(re.search('e12344466',s))#从整个字符串的进行匹配，匹配到则返回一个对象，否则返回None
# s = 'q_1@\t#\nqwe'
# print (re.finally('\w',s))
# print (re.finally('\W',s))
# print (re.finally('\s',s))
# print (re.finally('\S',s))

# #服务端
import socket
#指定通信协议：socket.SOCK_DGTAM,UDP协议；socket.SOCK_STREAM,TCP协议
#指定IP协议版本：spcket.AF_INET,IPV4;socket.AF_INET,IPV4 IPV4的地址是32位长度ipv6是128位
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#绑定IP与端口
ip = '127.0.0.1'#IP不会找，本地连接使用locahost或者127.0.0.1
port = 9000#端口，范围0-65535
soc.bind((ip,port))
#设置监听
soc.listen(5)#五个监听
#连接客户端连接请求：
client_obj,client_addr = soc.accept()#因为会返回socket客户端对像和地址所以得设置两个变量接收
#输出客户端信息，向客户端发送一句话
print(f'>>>{client_addr}')#打印客户端地址
client_obj.send('客户端,你好'.encode('utf'))#用客户端对象调用send方法，并进行编码

'''需要再写一个客户端导入创建'''
soc.connect((ip,port))#连接服务端  
#接受服务端消息、
msg = soc.recv(1024)#表示一次最多接受1024个字节
print(f'>>>{msg.decode("utf8")}')#打印并解码
