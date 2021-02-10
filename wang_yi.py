

import sys, os
import requests
from mutagen.mp3 import MP3
import pygame
from PySide2.QtCore import QFile, QStringListModel,QTimer,QModelIndex
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QFileDialog


class Play_Music:
    def __init__(self):
        super(Play_Music, self).__init__()

        # qflie = QFile('D:\Code\Python\pyqt\pyside2\\play_music.ui')
        
        qflie = QFile('./play_music.ui')
        qflie.open(QFile.ReadOnly)
        qflie.close()

        self.ui = QUiLoader().load(qflie)
        # self.ui = QUiLoader().load('D:\Code\Python\pyqt\pyside2\\play_music.ui')


        self.ui.Slider_vol.valueChanged.connect(self.vol_chang)
        self.ui.Slider_pos.valueChanged.connect(self.music_pos)
        
        self.ui.pushButton_search.clicked.connect(self.get_song_list)
        self.ui.pushButton_pause.clicked.connect(self.pause_song)      
        self.ui.song_list.doubleClicked.connect(self.doublechecked_song)

        self.ui.pushButton_location.clicked.connect(self.loc_play)
        
        







        self.timer1 = QTimer()
        self.timer1.start(1000)
        self.timer1.timeout.connect(self.show_info)

        self.url = 'http://www.gequdaquan.net/gqss/api.php?callback=jQuery111305903476798204579_1611647627808'
        self.headers = {
            'Referer':'http://www.gequdaquan.net/gqss/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3861.400 QQBrowser/10.7.4313.400',
            'X-Requested-With': 'XMLHttpRequest'
        }


        pygame.init()
        self.pause_state = 0
        self.time_length = float(0)
        pygame.mixer_music.set_volume(0.5)
        self.get_vol = pygame.mixer_music.get_volume()

        self.song_list = []
        self.source = 'netease'
        self.search_name = ''
        self.song_name = ''
        self.song_id = ''
        self.song_artist = ''
        self.show_list = []
        self.song_url = ''
        self.index = ''
        self.play_star = 0
        self.song_playname = ''
        self.dir_choose = os.getcwd()
        
      
   

    def vol_chang(self):
        get_vol = self.ui.Slider_vol.value() /100
        # print(get_vol)
        pygame.mixer_music.set_volume(get_vol)

    def get_song_list(self):
        self.show_list = []        
        self.search_name = self.ui.lineEdit_song.text()
        data = {
            'types': 'search',
            'count': 50,
            'source': self.source,
            'pages': 1,
            'name': self.search_name
        }
        response = requests.post(url=self.url, headers=self.headers, data=data)
        # result = response.text.replace('\\','')
        
        if response.status_code == 200:
            result = response.text.encode().decode('unicode_escape')   
            result = result.strip('jQuery111305903476798204579_1611647627808()')
            self.song_list = eval(result)
            for song in self.song_list:
                self.song_name = song.get('name')
                self.song_id = song.get('id')
                self.song_artist = ' '.join(song.get('artist'))
                # print(self.song_artist)
                self.show_list.append(self.song_name + ' -- ' + self.song_artist)
                # print(self.show_list)
            self.add_show_list()
            self.get_song_url()
        else:
            self.ui.label_state.setText('网络查找....')

  
    def add_show_list(self):
        list_model = QStringListModel()
        list_model.setStringList(self.show_list)
        self.ui.song_list.setModel(list_model)
        

    def get_song_url(self):
        data = {
            'types': 'url',
            # 'id': '0d07389f31ee4d5470640733c4737962',
            'id': self.song_id,
            'source': self.source,
        }

        response = requests.post(url=self.url, headers=self.headers, data=data)
        print(response.content)
        if response.status_code == 200:
            result = response.text.replace('\\','')
            
            result = result.encode().decode()
            result = result.strip('jQuery111305903476798204579_1611647627808()')
            
            result = eval(result)
            self.song_url = result.get('url')
        else:
            self.ui.label_state.setText('网络查找....')

            

    def download_song(self):

        self.get_song_url()
        response = requests.get(url=self.song_url, headers=self.headers)
        # print(response.status_code)
        if response.status_code == 200:
            self.song_playname = self.song_name + '--' + self.song_artist + '.mp3'

            # self.ui.label_state.setText('正在下载' + self.song_name + '--' + self.song_artist + '.mp3')
            self.ui.label_state.setText('正在下载' + self.song_playname)

            self.dir_choose = QFileDialog.getExistingDirectory(None, "选取歌曲保存文件夹", self.dir_choose )
            # print(dir_choose)


            self.song_playname = self.dir_choose + '/' + self.song_playname   
            print(self.song_playname)
            with open(self.song_playname, 'wb') as w:
            # with open(save_path, 'wb') as w:
                w.write(response.content)
            self.ui.label_state.setText('下载完成')
            self.ui.Slider_pos.setValue(0)
            
            self.play_song()
            self.pause_state = 1
            self.ui.label_state.setText('正在播放 ' + self.song_playname)
        else:
            print('failed')
            
            self.ui.label_state.setText('网络查找....')
        
    def loc_play(self):
        self.song_playname, _ = QFileDialog.getOpenFileName(None, "选取播放的MP3文件", self.dir_choose, "mp3 Files (*.mp3)")
        self.ui.Slider_pos.setValue(0)
        self.play_song()
        self.pause_state = 1
        self.ui.label_state.setText('正在播放 ' + self.song_playname)


    def checked_song(self,index):
        self.index = index
        song = self.song_list[index.row()]
        self.song_id = song.get('id')
        self.source = song.get('source')
        self.song_name = self.show_list[index.row()].split('--')[0]
        self.song_artist = self.show_list[index.row()].split('--')[1]

    def doublechecked_song(self,index):
        self.checked_song(index)
        self.download_song()


    def play_song(self):
        pygame.init()
        pygame.mixer.music.load(self.song_playname)
        
        self.time_length = MP3(self.song_playname).info.length
        self.song_playname = self.song_playname.split('/')[-1]
        pygame.mixer.music.play()
        

    def pause_song(self):
        
        if self.pause_state == 1:
            pygame.mixer.music.pause()
            self.ui.pushButton_pause.setText('继续')
            self.ui.label_state.setText('暂停 ' + self.song_playname)
            self.pause_state = 0
        else:
            pygame.mixer.music.unpause()
            self.ui.pushButton_pause.setText('暂停')
            self.ui.label_state.setText('播放 ' + self.song_playname)
            self.pause_state = 1

    def show_info(self):
        
        if self.time_length != float(0):
            all_m, all_s = divmod(float(self.time_length),60)
            all_time = str(int(all_m)) + ':' + str(int(all_s))
            get_time = pygame.mixer.music.get_pos()/1000 + self.play_star
            get_m, get_s = divmod(float(get_time), 60)
            now_time = str(int(get_m)) + ':' + str(int(get_s))           
            self.ui.label_info.setText(now_time + '/' + all_time)

            get_pos = int(float(get_time)*99/float(self.time_length))
            self.ui.Slider_pos_2.setValue(get_pos)

    def music_pos(self):
        get_pos = self.ui.Slider_pos.value()
        get_pos = int(float(self.time_length)*get_pos/100)
        self.play_star = get_pos

        pygame.mixer.music.play(loops=1,start=get_pos)
        # self.ui.Slider_pos.setValue(0)



if __name__ == '__main__':
    app = QApplication([])
    app.setStyle('Fusion')
    windows = Play_Music()
    windows.ui.show()
    app.exec_()
