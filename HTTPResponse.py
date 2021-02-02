import urllib.request                           #导入request子模块
url = 'https://fishc.com.cn/forum.php'
response = urllib.request.urlopen(url = url)    #发送网络请求
print('状态响应码为： ', response.status)
print('响应头所有信息为： ',response.getheaders())
print('响应头指定信息为： ',response.getheader('Accept-Ranges'))
#读取HTML代码并进行utf-8解码
print('Python官网HTML代码如下：\n',response.read().decode('utf-8'))
x = input("任意键退出")