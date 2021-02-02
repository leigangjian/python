#导入模块
from selenium import webdriver
import pandas as pd
# 打开浏览器 实例化对象
driver=webdriver.Chrome()
# 访问网址
driver.get('https://music.163.com')
# 在新标签页 打开网址
driver.execute_script("window.open('https://music.163.com/#/song?id=1426361558')")
# 窗口切换
# 首先要获取窗口 对象
handles=driver.window_handles
# 切换标签
driver.switch_to_window(handles[-1])
# 发现有 ifram,需要切换到iframe中
# driver.switch_to_frame('iframe的id')
# driver.switch_to_frame('iframe的name')
# driver.switch_to_frame('driver.find_element_by_(" ")的到的对象')
driver.switch_to_frame('g_iframe')
parent=driver.find_element_by_class_name('cmmts')
# 如果 爬内层 itm,用css选择器
divs=parent.find_elements_by_css_selector('div.itm')
mylist=[]
for each_div in divs:
    mylist.append(each_div.find_element_by_class_name('cnt').text)
mylist
# 将列表转换为数据框
df = pd.DataFrame(mylist)
# 查看输出结果
print(df)
# 存入csv文档
df.to_csv('output.csv', encoding='utf-8', index=False)
x = input("请输入任意键退出")
