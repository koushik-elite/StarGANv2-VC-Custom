import array
from pydub import AudioSegment
from pydub.utils import get_array_type

# from phonemizer import phonemize
# from phonemizer.backend import EspeakBackend
# from phonemizer.separator import Separator
import os
from os import listdir
from os.path import isfile, join
from os import walk
import pandas as pd
from tqdm import tqdm
import shutil

mypath = "/mnt/d/voice/"
srcpath = "/mnt/d/tamil/"
# dir_list = os.listdir(mypath)

if os.path.exists(srcpath):
    shutil.rmtree(srcpath)

for dir in os.listdir(mypath):
    sub_srcpath = srcpath + dir
    sub_mypath = mypath + dir
    os.makedirs(sub_srcpath)
    count = 1
    for filenames in os.listdir(sub_mypath):
        print(filenames)
        path_to_file = sub_mypath + "/" + filenames
        path_to_out = sub_srcpath + f"/{count}.wav"

        print(path_to_out)
        sound = AudioSegment.from_file(file=path_to_file)
        mono_audios = sound.split_to_mono()
        # print(len(mono))
        # left = sound.split_to_mono()[0]
        # # print(left)
        # bit_depth = left.sample_width * 8
        # # print(bit_depth)
        # array_type = get_array_type(bit_depth)
        # # print(array_type)
        # numeric_array = array.array(array_type, left._data)
        # print(numeric_array)
        # mono_audios = stereo_audio.split_to_mono() 
  
        # Exporting/Saving the two mono 
        # audio files present at index 0(left) 
        # and index 1(right) of list returned 
        # by split_to_mono method 
        if len(mono_audios) > 0:
            mono_left = mono_audios[0].export(path_to_out, format="wav")
            count = count + 1
        # break

