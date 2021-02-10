'''
功能：模拟掷骰子
版本：5.0
'''
import random
import matplotlib.pyplot as plt
import numpy as np
# 解决中文显示问题
plt.rcParams['font.sans-serif'] = ['SimHei']  #SimHei黑体 
plt.rcParams['axes.unicode_minus'] = False
 
def roll_dice():
    '''
    模拟掷骰子
    '''
    roll = random.randint(1,6)
    return roll
 
def main():
    total_times = 1000
    # 记录骰子的结果
    roll1_arr = np.random.randint(1,7,size=total_times)
    roll2_arr = np.random.randint(1, 7, size=total_times)
    result_arr = roll1_arr + roll2_arr
    # hist,bins = np.histogram(result_arr ,bins=range(2,14))
    # print(hist)
    # print(bins)
    #数据可视化
    plt.hist(result_arr  ,bins=range(2,14),normed= 1,edgecolor='black',linewidth=1,rwidth= 0.8)
            #edgeclor:边缘颜色   linewidth:边缘宽度  normed=1时转化为概率图  rwidth:柱子宽度
    #设置X轴坐标点
    tick_labels = ['2点', '3点', '4点', '5点',
                   '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13) + 0.5
    plt.xticks(tick_pos,tick_labels)
 
    plt.title('骰子点数统计')  #名称
    plt.xlabel('点数')
    plt.ylabel('频率')
    plt.show()
if __name__ == '__main__':
    main()