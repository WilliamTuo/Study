'''固件（fixture），跨脚本实现相同的前置和后置
1、 在项目目录下创建文件conftest.py
2、 在文件conftest.py 中创建fixture，实现前置和后置
   @pytest.fixture([name,scope,params,autouse])
   def function()
   ...
   __name ,固件名称，如果不指定则默认被装饰的函数名
  ---scope，固件作用范围，包括module、class/function（默认）session、package
   --params，
   ---autouse，如果设置为TRUE，则可以自动调用fixture参数'''

import requests,pytest 
@pytest.fixture(name='ll',scope='module')
def login_logout():
    re = requests.session()
    url = 'http://47.92.203.151:8080/woniusales/user/login'  
    rq.post(url=url,data={'username':'admin','password':'123456','verifycode':'0000'}'login-pass'],)
    yield rq
    url = 'http://47.92.203.151:8080/woniusales/user/login'
    rq.get(url=url )




'''测试报告
1、模块：pytest-html
2、使用：在main函数中添加参数--html=path/file.html,在指定目录下生成1个html文件'''

import pytest
if __name__ =='__main':
    pytest.main(['-v','-k woniusales','html=./req.html','./'])