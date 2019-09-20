

apt install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0 ffmpeg
pip install pyaudio

import pyaudio
import struct
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

#variables
# how many samples per frame
CHUNK = 1024 * 4 # how many audio frame we will display
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100