import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as input:
    print("録音中:")
    audio = r.listen(input)

text = r.recognize_google(audio, language='ja-JP')
