from gtts import gTTS
import os
text = input("write something: ")
language = 'en'
tts = gTTS(text=text, lang=language, slow=False)
tts.save("hello.mp3")
    # To play the audio (requires a player like playsound or os.startfile on Windows)
    # os.system("start hello.mp3") # For Windows
    # from playsound import playsound
    # playsound("hello.mp3")