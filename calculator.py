from time import *
def chushihua():
    print("欢迎使用计算器")
    sleep(1)
    print('加载中')
    sleep(0.5)
    print('加载中/')
    sleep(0.5)
    print('加载中//')
    sleep(0.5)
    print('加载中///')
    sleep(0.5)
    print('加载中////')
    sleep(0.5)
    print('加载中/////')
    sleep(0.5)
    print('加载成功//////')
    sleep(0.8)
    print('加载成功       ')
    sleep(0.8)
    print('加载成功//////')
    sleep(0.8)
    print('加载成功       ')
    sleep(1.0)
   
def add(x, y):
   
 
   return x + y
 
def subtract(x, y):
   
 
   return x - y
 
def multiply(x, y):
   
 
   return x * y
 
def divide(x, y):
   
 
   return x / y

def power(x, y):
   
 
   return x ** y

while True: 
   chushihua() 
   print("请选择运算模式：")
   sleep(0.5)
   print("1、相加")
   sleep(0.5)
   print("2、相减")
   sleep(0.5)
   print("3、相乘")
   sleep(0.5)
   print("4、相除")
   sleep(0.5)
   print('5、次方')
   sleep(0.5)
   print("off、关机")
   sleep(1) 
   choice = input("输入你的选择(1/2/3/4/5/off):")
   if choice=='off':
      print("&#10084;关机成功，感谢您的使用！&#10084;")
      break
   num1 = int(input("输入第一个数字: "))
   num2 = int(input("输入第二个数字: "))
    
   if choice == '1':
      print('正在计算.')
      sleep(0.5)
      print('正在计算..')
      sleep(0.5)
      print('正在计算...')
      sleep(0.5)
      print('正在计算....')
      sleep(0.7)
      print(num1,"+",num2,"=", add(num1,num2))
      sleep(0.5)
      print('计算成功.....')
      
    
   elif choice == '2':
      print('正在计算.')
      sleep(0.5)
      print('正在计算..')
      sleep(0.5)
      print('正在计算...')
      sleep(0.5)
      print('正在计算....')
      sleep(0.7)
      print(num1,"-",num2,"=", subtract(num1,num2))
      sleep(0.5)
      print('计算成功.....')
      
    
   elif choice == '3':
      print('正在计算.')
      sleep(0.5)
      print('正在计算..')
      sleep(0.5)
      print('正在计算...')
      sleep(0.5)
      print('正在计算....')
      sleep(0.7)
      print(num1,"*",num2,"=", multiply(num1,num2))
      sleep(0.5)
      print('计算成功.....')
      
    
   elif choice == '4':
      print('正在计算.')
      sleep(0.5)
      print('正在计算..')
      sleep(0.5)
      print('正在计算...')
      sleep(0.5)
      print('正在计算....')
      sleep(0.7)
      print(num1,"**",num2,"=",divide (num1,num2))
      sleep(0.5)
      print('计算成功.....')
      
    
   elif choice == '5':
      print('正在计算.')
      sleep(0.5)
      print('正在计算..')
      sleep(0.5)
      print('正在计算...')
      sleep(0.5)
      print('正在计算....')
      sleep(0.7)
      print(num1,"**",num2,"=", power(num1,num2))
      sleep(0.5)
      print('计算成功.....')
      
      
   else:
      print("输入错误")
      sleep(0.5)
      print("输入错误")
      sleep(0.5)
      print(“输入错误")
      continue