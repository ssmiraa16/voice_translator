import speech_recognition
import pyttsx3
rec = speech_recognition.Recognizer()
mic = speech_recognition.Microphone()
voice = pyttsx3.init()
def talk(string):
    voice.say(string)
    voice.runAndWait()
with mic as source:
    print('Говорите...')
    rec.pause_threshold = 1
    rec.adjust_for_ambient_noise(source, duration = 1)
    audio = rec.listen(source)
    print('Секундочку...')
    text = rec.recognize_google(audio, language='ru-RU')
    text = text. capitalize()
    print('Вы сказали:', text)
    talk(text)
from translate import Translator
t = Translator(from_lang = "ru", to_lang = "en")
etext = t.translate(text)
print('Перевод на английский:', etext)