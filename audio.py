import glob
import random
import subprocess
from subclip import subclip
from files import files
from getfileinfo import getfileinfo

class audio:
    getfileinfo=getfileinfo()
    def audiogain(self):
        #audio gain -15db
        print("ffmpeg -i concatenate.mp4 -vcodec copy -af \"volume=-15dB\" audiogain.mp4")

        p = subprocess.Popen("ffmpeg -i concatenate.mp4 -vcodec copy -af \"volume=-15dB\" audiogain.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
	        print(line),

    def addaudio(self):
        #add background song

        #get list of mp3
        mp3list=[]
        bsong=""
        for name in glob.glob('*.mp3'):
            mp3list.append(name)
        if not mp3list:
            bsong = input("Enter background song path(D:\\filename.mp3) : ")
        else:
            bsong=mp3list[0]
        print("Selected background song : "+bsong)

        print("ffmpeg -i \""+bsong+"\" -i audiogain.mp4 -filter_complex \"[0:a][1:a]amerge,pan=stereo:c0<c0+c2:c1<c1+c3[out]\" -map 1:v -map \"[out]\" -c:v copy -shortest addaudio.mp4")

        p = subprocess.Popen("ffmpeg -i \""+bsong+"\" -i audiogain.mp4 -filter_complex \"[0:a][1:a]amerge,pan=stereo|c0<c0+c2|c1<c1+c3[out]\" -map 1:v -map \"[out]\" -c:v copy -shortest addaudio.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line),
    
    def fade(self):
        self.getfileinfo.getvideoinfo("addaudio.mp4")
        print("ffmpeg -i addaudio.mp4 -af \"afade=t=in:ss=0:d=2,afade=t=out:st="+str(self.getfileinfo.vduration)+":d=3\" fade.mp4")
        p = subprocess.Popen("ffmpeg -i addaudio.mp4 -af \"afade=t=in:ss=0:d=2,afade=t=out:st=\""+str(self.getfileinfo.vduration-3)+"\":d=3\" fade.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line),