'''
7、前置和后置
 1) 模块级，作用范围当前模块，模块中的所有用例执行前后分别运行1次前置和后置
     setup_module(),前置，所有用例执行前运行一次
     teardown_module()，后置，所有用例执行后运行一次



 2) 函数级，作用范围当前模块中的每一个测试函数，每条用例执行前后分别运行一次前置和后置
      setup_function(),前置，每条用例执行前运行一次
      teardown_function(),后置，每条用例执行后运行一次



 3) 类级， 作用范围当前类，模块中的所有用例执行前后分别运行1次前置和后置
     setup_class(),前置，所有用例执行前运行一次
     teardown_class()，后置，所有用例执行后运行一次



 4) 方法级， 作用范围当前类中的每一个测试方法，每条用例执行前后分别运行1次前置和后置
     setup_method()/setup(),前置，所有用例执行前运行一次
     teardown_method()/teardown，后置，所有用例执行后运行一次
'''
# import pytest#模块级的例题      这个是模块前后各一次
# def setup_module():
#     print('模块级前置')
# def teardown_module():
#     print('模块级后置')
# @pytest.mark.parametrize('a'[1,2,3,4,5])
# def test(a):
#     print(a)
# if __name__ =='__main__':
#     pytest.main(['-s',__file__])



# import pytest  #函数级的例题        这个是每个每条用例前后都各有一次
# def setup_module():
#     print('模块级前置')
# def teardown_module():
#     print('模块级后置')
# def setup_function():
#     print('函数级前置')
# def teardown_function():
#     print('函数级后置')
    
# @pytest.mark.parametrize('a'[1,2,3,4,5])
# def test(a):
#     print(a)
# if __name__ =='__main__':
#     pytest.main(['-s',__file__])



# import pytest  #类级别的前置和后置例题   只作用于当前类
# class Test:
#     def setup_class():
#         print('类级前置')
#     def teardown_class():
#         print('类级后置')
#     @pytest.mark.parametrize('a'[1,2,3,4,5])
#     def test(self,a):
#         print('类级前置')
# if __name__ =='__main__':
#     pytest.main(['-s',__file__])



# import pytest#方法前后置
# def setup_method():
#     print('方法前置')
# def teardown_method():
#     print('方法级后置')

'''前后置练习'''

# import requests
# import pytest
# rq = requests.session() #会话保持
# def setup_modle():#前置登录
#     url = 'http://47.92.203.151:8080/woniusales/user/login'
#     res = requests.post(url=url,data={'username':'admin','password':'123456','verifycode':'0000'}'login-pass')
# def teardown_module():#后置，注销
#     url = 'http://47.92.203.151:8080/woniusales/user/login'   
#     rq.get(url=url)
# def query_customer(**kwargs):#会员查询
#     url = 'http://47.92.203.151:8080/woniusales/customer/search'
#     res = rq.post(url=url,data=kwargs)
#     return res.text
# def test_query_customer():
#     res = query_customer(customer='13512345678',page='1')
#     assert res
# if __name__=='__main__':
#     pytest.main(['-v',__file__])

# #商品查询
# import requests
# import pytest
# rq = requests.session() #会话保持
# def setup_modle():#前置登录
#     url = 'http://47.92.203.151:8080/woniusales/user/login'
#     res = requests.post(url=url,data={'username':'admin','password':'123456','verifycode':'0000'}'login-pass')
# def teardown_module():#后置，注销
#     url = 'http://47.92.203.151:8080/woniusales/user/login'   
#     rq.get(url=url)
# def query_goods(**kwargs):#商品查询
#     url = 'http://47.92.203.151:8080/woniusales/customer/search'
#     res = rq.post(url=url,data=kwargs)
#     return res.text
# def test_query_goods():
#     res = query_goods(barcode='6955203662897')
#     assert res
# if __name__=='__main__':
#     pytest.main(['-v',__file__])


import pytest ,requests
re = requests.session()
def setup_moduler():
    loging()
def teardown_module():#后置，注销
    url = 'http://47.92.203.151:8080/woniusales/user/login'   
    rq.get(url=url)
def query_goods(**kwargs):#商品查询
    url = 'http://47.92.203.151:8080/woniusales/customer/search'
    res = rq.post(url=url,data=kwargs)
    return res.text
def test_query_goods():
    res = query_goods(barcode='6955203662897')
    assert res
if __name__=='__main__':
    pytest.main(['-v',__file__])



