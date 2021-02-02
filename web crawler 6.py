import re
import os
import requests
import easygui as g
import time

def get_html(url):
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3314.0 Safari/537.36 SE 2.X MetaSr 1.0',
                      'Referer':'https://www.mzitu.com/japan/'} 
    html=requests.get(url,headers=header)
    return html

def get_img(html):
    html=html.text
    img_re="https:\/\/imgpc\.iimzt\.com\/(?:.+\/)+.+(?:\.jpg)" #详情页查找jpg图片正则表达式
    imgs=re.findall(img_re,html)
    return imgs


def save_img(imgs,page):
    for img_url in imgs:
        res = get_html(img_url)
        img = res.content
        name=page+img_url.split("/")[-1] #加个page,知道是第几页的模特,方便下次继续，嘿嘿嘿
        print(img_url)
        with open(name, "wb") as f:
            f.write(img)


def download_mm():
    great=g.diropenbox()
    os.chdir(great)
    i=int(input("请输入开始页码（建议为1）："))
    n=int(input("请输入结束页码："))
    while i<n:
        home_url="https://www.mzitu.com/page/"+str(i)+"/"
        i+=1
        model_html=get_html(home_url).text
        model=re.compile("https:\/\/.{13}\/\d{5,6}")# 获取模特编号正则表达式
        all_model= model.findall(model_html) 
        all_model=list(set(all_model)) #去重
        for each in all_model:           
            
            img_url=get_html(each).text
            dirs=re.search(r'([\u4e00-\u9fa5·]{2,16})',img_url).group()#"获取模特名字正则表达式"
            print('开始下载%s模特的图片' % dirs)
            if os.path.exists(dirs):
                pass
            else:
                os.mkdir(dirs)#给每个模特建个文件夹
                os.chdir(dirs)
                try:
                    nums=re.findall("https:\/\/.{13}\/\d{5,6}\/\d{2}",img_url)#获得页码正则表达式
                    page_num=int(nums[-1].split("/")[-1])
                    print('该模特共有%s张图片'% page_num)
                    for mm in range(page_num):
                        mm_url=each+"/"+str(mm+1)
                        print(mm_url)
                        mm_html=get_html(mm_url)
                        imgs=get_img(mm_html)
                        page=str(i-1)+"_"
                        save_img(imgs,page)
                        time.sleep(1)# 下载速控制一下 不要太快
                except:
                    pass
                os.chdir(os.pardir)
    x = input("请输入任意键退出")
        

if __name__=="__main__":
    download_mm()

