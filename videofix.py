import os
import glob
import random
import subprocess
from subclip import subclip
from files import files
from getfileinfo import getfileinfo


class videofix:
    getfileinfo=getfileinfo()
    videoW=""
    videoH=""
    def videofix(self,vlistedit):
        for i in vlistedit:
            self.getfileinfo.audiostatus=""
            self.getfileinfo.getvideoinfo(i)
            #check audio status
            if self.getfileinfo.audiostatus == "audio":
                print(i+" has audio")
            else:
                print(i+" adding audio")
                print("ffmpeg -i "+i+" -i dummysilence.mp3 -codec copy -shortest dummy."+i)
                p = subprocess.Popen("ffmpeg -i "+i+" -i dummysilence.mp3 -codec copy -shortest dummy."+i, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for line in p.stdout.readlines():
                    print(line),
                os.remove(i)
                os.rename("dummy."+i,i)
            #set video resolution
            self.videoW="1920"
            self.videoH="1080"
            print("vi width "+str(self.getfileinfo.w))
            if(self.videoW == str(self.getfileinfo.w)):
                print("video resolution: "+str(self.getfileinfo.w)+":"+str(self.getfileinfo.h))
            else:
                print("ffmpeg -i "+i+" -filter:v scale="+self.videoW+":"+self.videoH+",setdar=16:9,setsar=1:1 -c:a copy width."+i)
                p = subprocess.Popen("ffmpeg -i "+i+" -filter:v scale="+self.videoW+":"+self.videoH+",setdar=16:9,setsar=1:1 -c:a copy width."+i, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for line in p.stdout.readlines():
                    print(line),
                os.remove(i)
                os.rename("width."+i,i)
    

