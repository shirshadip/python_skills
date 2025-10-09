import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set voice properties
engine.setProperty('rate', 120)      # Speed of speech
engine.setProperty('volume', 1.0)    # Volume (0.0 to 1.0)

# Get available voices
voices = engine.getProperty('voices')

# Change voice (0 for male, 1 for female - depends on system)
engine.setProperty('voice', voices[1].id)

# Speak the text
text=input ("enter something you want to convert into speech")
engine.say(text)
engine.runAndWait()
