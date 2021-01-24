#-*-coding:utf-8-*-
import Tkinter
import tkMessageBox

root = Tkinter.Tk()
root.title("XO棋")

#保存棋盘现状
chessboard=['','','','','','','','','']
#胜局数组8种情况
victorychesskeep=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
isgameover = True

       
#回调函数
def updatebttx_1():
        button_1['text']='O'
        button_1['state']='disabled'#点了就冻结
        chessboard[0]='O'
        if judgemodulcase.judge()== False:#O走完判断
                computerstepcase.computerchess()
                judgemodulcase.judge()#X走完判断
       
def updatebttx_2():
        button_2['text']='O'
        button_2['state']='disabled'
        chessboard[1]='O'
        if judgemodulcase.judge()== False:
                computerstepcase.computerchess()
                judgemodulcase.judge()

def updatebttx_3():
        button_3['text']='O'
        button_3['state']='disabled'
        chessboard[2]='O'
        if judgemodulcase.judge()== False:
                computerstepcase.computerchess()
                judgemodulcase.judge()

def updatebttx_4():
        button_4['text']='O'
        button_4['state']='disabled'
        chessboard[3]='O'
        if judgemodulcase.judge()== False:
                computerstepcase.computerchess()
                judgemodulcase.judge()

def updatebttx_5():
        button_5['text']='O'
        button_5['state']='disabled'
        chessboard[4]='O'
        if judgemodulcase.judge()== False:
                computerstepcase.computerchess()
                judgemodulcase.judge()

def updatebttx_6():
        button_6['text']='O'
        button_6['state']='disabled'
        chessboard[5]='O'
        if judgemodulcase.judge()== False:
                computerstepcase.computerchess()
                judgemodulcase.judge()

def updatebttx_7():
        button_7['text']='O'
        button_7['state']='disabled'
        chessboard[6]='O'
        if judgemodulcase.judge()== False:
                computerstepcase.computerchess()
                judgemodulcase.judge()

def updatebttx_8():
        button_8['text']='O'
        button_8['state']='disabled'
        chessboard[7]='O'
        if judgemodulcase.judge()== False:
                computerstepcase.computerchess()
                judgemodulcase.judge()

def updatebttx_9():
        button_9['text']='O'
        button_9['state']='disabled'
        chessboard[8]='O'
        if judgemodulcase.judge()== False:
                computerstepcase.computerchess()
                judgemodulcase.judge()
       
def chessboardfreeze():#棋盘冻结
        button_1['state']='disabled'
        button_2['state']='disabled'
        button_3['state']='disabled'
        button_4['state']='disabled'
        button_5['state']='disabled'
        button_6['state']='disabled'
        button_7['state']='disabled'
        button_8['state']='disabled'
        button_9['state']='disabled'       
def unchessboardfreeze():#棋盘冻结
        button_1['state']='normal'
        button_2['state']='normal'
        button_3['state']='normal'
        button_4['state']='normal'
        button_5['state']='normal'
        button_6['state']='normal'
        button_7['state']='normal'
        button_8['state']='normal'
        button_9['state']='normal'

#棋盘布局
button_1 = Tkinter.Button(root,width = 13,height=5,cursor = "hand2")
button_1['text']=''
#button_1.bind('<Button-1>',updatebttx_1)
button_1["command"] = updatebttx_1
button_1.grid(row=0,column = 0)

button_2 = Tkinter.Button(root,width = 13,height=5,cursor = "hand2")
button_2['text']=''
button_2["command"] = updatebttx_2
button_2.grid(row=0,column = 1)

button_3 = Tkinter.Button(root,width = 13,height=5,cursor = "hand2")
button_3['text']=''
button_3["command"] =updatebttx_3
button_3.grid(row=0,column = 2)

button_4 = Tkinter.Button(root,width = 13,height=5,cursor = "hand2")
button_4['text']=''
button_4["command"] =updatebttx_4
button_4.grid(row=1,column = 0)

button_5 = Tkinter.Button(root,width = 13,height=5,cursor = "hand2")
button_5['text']=''
button_5["command"] = updatebttx_5
button_5.grid(row=1,column = 1)

button_6 = Tkinter.Button(root,width = 13,height=5,cursor = "hand2")
button_6['text']=''
button_6["command"] = updatebttx_6
button_6.grid(row=1,column = 2)

button_7 = Tkinter.Button(root,width = 13,height=5,cursor = "hand2")
button_7['text']=''
button_7["command"] = updatebttx_7
button_7.grid(row=2,column = 0)

button_8 = Tkinter.Button(root,width = 13,height=5,cursor = "hand2")
button_8['text']=''
button_8["command"] = updatebttx_8
button_8.grid(row=2,column = 1)

button_9 = Tkinter.Button(root,width = 13,height=5,cursor = "hand2")
button_9['text']=''
button_9["command"] = updatebttx_9
button_9.grid(row=2,column = 2)

       
class Judgemodul:#判断胜负类
        def judge(self):
                ishasend = False
                eval = chessthink.evaluatefunc()
                if eval == 1000 or eval == -1000 or eval ==0:
                        ishasend = True
                        chessboardfreeze()
                        if(eval == 1000):
                            tkMessageBox.showinfo(title='结果', message='电脑赢了')
                        if(eval == -1000):
                                tkMessageBox.showinfo(title='结果', message='你赢了')
                        if(eval == 0):
                                tkMessageBox.showinfo(title='结果', message='平局')
                return ishasend       


class Thinkfunc:#AI走法类
               
        def        evaluatefunc(self):#评估函数
                end = 1#结果初始化 0：平局，1：继续，1000：赢......
                isfull = True#棋盘是否已满
                Xcx = 0#X的2连子计量
                Ocx = 0
                for ech in chessboard:
                        if ech == '':
                                isfull = False
                                break       
                for x in range(0,len(victorychesskeep)):
                        #3连子
                        if chessboard[victorychesskeep[x][0]] == chessboard[victorychesskeep[x][1]] ==chessboard[victorychesskeep[x][2]]:
                                if chessboard[victorychesskeep[x][0]] != '':
                                        if chessboard[victorychesskeep[x][0]] == 'X':
                                                end =1000
                                                return end
                                        elif chessboard[victorychesskeep[x][0]] == 'O':
                                                end = -1000
                                                return end
                        elif end != 1000 or end != -1000:#没赢没输
                                if isfull == True:#棋盘满了
                                        end = 0#平局
                                        return end
                                elif isfull == False:#没赢没输没满，判断2连子
                                        if chessboard[victorychesskeep[x][0]]==chessboard[victorychesskeep[x][1]] or chessboard[victorychesskeep[x][2]]==chessboard[victorychesskeep[x][1]]:                       
                                                if chessboard[victorychesskeep[x][1]] != '':
                                                        if chessboard[victorychesskeep[x][1]] == 'X':
                                                                Xcx = Xcx +1
                                                        elif chessboard[victorychesskeep[x][1]] =='O':
                                                                Ocx = Ocx +1
               
                end = Xcx*50 - Ocx*50#2连子差
                if end == 0:#不是平局的0，则继续
                        end = 1
                return end                               
                               
       
        def recurmin(self,searchdeep,alpha,beta):
                isgameover = False
                bettervalue = 1000
                value = self.evaluatefunc()
                if value == 1000 or value == -1000 or value == 0:
                        isgameover = True
                if(alpha >= beta):#对min最有利>=对max最有利，β剪枝
                        return value
                if(searchdeep == 0 or isgameover == True):
                        return value
                for ech in range(0,len(chessboard)):
                        if chessboard[ech] == '':
                                chessboard[ech]= 'O'
                                recordvalue = self.recurmax(searchdeep-1,alpha,min(bettervalue,beta))
                                bettervalue = min(recordvalue,bettervalue)
                                chessboard[ech] =''
                return bettervalue
       
        def recurmax(self,searchdeep,alpha,beta):
                isgameover = False
                bettervalue = -1000
                value = self.evaluatefunc()
                if value ==1000 or value == -1000 or value == 0:
                        isgameover = True
                if(beta <= alpha):#对max最有利<=对min最有利，α剪枝
                        return value
                if(searchdeep ==0 or isgameover == True):
                        return value
                for ech in range(0,len(chessboard)):
                        if chessboard[ech] == '':
                                chessboard[ech] = 'X'
                                recordvalue = self.recurmin(searchdeep-1,max(alpha,bettervalue),beta)
                                bettervalue = max(recordvalue,bettervalue)
                                chessboard[ech] =''
                return bettervalue

                       
        def minMax(self,searchdeep):
                keepindex=[]
                bettervalue = -1000
                for ech in range(0,len(chessboard)):
                        if chessboard[ech] == '':
                                chessboard[ech] = 'X'#假设
                                recordvalue = self.recurmin(searchdeep,-1000,1000)
                                if(recordvalue >= bettervalue):#最大值
                                        bettervalue = recordvalue
                                        betterposition = ech
                                chessboard[ech] = ''#还原
                return betterposition



class Computerstep:#电脑走棋类
        def computerchess(self):
                nextsp = chessthink.minMax(5)
                if nextsp == 0:
                        button_1["text"]='X'
                        button_1['state']='disabled'#点了就冻结
                        chessboard[0]='X'
                elif nextsp ==1:
                        button_2["text"]='X'
                        button_2['state']='disabled'
                        chessboard[1]='X'
                elif nextsp ==2:
                        button_3["text"]='X'
                        button_3['state']='disabled'
                        chessboard[2]='X'
                elif nextsp ==3:
                        button_4["text"]='X'
                        button_4['state']='disabled'
                        chessboard[3]='X'
                elif nextsp ==4:
                        button_5["text"]='X'
                        button_5['state']='disabled'
                        chessboard[4]='X'
                elif nextsp ==5:
                        button_6["text"]='X'
                        button_6['state']='disabled'
                        chessboard[5]='X'
                elif nextsp ==6:
                        button_7["text"]='X'
                        button_7['state']='disabled'
                        chessboard[6]='X'
                elif nextsp ==7:
                        button_8["text"]='X'
                        button_8['state']='disabled'
                        chessboard[7]='X'
                elif nextsp ==8:
                        button_9["text"]='X'
                        button_9['state']='disabled'
                        chessboard[8]='X'

def main():
    unchessboardfreeze()#解冻               
    computerstepcase.computerchess()#第一步
    chessboard=['','','','','','','','','']
    victorychesskeep=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    isgameover = True
       
chessthink = Thinkfunc()
computerstepcase = Computerstep()
judgemodulcase = Judgemodul()
main()
root.resizable(width='false',height='false')#不改变窗体大小
root.mainloop()