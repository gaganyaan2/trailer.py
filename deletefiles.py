import os
import glob
class deletefiles:

    def getdeletefiles(self,vlist,imglist):
        # Delete tmp files
        print("Deleting tmp files...")
        vcount=0
        for i in vlist:
            vcount=vcount+1
            os.remove(str(vcount)+".mp4")

        for jpg in glob.glob("*.jpg.jpg"):
            os.remove(jpg)
        for jpg in glob.glob("*.png.jpg"):
            os.remove(jpg)

        os.remove("concatenate.mp4")
        os.remove("audiogain.mp4")
        os.remove("addaudio.mp4")
        os.remove("fade.mp4")
        for i in imglist:
            os.remove("out."+i+".mp4")
        
        os.remove("filter.mp4")
        print("Delete all *.mp4 files")
        print("Deleted tmp files...")