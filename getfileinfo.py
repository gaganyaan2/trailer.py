import glob
import random
import subprocess
import shlex
import json

class getfileinfo:
    h=""
    w=""
    vduration=0
    filename=""
    audiostatus=""
    def getvideoinfo(self,filename):
        #get video duration/resolution 
        cmd = "ffprobe -v quiet -print_format json -show_streams"
        args = shlex.split(cmd)
        args.append(filename)

        # run the ffprobe process, decode stdout into utf-8 & convert to JSON
        ffprobeOutput = subprocess.check_output(args).decode('utf-8')
        ffprobeOutput = json.loads(ffprobeOutput)

        # prints all the metadata available:
        import pprint
        pp = pprint.PrettyPrinter(indent=2)
        #pp.pprint(ffprobeOutput)

        self.h = ffprobeOutput['streams'][0]['height']
        self.w = ffprobeOutput['streams'][0]['width']
        if len(ffprobeOutput['streams'])==2:
            self.audiostatus = ffprobeOutput['streams'][1]['codec_type']
        fduration = ffprobeOutput['streams'][0]['duration']
        self.vduration = float(fduration)