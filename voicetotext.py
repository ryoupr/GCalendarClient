from unicodedata import bidirectional
import speech_recognition as sr
import PySimpleGUI as sg


def voicetotext():
    layout = [
        []
    ]
    voicereqwindow = sg.Window(
        'Recording...', layout, finalize=True, background_color='#FFFFFF', size=(235, 0))

    r = sr.Recognizer()
    with sr.Microphone() as input:
        print("録音中:")
        audio = r.listen(input)

    text = r.recognize_google(audio, language='ja-JP')

    voicereqwindow.close()
    return text


if __name__ == '__main__':
    print(voicetotext())
