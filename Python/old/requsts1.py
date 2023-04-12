'''模块:requests
---get请求
   方法:get(url,params,headars,verify=Falas),返回一个对象
        url，请求地址
        params,请求参数，一般用字典传入
        headers，请求头,一般也用字典传入，
        verify=Falas,表示忽略ssl验证，主要针对HTTPS协议
请求地址参数方法得有，地址和方法必须有

    获取服务端相应：
    1) text,以字符串形式获取服务端相应内容
    2） content，以字节形式获取服务端相应内容
    3) json(), 以json获取服务端相应内容
   
----post请求
    方法：post(url,data,headars,verify=Falas)
         data :请求参数，一般用字典传入
'''

import requests
import re  #使用正则表达式需要倒入re模块
def down_image(url,left,right,path):#没有带参数的时候
    '''从指定的页面下载图片到本地
        url:请求地址
        left:图片地址左边界
        right:图片地址右边界
        path:本地保存图片的路径'''
    '''对一个页面发起请求'''
    res = requests.get(url=url,verify=False)    #对指定url（请求地址）发起get 请求【是不是对地址发起请求的意思】verify=false忽略证书
    page = res.text    #获取页面源码（什么是页面源码：源码是指编写的最开始的程序代码）以字符串形式
    '''下列   从页面源码中获取到图片地址，复制图片地址并搜索，怎么在一堆编码中获取地址，需要用到正则表达式'''
    imgs = re.findall(f'{left(.*?)ringht}'page)    #findall(一列表返回字符串中与规则pattern匹配的内容，没有匹配返回空列表)left为左边界,.*?贪婪匹配最大范围匹配左右边界，right右边界，从page里面找{使用正则表达式获取图片地址}保存在imgs里
    '''imgs就是获取到图片地址了'''
      #下载图片到本地，以下所有均是在下载图片
    
    if imgs:
        print(f'开始下载，总共{len(imgs)}张图片')     #len在集合里是返回可迭代对象中所有元素数量但是我不知道是不是对的
        for i,j in enumerate(imgs):   #i是索引 j是每一个图片地址，enumerate：是个内置函数作用是将一个可遍历的数据对象（如列表、字符串）组合为一个索引序列，同时列出数据和数据下标，这样遍历数据时，就可以同时获得索引和数据
            print(f'正则下载第{i+1:2}张图片,剩余{len(imgs)-i-1}张图片')    #i+1代表不懂不懂？？？？？
            with open(f'{path}/{i+1}.jepg','wb') as f:           #打开文件保存在path下面 i+1索引作为图片的名字 wb以二进制覆盖写的方式打开文件
              res = requests.get(url=j)       #对每个图片地址发起请求
              f.write(res.content)#'f.write是什么''以字节形式获取服务端请求的响应，并将该响应写入二进制写的方式打开的文件中'''
        else:
            print('下载完成')
    else:
        print('当前叶页面未找到图片')
def get_params(url,**kwargs):#带参数
    res =requests.get(url=url,params=kwargs,verify=False)#url请求参数 params请求参数，一般用字典传入
    print(res.url)
    print(res.text)#3分19秒抓包工具
def get_header(url,header,**kwargs):#带请求头的请求,header请求头
    res =requests.get(url=url,params=kwargs,verify=False,headers=header)
    print(res.text)#打印带请求头结果
 
def zentao_login(url,**kwargs):#post方法
    res = requests.post(url=url,data=kwargs)
    print(res.text)
    print(res.json())#获取服务端相应的JSON数据

def query_customer(url,**kwargs):#会员查询 地址加参数



if __name__=='__main__':
    # url ='https;//www.dgtle.com/article-1577853-1.html'
    # '''https地址带有安全界面的请求,需要用verify=False忽略证书'''
    # # down_image(url,'original="','"class=','./imgs')        #将url传进来，original="左边界，"class=右边界，保存在当前路径imgs下（需要重新新建一个imgs目录）
    # # requests.get(url='https;//www.dgtle.com/article-1577853-1.html')     #对这个图片发起请求
    # # print(res.content)#不懂
    # url = 'http://www.bigidu.com/daidu'#请求地址
    # # get_params(url=url,q='蜗牛学院',word='蜗牛学院')#带参数，Word是地址吗？
    # url='heeps://movie.douban.com/chart'
    # header = {'请求头'}
    # get_header(url,header)

    # res = requests.get(url=url,verify=False)
    # print(res.text)
    url='请求头'
    zentao_login(url=url,username='admin',password='123344',verifycode='0000')#密码正确




'''一、扩展enumerate:这是个内置函数多用于for循环中得到计数，利用她可以同时获得索引和值,即需要index和value值的时候可以使用她，下标和值例如0 小明 0就是index小明就是value
   二、with open语句，上下管理工具，可以实现自动关闭文件、语法whit open(filn[,mode=type,encoding=编码])asf：
file：待打开的文件（传入的路径必须指向一个文件
mode：type，打开的方式默认认为只读
type：有常用的四种类型
                    1、r：只读如果指定的文件不存在系统将报错
                    2、w：覆盖写，如果指定的文件不存在系统会自动创建该文件
                    3、a：追加写，如果指定的文件不存在系统会自动创建该文件
                    4、b：二进制一般用于图片类型文件
    三、请求头：告诉服务器关于客户端环境和请求正文相关的一些信息，例如浏览器版本，请求参数的长度,有的会反爬虫，得伪装成浏览器所以得需要请求头
    四、get请求和post请求的区别get请求一般用于在服务器上获取资源 post请求一般向服务器提交资源登录、正删改这些，传参不同                                       
'''