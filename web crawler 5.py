import requests
import json             #模块 requests  json  均是自己导入的

#第一部分，伪装网址
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Referer': 'http://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
    'csrf': 'RUJ53PGJ4ZD',
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1577029678,1577034191,1577034210,1577076651; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1577080777; kw_token=RUJ53PGJ4ZD',
}  #伪装，，在网页F12--Network--选好Name---再选择Headers---中Requests Headers---中User-Agent，Referer，csrf


#第三部分 下载音乐

#再次发送请求
def get_music(rid,name):

    url = " http: // www.kuwo.cn / url?format = mp3 & rid ={} & response = url & type = convert_url3 & br = 128".format(rid)
    relut = requests.get(url,headers = headers).json()
    music_url = relut["url"]

    with open("酷我音乐/{}.mp3“.format(name)","wb") as f :   #一定要自己创建好 “酷我音乐”文件夹，如果没有创建成功，就删去“/”，就会自动保存到现有的文件夹
        music = requests.get(music_url).content      #.content将文本形式转换为二进制
        f.write(music)
        f.close()
        print("下载完毕")

#第二部分  获取网址

def main():           #做一个分装函数

    singer = str(input("请输入你的歌手："))
    pagebox = int(input("请输入你需要的页数："))
    for page in range(1,pagebox + 1):
        url = "http://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={}&pn={}&rn=30&reqId=6a22ad90-6381-11ea-ad74-db939e27359f".format(singer, page)
        response = requests.get(url,headers = headers).json()  #.json()转换为字典   #get是请求方法，在网页F12--Network--选好Name---再选择Headers---中 General-- 中Request Method         Request URL  即为网址
        #print(response)
        data = response['data']['list']
        #print(data)

        for i in data:
            rid = i["rid"]
            name = i["name"]   #字典取值
            get_music(rid,name)
main()