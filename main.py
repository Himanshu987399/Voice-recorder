import sounddevice as sd
import soundfile as sf
from tkinter import *

def Voice_recorder():
    fs=48000
    dur=10
    myrec = sd.rec(int(dur * fs),samplerate=fs,channels=2)
    sd.wait()
    return sf.write("My_Audio_file.flac",myrec,fs)

a= Tk()
Label(a,text = "Voice Recorder ").grid(row=0,sticky=W,rowspan=5)
b=Button(a,text = "Start",command = Voice_recorder)
b.grid(row=0,column = 2,columnspan=2,rowspan=2,padx=5,pady=5)
mainloop()