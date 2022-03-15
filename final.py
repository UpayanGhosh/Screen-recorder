from video_recorder import video
import time
from audio_recorder import audio
import multiprocessing

p1=multiprocessing.Process(target=video) 
p2=multiprocessing.Process(target=audio)
if __name__ == '__main__':
    p1.start()
    p2.start()
    p2.join()
    p1.join()
    