import urllib.request
import os
def url_oprn():
    req = urllib.request.Request(url)
    req.add_header('user-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75')
    response = urllib.request.urlopen(url)
    html = response.read()

    return html

def get_page(url):
    url_open(url).decode('utf-8')

    a = html.find('rifhttext') - 6
    b = html.find('<',a)

    return html[a:b]

def find_imgs(url):
    url_open(url).decode('utf-8')
    img_addrs = []

    a = html.find('img src=')
    while a != -1 :
        b = html.find('.jpg',a+255)
        if b != -1:
            img_addrs.append(html[a+9,b+4])
        else :
            b = a + 9
    return img_addrs
def save_imgs(folder,img_addrs):
    for each in img_addrs :
        filename = each.split('/')[-1]
        with open(filename,'wb') as f :
            img = urllib(each)
            f.write(img)


def download_img(folder='',pages=10):
    os.mkdir(folder)
    os.chdir(folder)

    url = ""
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url =url + 'page-' + str(page_num) + "#comments"
        img_addrs = find_imgs(page_url) 
        save_imgs(folder,img_addrs)

if __name__ == '__main__':
    download_img()