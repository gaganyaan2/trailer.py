from pathlib import Path
import urllib.request

class download:
    def downloadpng(self):
        png = Path("input.png")
        if png.exists():
            print("input.png file found")
        else:
            print('downloading input.png')
            url = 'https://github.com/initedit-project/trailer.py/raw/master/input.png'  
            urllib.request.urlretrieve(url, 'input.png')

    
    def dummysilence(self):
        dummysilence = Path("dummysilence.mp3")
        if dummysilence.exists():
            print("dummysilence.mp3 file found")
        else:
            print('downloading dummysilence.mp3')
            url = 'https://github.com/initedit-project/trailer.py/raw/master/dummysilence.mp3'  
            urllib.request.urlretrieve(url, 'dummysilence.mp3')

    def adummysong(self):
        adummysong = Path("adummysong.mp3")
        if adummysong.exists():
            print("adummysong.mp3 file found")
        else:
            print('downloading adummysong.mp3')
            url = 'https://github.com/initedit-project/trailer.py/raw/master/adummysong.mp3'  
            urllib.request.urlretrieve(url, 'adummysong.mp3')