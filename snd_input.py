#!/usr/bin/env python3

import numpy as np
import pygame
import sounddevice as sd

# CONFIG
SLEEP_DURATION = 10         # seconds, need not modify
MULTIPLIER = 10             # resolution, basically
THRESHOLD = 8               # after multiplication
SOUND_FILE = "ringout.wav"  # sound to play if threshold is reached
# END OF CONFIG

def print_sound(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * MULTIPLIER
    
    if volume_norm > THRESHOLD:
        print("#" * int(volume_norm))
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
    else:
        print("=" * int(volume_norm))

if __name__ == "__main__":
    pygame.mixer.init()
    pygame.mixer.music.load(SOUND_FILE)
    
    with sd.InputStream(callback=print_sound):
        try:
            while True:
                sd.sleep(SLEEP_DURATION * 1000)
        except KeyboardInterrupt:
            pass
