import requests
import os

# GitHub Secrets'tan anahtarı alıyoruz
API_KEY = os.environ.get("ELEVENLABS_API_KEY")

if not API_KEY:
    print("HATA: ELEVENLABS_API_KEY bulunamadı. Lütfen GitHub Secrets'a ekle.")
    exit()

# Adam isimli, çok derin ve sinematik bir erkek sesi kullanıyoruz (Voice ID)
VOICE_ID = "nPczCjzI2devNBz1zQrb" 

url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": API_KEY
}

# AI'ın okuyacağı metin. Üç nokta (...) koyarsan nefes alır ve duraklar.
data = {
  "text": " Bu durum, piyasa analistleri tarafından AI teknolojisinin potansiyeline olan inancın azaldığı anlamına gelmeyip, aksine daha sağlıklı ve sürdürülebilir bir büyüme evresine geçişin bir göstergesi olarak yorumlanmaktadır.",
  "model_id": "eleven_multilingual_v2",
  "voice_settings": {
    "stability": 0.4, # Düşük tutarsan daha duygulu ve değişken okur
    "similarity_boost": 0.8
  }
}

print("ElevenLabs stüdyoya girdi, kayıt başlıyor...")
response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    with open('gercek_vokal.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    print("Mükemmel! gercek_vokal.mp3 hazır.")
else:
    print("Hata oluştu:", response.text)
