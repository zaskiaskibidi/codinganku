import time
from threading import Thread, Lock
import sys

lock = Lock()

def animate_text(text, delay=0.1):
    with lock:
        for char in text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    lyrics = [
        ("\nOne, eight, zero, zero, he's so handsome, he's my hero", 0.01),
        ("One, eight, zero, zero", 0.06),
        ("it's that 1-800, hit my line", 0.06),
        ("One, eight, zero, zero, he's so handsome, he's my hero\n", 0.6),
        ("One, eight, zero, zero", 0.06),
        ("let me 1-800, blow your mind", 0.05),
    ]
    
    delays = [0.2, 0.2, 0.2, 0.1, 0.3, 0.3,]
    
    threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        threads.append(t)
        t.start()
    
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
