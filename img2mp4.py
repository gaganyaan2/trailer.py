import glob
import random
import subprocess

class img2mp4:
    imglist=[]
    def getimg2mp4(self):
        for imgs in glob.glob('*jpg.jpg'):
            self.imglist.append(imgs)
        for imgs in glob.glob('*.png.jpg'):
            self.imglist.append(imgs)
        for imgs in glob.glob('*.jpeg.jpg'):
            self.imglist.append(imgs)

        #convert imgs to random sec mp4

        for i in self.imglist:
            print("self.imglist :  ",self.imglist)
            print("Working on : "+i)
            rtime=str(random.uniform(0.8, 1))
            print("ffmpeg -loop 1 -i "+i+" -c:v libx264 -t "+rtime+" -pix_fmt yuv420p -vf scale=1920:1080,setdar=16:9,setsar=1:1 out."+i+".mp4")
            p = subprocess.Popen("ffmpeg -loop 1 -i "+i+" -c:v libx264 -t "+rtime+" -pix_fmt yuv420p -vf scale=1920:1080,setdar=16:9,setsar=1:1 out."+i+".mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            for line in p.stdout.readlines():
                print(line),