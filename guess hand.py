import random
youturn=['石头','剪刀','布']
c=0
pc=0
win_list=['12','23','31']
shitoujiandaobu=['1','2','3']
a = (['1', '2', '3'])
name = input('请输入名称')
while True:
    computer=random.choice(['1','2','3'])
    you = input('请选择:1石头2剪刀3布')
    if you=='1':
        x=1
    elif you=='2':
        x=1
    elif you=='3':
        x=1
    else:
        print("请重新输入！")
        continue
    if you==computer:
        you=int(you)-1
        print('你和电脑都出了'+youturn[you])
        print(name +str(c))
        print('电脑' +str(pc))
        continue
    elif you + computer in win_list:
        print('你赢了')
        c+=1
        print(name +str(c))
        print('电脑' +str(pc))
        if c==10:
            print('你成功了！')
            print(name +str(c))
            print('电脑' +str(pc))
        continue
    else:
        print('你输了')
        pc+=1
        if pc==10:
            print('你失败了！')
            print(name +str(c))
            print('电脑' +str(pc))
        else:
            print(name +str(c))
            print('电脑' +str(pc))
            continue