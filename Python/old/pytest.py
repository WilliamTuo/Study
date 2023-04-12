'''
1、模块：pytest



2、使用说明
  1）脚本的名字需要以test开头
  2）函数名需要以test开头
  3）类名、方法名需要以test开头，在类中不能有构造方法
  4）assert进行断言，assert 预期 == 实际 例如assert 1==1就是判断

  


3、基本使用
   1） 作用于函数
   2） 作用于类



   
4、用例执行
   1） 启动测试
       脚本：  pytest.main([参数1，参数2，.....,文件、目录])
       命令：pytest 参数 脚本
             py.test 参数 脚本
             python -m pytest 参数 脚本
    2） 参数
         -s 
         -q
         -v下有
         -k， 通过关键字匹配脚本名、 函数名、类名、方法名 例如：（pytest.main(['-v','-k login',''./'])）
         -x， 执行测试过程中一旦有fail的用例，则立即停止测试（执行失败的用例）；例如（pytest.main(['-q','-k login','-x'__file__])）
         --maxfial = n， 执行测试过程中fail的用例数达到n，则立即停止测试 例如：（pytest.main(['-q','--maxfail=2'__file__])）
         -m， 执行指定标记的用例
              1、--在项目目录下创建一个文件： pytest.ini(意思是名字必须是这个pytest.ini)
              2、--在文件中配置用例标记 如下
                [pytest]  (指定配置)
                 markers = smoke_case （markers=必须有，smoke_case 是标记意思是冒烟测试，你想用什么标记都行用什么名字带表都可以）
                           sys_case  （系统测试，）
              3、--使用装饰器 @pytest.mark.标记  ，用来标记用例 例如（@pytest.mark.smoke_case）疑问 方法和函数类都可以使用吗？或者是任何地方方法代码里头都可以使用吗？
              4、--执行测试，-m 标记名，意思是用来执行指定用例   例如，下面代码中有自己慢慢找（pytest.main(['-v','--maxfail=2','-m smoke_case','./'])）
       
              


5、 跳过用例
    1） @pytest.mark.skip(reason=value),无条件跳过用例  例如：【@pytest.mark.skip(reason='无条件跳过')】
    2)  @pytest.mark.skipif(布尔表达式，reason=value),有条件跳过用例，当布尔表达式结果为True的情况下那这条用例就会被跳过  例如：【@pytest.mark.skipif(1==1,reason='无条件跳过')#1是等于1所以结果是为真是所以可以跳过用例】
    3） pytest。skip(msg),在方法或者函数内部使用   例如：【pytest.skip('跳过')】这个一般用在if语句里面，当瞒足某个条件下就用这个方法来跳过用例的执行
       
        
    

         
6、 参数化（每个函数就是一条用例，100个用例那就会产生100个函数，从而浪费很多资源，为了减少代码的冗余可用性就有了参数化）
----@pytest.mark.parametrize('参数1,......',value,ids)  参数是什么，就是被装饰函数里面的参数，username,passwd 就是他的参数  例如【def test_login_case1(username,passwd)】
     1、参数。为一个字符串，内容必须与被装饰的函数或者方法的形参相同
     2、value，传给参数的值，通常使用列表
     3.ids，在测试报告中设置用例名称，值为一个列表
          
           
            
 '''
import pytest
# @pytest.mark.smoke_case#使用-m第三步 -m参数
# @pytest.mark.skip(reason='无条件跳过')
# def test_login_case1():
#     print('用例1')
#     assert 1==1
# @pytest.mark.skipif(1==1,reason='无条件跳过')#1是等于1所以结果是为真是所以可以跳过用例
# def test_case2():
#     print('用例2')
#     assert 1 == 1
# def test_login_case3():
#     print('用例3')
#     assert 1==1
#     #以上是测试函数
# class Test_:#类名、方法名需要以test开头，在类中不能有构造方法
#     def test_case3(self):
#         pytest.skip('跳过')
#    # def __init__(self):不允许有构造方法    
# if __name__ == '__main__':
#     # pytest.main(['-v',__file__])#-v会显示测试用例的详细信息以及测试结果
    # pytest.main(['-s',__file__])#-s，显示测试用例中print语句的结果
    # pytest.main(['-q',__file__])#-q， 显示简略信息  __file__，当前文件
    # pytest.main(['-q','--maxfail=2'__file__])
    # pytest.main(['-v','--maxfail=2','-m smoke_case','./'])

'''参数化例题'''
import requests
#例一
case = [['admin','1234565'],['admin','123123'],['admin','']]#三个就是三个用例
@pytest.mark.parametrize('username,passwd',case)#username,passwd，下列方法的参数   case传给参数的值
def test_login_case1(username,passwd):
    print(username,passwd)
    assert 1==1

#例二
cases = [['输入有效的信息','登录成功',{'username':'admin','password':'123456','verifycode':'0000'}'login-pass'],
         ['输入错误密码','登录失败',{'username':'admin','password':'123123','verifycode':'0000'}'login-fail'],
         ['不输入密码','登录失败',{'username':'admin','password':'','verifycode':'0000'}'login-fail'],
         ['输入错误验证码','登录失败',{'username':'admin','password':'123456','verifycode':'0011'}'vcode-error'],
         ['验证码为空','登录失败',{'username':'admin','password':'123456','verifycode':''}'vcode-error']]
url = 'http://47.92.203.151:8080/woniusales/user/login'
@pytest.mark.parametrize('case',cases)
def test_login(case):
    exp, data = case[-1],case[1]
    res = requests.post(url=url,data=data)
    assert exp == res.tsxt
if __name__ =='__main__':
    pytest.main(['-v',__file__])


'''拓展
1、 -v， 显示测试执行详细信息，每条用例的执行结果
2、 -s，显示测试用例中print语句的结果
3、 -q， 显示简略信息
4、 __file__，当前文件
5 ;collecting....collceted 6 items / 1deselected / 5 selected 
意思是一共加载到六条用例，一个没被选中，五条选中了
6、 pytest.main(['-v','-k login',''./'])
       ./:当前目录下，当前目录是当前文件夹，那么里面文件的用例或者别的东西都会运行
7、 pytest单独运行一个脚本是没有问题的，但如果是目录下的他没有以test开头是不会运行他的直接就略过了


'''