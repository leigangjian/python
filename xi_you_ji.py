print("西游记人物出场次数如下：")
import jieba
import time
start = time.perf_counter()
text = open("C:\Python\西游记.txt", "r", encoding="gb18030").read()
excludes = {"一个", "那里", "怎么", "我们", "不知", "两个", "甚么", "只见", "不是", "原来", "不敢", "闻言", "如何"}
words = jieba.lcut(text)  
# jieba.lcut()方法对变量text中的内容进行分词，把分词的结果列表保存到变量words中
counts = {}         # 新建一个叫作counts的字典
for word in words:
    if len(word) == 1:
        continue
    elif word == "行者" or word == "齐天大圣" or word == "老孙":
        rword = "孙悟空"                                     
# 新建了一个变量rword，用它代替word作为字典counts的键
    elif word == "师父" or word == "三藏" or word == "圣僧":
        rword = "唐僧"                                       
# 将rword作为字典counts的键，将其出现次数作为值。例如，我们知道“师傅”
# “三藏”和“圣僧”都是对“唐僧”的尊称，所以我们可以这些词归类为唐僧
    elif word == "呆子" or word == "八戒" or word == "老猪":  
        rword = "猪八戒"
    elif word == "沙和尚":
        rword = "沙僧"
    elif word == "妖精" or word == "妖魔" or word == "妖道":
        rword = "妖怪"
    elif word == "佛祖":
        rword = "如来"
    elif word == "三太子":
        rword = "白马"
    else:
        rword = word
counts[rword] = counts.get(rword, 0) + 1
# 一个新的for循环遍历列表excludes中的元素，把每个元素赋值给变量word
for word in excludes:
  del counts[word]  
# 在循环体中，使用del语句，将字典counts中的键为word的键—值对删除
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)  
# 把字典转换为列表，然后利用列表的sort()方法来排序
for i in range(6):  # 借助range()函数生成一个等差数组，展示items中前6个元素
    word, count = items[i]
print("{0:<10}{1:>5}次".format(word, count))  
# word的值左对齐，宽度是10；把count的值右对齐，宽度是5
dur = time.perf_counter() - start
print("运行时间为{:.2f}s".format(dur))
