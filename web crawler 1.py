import urllib.request

response=urllib.request.urlopen("http://www.fishc.com")
html=response.read()
html=html.decode("utf-8")
print(html)
x = input("请输入任意键退出")