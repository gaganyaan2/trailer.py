import glob
import random
import subprocess
from getfileinfo import getfileinfo

class vertical2H:
    vimg=[]
    getfileinfo=getfileinfo()
    videohw=""
    def getvimg(self):
        for imgs in glob.glob('*.jpg'):
            self.vimg.append(imgs)
        for imgs in glob.glob('*.png'):
            self.vimg.append(imgs)

    def v2h(self):

        for i in self.vimg:
            print("vimg :  ",self.vimg)
            print("Working on : "+i)
            print("ffmpeg -i "+i+" -vf \"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2\" outv2h."+i+".jpg")
            p = subprocess.Popen("ffmpeg -i "+i+" -vf \"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2\" outv2h."+i+".jpg", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                print(line),