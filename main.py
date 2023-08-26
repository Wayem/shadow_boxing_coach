import os
import os.path
import random
import time
from config import commands, min_interval, max_interval
from gtts import gTTS
from pydub import AudioSegment

def simplify_text(text):
    """Convert the given text to a simplified format suitable for filenames."""
    return ''.join(e for e in text if e.isalnum())

def speak(text):
    simplified_name = simplify_text(text)
    mono_filename = f"cache/{simplified_name}_mono.mp3"
    stereo_filename = f"cache/{simplified_name}.mp3"

    # If the stereo audio file doesn't exist, create it
    if not os.path.exists(stereo_filename):
        # If the mono audio file doesn't exist, generate it using gTTS
        if not os.path.exists(mono_filename):
            tts = gTTS(text=text, lang="en")
            tts.save(mono_filename)

        # Convert mono to stereo
        mono_audio = AudioSegment.from_mp3(mono_filename)
        stereo_audio = mono_audio.set_channels(2)
        stereo_audio.export(stereo_filename, format="mp3")
        os.remove(mono_filename)  # Optionally remove the mono file

    os.system(f"mpg321 {stereo_filename}")

def main():
    print("Shadow Boxing Assistant Started!")
    while True:
        command = random.choice(commands)
        speak(command)
        sleep_time = random.uniform(min_interval, max_interval)
        time.sleep(sleep_time)

if __name__ == "__main__":
    main()
