import datetime
from sqlite3 import Timestamp
import pyaudio
import wave
def audio():
    audio = pyaudio.PyAudio()
    stream=audio.open(format=pyaudio.paInt16, channels=2, rate=48000, input=True, frames_per_buffer=1024)
    frames = [] 
    try:
        while True:
            data = stream.read (1024) 
            frames.append (data)
    except KeyboardInterrupt:
        stream.stop_stream ()
        stream.close ()
        audio.terminate ()
        time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M')
        sound_file = wave.open(f'{time_stamp}.wav', "wb") 
        sound_file.setnchannels(2)
        sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        sound_file.setframerate (48000)
        sound_file.writeframes (b''.join(frames))
        sound_file.close()
