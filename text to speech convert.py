from gtts import gTTS
import os

# Text to be converted to speech
text = "भारत हा जगातील ७व्या क्रमांकाचा देश आहे. भारत आशिया खंडात स्थित आहे. भारत हा एक महान देश आहे, जिथे अनेक संत आणि महात्म्यांनी जन्म घेतला आहे. १५ ऑगस्ट १९४७ रोजी भारत ब्रिटिश राजवटीपासून स्वतंत्र झाला."

# Initialize the gTTS object with the text and language
tts = gTTS(text, lang='mr')

# Save the speech as an audio file
tts.save("output.mp3")

# Play the generated audio file (works on Windows)
os.system("start output.mp3")
