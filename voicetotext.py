import speech_recognition as sr

def voicetotext():
    r = sr.Recognizer()
    with sr.Microphone() as input:
        print("録音中:")
        audio = r.listen(input)
    text = r.recognize_google(audio, language='ja-JP')
    return text

if __name__ == '__main__':
    print(voicetotext())
