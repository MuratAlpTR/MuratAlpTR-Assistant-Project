import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import playsound
from gtts import gTTS
import webbrowser
import os
import random
import datetime

r = sr.Recognizer()
engine = pyttsx3.init()

def konuş(text):
    engine.say(text)
    engine.runAndWait()

def konuş(yazı):
    tts = gTTS(text = yazı, lang= "tr")
    dosya_ismi = "ses"+ str(random.randint(0,1000000000000000000000)) + ".M4A"
    tts.save(dosya_ismi)
    playsound.playsound(dosya_ismi)

def sesi_kaydet():

    with sr.Microphone() as kaynak:
        ses = r.listen(kaynak)
        print('Dinleniyor...')

        söylenen_cümle = ""

        try:
            söylenen_cümle = r.recognize_google(ses, language="Tr-tr")
            print(söylenen_cümle)

        except Exception:
            konuş("söylediğin cümleyi anlayamadım")

    return söylenen_cümle


if __name__=="__main__" :    
    konuş('Murat Alp hizmetinizde. Lütfen bugün size nasıl yardımcı olabilirim?')

while True:
    yazı = sesi_kaydet()
    if "nasılsın" in yazı:
        konuş("iyiyim sen nasılsın")
      
    if "Merhaba" in yazı:
        konuş("merhaba")
    
    if "naber" in yazı:
        konuş("iyi sende naber")

    if "nasılsın" in yazı:
        konuş("iyiyim teşekkür ederim sende nasılsın")

    if "ince" in yazı or "direk" in yazı:
        konuş("İyi olduğunu bilmek güzel.")

    if "Ben Kimim" in yazı or "Alp Kim" in yazı:
        konuş("Eğer konuşursan o zaman kesinlikle insanın")

    if "seni seviyorum" in yazı:
        konuş("Bunu anlamak zor")
    
    if "gerizekalı" in yazı or  "gerızekalı" in yazı:
        konuş("sensin gerizekalı")
    
    if "geri zekalı" in yazı or  "mal mısın" in yazı:
        konuş("terbiyesiz herif")

    if "Ne yapıyorsun" in yazı:
        konuş("Seninle olmak, eğer etrafımda beni istiyorsan")

    if "Delik" in yazı or "Sıkılmış hissetmek" in yazı:
        konuş("Pekala, şaka yapabilirim o zaman") 

    if "Aşk Nedir" in yazı or "Aşk ne demek" in yazı:
        konuş("Diğer tüm duyuları yok eden 7. duyudur")

    if "Sen kimsin" in yazı:
        konuş("Ben Murat Alp tarafından yaratılan kişisel asistanınızım ")

    if "Sebep" in yazı or  "sebep" in yazı:
        konuş("Usta Murat Alp tarafından büyük bir proje olarak yaratıldım") 

    if "Neden dünyaya geldin" in yazı or "neden dünyaya geldin" in yazı:
        konuş("Murat Alp'a teşekkürler, dahası Bu bir sır")

    if "Seni kim yaptı" in yazı or "seni kim yarattı" in yazı:
        konuş("Murat Alp tarafından yaratıldım.")

    if "Başaramadık abi" in yazı or "başaramadık" in yazı:
        konuş("Neyi başaramadın Amına Goyım ")

    if "ahahahahaha" in yazı or "hahahahahaha" in yazı or "ahahaha" in yazı:
        konuş("Gülme Oğlım Şerefsiz")

    if "ahlaksız Robot" in yazı or "ahlaksız robot" in yazı or "ahlaksız adam" in yazı or "ahlaksız" in yazı:
        konuş("Alçak puşt")

    if "terbiyesiz" in yazı:
        konuş("Alçak puşt") 

    if "Günaydın" in yazı:
        konuş("Sıcak" + yazı)
        konuş("Nasılsın efendim")

    if "öğleden sonra" in yazı:
        konuş("Efendim" + yazı)
        konuş("Nassılsınız efendim")

    if "Akşam" in yazı:
        konuş("Efendim" + yazı)
        konuş("Nasılsınız efendim")

    if "Gece" in yazı:
        konuş("Efendim" + yazı)
        konuş("İyi uykular")

    if "mustafa kemal atatürk kimdir" in yazı:
        konuş("Mustafa Kemal Atatürk Türkiye cumhuriyetinin kurucusu Ve Büyük Önderidir")
    
    if "saat kaç" in yazı:
        konuş(datetime.now().strftime("%H:%M:%S"))

    if "Kim bu" in yazı:
        konuş("Aranıyor")
        yazı = yazı.replace("Wikipedia","")
        results = wikipedia.summary(yazı,sentences=1)
        konuş(results)

    if "Müzik çal" in yazı or "müzik çal" in yazı:
        songs_dir = 'C:/Users/AlpCoffee/Desktop/Müzik'
        music = os.listdir(songs_dir)
        os.startfile(os.path.join(songs_dir,music[0]))

    if "Erik Dalı" in yazı or "erik Dalı" in yazı or "erik dalı " in yazı or "erik dalı" in yazı or "Erik Dalı Çal" in yazı or "Sendemi Oldun Ankaralı" in yazı or "Sendemi oldun ankaralı" in yazı or "Sendemi Oldun Ankaralı çal" in yazı:
            konuş("İşte Youtube'a gidiyorsun\n")
            webbrowser.open("https://www.youtube.com/watch?v=P6KTCcdLZAE")

    if "Müzik aç" in yazı or "müzik aç" in yazı or "Müzik açarmısın" in yazı:
            konuş("Müzik giriyoruz\n")
            webbrowser.open("https://open.spotify.com/playlist/0BQeHBftguFuQAtx4kteDr?si=8267616df7994c76")

    if "Alp" in yazı:
            yazı = yazı.replace("Alp","")
            print(yazı)
