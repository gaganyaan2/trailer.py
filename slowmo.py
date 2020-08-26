import glob
import random
import subprocess
import os
from files import files
from subclip import subclip

class slowmo:
    def getslowmo(self,vlistedit):
        #slowmo = input("Slowmotion trailer(y/n) ? : ")
        #slowmo = self.gui.slowmo
        slowmo="y"
        if slowmo=="y" :
    	    for j in subclip.vlistedit:
                print("Working on."+j)
                print("ffmpeg -i "+j+" -filter_complex \"[0:v]setpts=2*PTS[v];[0:a]atempo=0.5[a]\" -map \"[v]\" -map \"[a]\" slow."+j+"")

                p = subprocess.Popen("ffmpeg -i "+j+" -filter_complex \"[0:v]setpts=2*PTS[v];[0:a]atempo=0.5[a]\" -map \"[v]\" -map \"[a]\" slow."+j+"", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                for line in p.stdout.readlines():
                    print(line),
                os.remove(j)
                os.rename("slow."+j,j)