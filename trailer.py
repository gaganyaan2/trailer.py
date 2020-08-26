import glob
import random
import subprocess
import os
import datetime
import time
import os.path
from os import path
import shlex
import json
from files import files
from subclip import subclip
from slowmo import slowmo
from concatenate import concatenate
from audio import audio
from movieeffect import movieeffect
from deletefiles import deletefiles
from videofix import videofix
from img2mp4 import img2mp4
from vertical2H import vertical2H

vlist=[]
vlistedit=[]
vcount=0
vlist2 =""
randomlen=0
randomstart=0
vduration=""
slow=""

cwd = os.getcwd()
os.system("cd "+cwd)
print("working direcory :"+cwd)

#vertical image and pad

vertical2H=vertical2H()
vertical2H.getvimg()
vertical2H.v2h()

#img to mp4 converter
img2mp4=img2mp4()
img2mp4.getimg2mp4()

#get list of videos
vlist=files().getfiles()

#select subclip
subclip=subclip()
subclip.getsubclip(vlist)

#check size/audio
videofix=videofix()
videofix.videofix(subclip.vlistedit)

#slomotion random
slowmo=slowmo()
slowmo.getslowmo(subclip.vlistedit)

#concatenate all video
concatenate=concatenate()
concatenate.getconcatenate(subclip.vlistedit,subclip.vlist2)

#audio
audio=audio()
audio.audiogain()
audio.addaudio()
audio.fade()

#movieeffect
movieeffect=movieeffect()
movieeffect.filter()
movieeffect.blackbar()

# Delete tmp files
deletefiles=deletefiles()
deletefiles.getdeletefiles(vlist,img2mp4.imglist)

#output
print("Output file Movietrailer.mp4")
print("Completed")
input("Press any key to exit")
