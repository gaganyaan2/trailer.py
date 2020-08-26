import glob
import subprocess

class files:
    def getfiles(self):
        vlist=[]
        for name in glob.glob('*.mp4'):
	        vlist.append(name)
        for name in glob.glob('*.avi'):
	        vlist.append(name)
        for name in glob.glob('*.mkv'):
	        vlist.append(name)
        for name in glob.glob('*.mov'):
	        vlist.append(name)
        for name in glob.glob('*.3gp'):
	        vlist.append(name)
        
        print("Selected Videos :",vlist)
        return vlist