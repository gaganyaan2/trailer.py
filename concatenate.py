import glob
import random
import subprocess
from subclip import subclip
from files import files

class concatenate:
    vlist=[]
    def getconcatenate(self,vlistedit,vlist2):
        cmdva=""
        vcount=0
        print("vlistedit : ",vlistedit)
        print("vlist2 : "+vlist2)
        for i in vlistedit:
            list2 ="["+str(vcount)+":v] ["+str(vcount)+":a] "
            vcount=vcount+1
            cmdva = cmdva+list2
        print("ffmpeg "+vlist2+" -filter_complex \""+cmdva+" concat=n="+str(vcount)+":v=1:a=1 [v] [a]\" -map \"[v]\" -map \"[a]\" concatenate.mp4")
        p = subprocess.Popen("ffmpeg "+vlist2+" -filter_complex \""+cmdva+" concat=n="+str(vcount)+":v=1:a=1 [v] [a]\" -map \"[v]\" -map \"[a]\" concatenate.mp4", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        for line in p.stdout.readlines():
            print(line)

