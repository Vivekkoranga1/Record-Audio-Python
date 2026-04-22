import sounddevice #sounddevice is used to record audio from microphone
from scipy.io.wavfile import write

seconds = 5
fps = 44100                 #frame per second in (Htz)
 

myrecording = sounddevice.rec(frames=fps*seconds , samplerate = fps ,channels = 1)
# channels = 1 Mono audio (1 channel)
# channels = 2 → Stereo (left + right)

sounddevice.wait()
#This pauses the program until recording is complete



write("output.mp3",fps,myrecording)