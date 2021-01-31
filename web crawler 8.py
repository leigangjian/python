import requests
import re
import os

def get_html(url):
    r = requests.get(url)
    #返回壁纸首页信息,用来提取壁纸列表
    return r.text                                                                                      

def get_img_urls(img_num):
    img_url = f'http://www.win4000.com/wallpaper_detail_{img_num}_1.html'
    r = requests.get(img_url)
    #提取系列壁纸的总页数
    em = int(re.findall(r'<em>(.*?)</em>', r.text)[0]) + 1
    img_urls = [f'http://www.win4000.com/wallpaper_detail_{img_num}_{i}.html' for i in range(1,em)]
    #返回系列壁纸的网页列表【】
    return img_urls                                                                                    

def get_src(img_url):
    r = requests.get(img_url)
    src = re.findall('<img class="pic-large" src="(.*?)" alt=".*?" title=".*?"/>',r.text)[0]
    down_dir = re.findall('<img class="pic-large" src=".*?" alt="(.*?)" title=".*?"/>',r.text)[0]
    #返回壁纸下载源src,和系列名
    return src,down_dir                                                                 

def save_img(url,down_dir):
    #创建保存路径
    if not os.path.exists(down_dir):
        os.mkdir(down_dir)
    r = requests.get(url)
    path = down_dir + '/' + url.split('/')[-1]
    try:
        with open(path,'wb') as f:
            f.write(r.content)
            print(path,'\t\t壁纸保存成功√')
    except Exception as e:
        print(e)

def main():
    input('---按任意键开始爬取壁纸---(默认为当前路径)\n')
    #美女壁纸的5页urls                                                                                                       
    urls = [f'http://www.win4000.com/wallpaper_2285_0_0_{i}.html' for i in range(1,6)]        
    for url in urls:                           
        src_list = []                    
        html = get_html(url)
        #获取当前页面的所有链接数字（之后做系列url拼接）
        lst = re.findall('<a href=".*?(\d*?).html" alt=".*?" title=".*?" target="_blank">',html)             
        print('正在加载资源...')
        for img_num in lst:
            img_urls = get_img_urls(img_num)                                                               
            if img_urls:
                for img_url in img_urls:                                                                   
                    (src,down_dir) = get_src(img_url)
                    save_img(src,down_dir)                                                                 

if __name__ == '__main__':
    main()
    print('程序执行完成！')
