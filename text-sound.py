import urllib.request
import urllib.parse
api = 'http://tts.baidu.com/text2audio?lan=zh&ie=UTF-8&text='
text = input("我：")
b = b'/:?='
text = urllib.parse.quote(text, b)
url = api + text
dat = urllib.request.urlopen(url).read()
with open('data.mp3', 'wb') as f:
    f.write(dat)