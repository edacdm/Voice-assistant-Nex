import pyttsx3
import speech_recognition as sr
import webbrowser
from datetime import datetime
import os
import pycaw.pycaw as pycaw #laptobun sesini kısıp açmak için 


def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('voice', 'turkish')  # Türkçe ses seçimi
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Sizi dinliyorum...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Ses algılanıyor...")
        voice_input = recognizer.recognize_google(audio, language="tr-TR")
        print("Ses algılandı: ", voice_input)
        return voice_input.lower()
    except sr.UnknownValueError:
        print("Üzgünüm, anlayamadım.")
        return ""
    except sr.RequestError as e:
        print("Sistem çalışmıyor; {0}".format(e))
        return ""

#müzik açmak için seçim yapmayı sağlar
def play_music_platform():
    if "müzik açar mısın?":
     speak("Spotify'dan mı, YouTube'dan mı müzik açayım?")
    voice_input = listen()

    if voice_input:
        if "spotify" in voice_input:
            speak("Spotify açılıyor...")
            os.system("start spotify")# Spotify'ı açmak için gereken kod
           
        elif "youtube" in voice_input:
            speak("YouTube açılıyor...")
            url = "https://www.youtube.com/"# YouTube'u açmak için gereken kod
            
        else:
            speak("Anlaşılmadı.")

while True:
    voice_input = listen()
    if voice_input:
        if "müzik aç" in voice_input:
            play_music_platform()
        else:
            speak("Üzgünüm, anlaşılmadı.")
        break


#Google'dan arama yapar
def search_google(query):
    url = "https://www.google.com.tr/search?q=" + query
    webbrowser.get().open(url)

while True:
    voice_input = listen()
    if voice_input:
        if "arama yap" in voice_input:
            speak("Ne aramamı istiyorsun?")
            search_query = listen()
            if search_query:
                speak("Aranıyor: " + search_query)
                search_google(search_query)
                speak("İşte bulduklarım:")
                break

        #Şu anki saati söyler 
        if "saat kaç" in voice_input:
            current_time = datetime.now().strftime("%H:%M")
            speak("Şu anda saat " + current_time)
        else:
            speak("Üzgünüm, komut anlaşılamadı.")
            break



"""def camera():
    if "kamerayı aç":
     speak("Kamera açılıyor...")
     os.system("start camera") #Kamerayı açmak için gereken kod

    elif "kamerayı kapat":
        speak("Kamera kapatılıyor...") #Kamerayı kapatmak için gereken kod
        os.system("stop camera")
        #bunda hata vermiyor ama kodu çalıştırmıyor 
        #derlemede problem yok ama kod eksik veya çalışmıyor
    """