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
  "text": """
GLOBAL AI & OTOMASYON VİZYONU
Bugünün Araştırma Odağı: ARTIFICIAL INTELLIGENCE BUSINESS OPPORTUNITIES

The Artificial Intelligence (AI) Software Sell-Off Created a Rare Buying Opportunity. Here Are 3 Stocks to Grab in 2026.
Haberin Orijinal Kaynağına Git

Kapsamlı Özet
Küresel piyasalarda yapay zeka (AI) yazılım şirketlerinin hisselerinde yaşanan son düşüş, uzun vadeli yatırımcılar için nadir bir alım fırsatı olarak değerlendirilmektedir. Başlıkta belirtilen haber, AI sektöründeki hızlı büyüme ve ardından gelen doğal düzeltmenin, spekülatif değerlemeleri törpüleyerek gerçek değer arayan yatırımcılar için cazip giriş noktaları yarattığını vurgulamaktadır. Bu durum, piyasa analistleri tarafından AI teknolojisinin potansiyeline olan inancın azaldığı anlamına gelmeyip, aksine daha sağlıklı ve sürdürülebilir bir büyüme evresine geçişin bir göstergesi olarak yorumlanmaktadır.

İş Fikri Olarak Fırsatlar (Upside)
Niş Pazar Odaklı AI Çözümleri: Yapay zeka yazılım sektöründeki genel düzeltme, henüz tam anlamıyla AI ile dönüştürülmemiş veya mevcut çözümlerin yetersiz kaldığı niş pazarlarda büyük bir boşluk yaratmaktadır. Bu alanlarda derinlemesine uzmanlık ile geliştirilecek AI yazılımları, yüksek kârlılık potansiyeline sahiptir.
AI Entegrasyon ve Adaptasyon Hizmetleri: Birçok şirket AI teknolojilerini benimsemeye hevesli olsa da, karmaşık entegrasyon süreçleri ve mevcut sistemlere adaptasyon konusunda zorluk yaşamaktadır. Girişimciler, şirketlere özel entegrasyon ve AI danışmanlığı sunan bir hizmet işi kurabilir.

Sektörel Riskler ve Kırılganlık (Downside)
Teknolojik Eskime ve Yüksek Ar-Ge Maliyeti: Yapay zeka sektörü, inanılmaz bir hızla gelişmektedir. Sınırlı sermayeli bir girişimci için, rekabetçi kalabilmek adına sürekli inovasyon yapmak büyük bir risk ve kırılganlık unsurudur.

Yatırım ve Aksiyon Stratejisi
Vizyoner bir girişimci için bu AI yazılımındaki "satış düşüşü", bir panik değil, aksine uzun vadeli stratejik bir giriş fırsatı sunar. Nassim Taleb'in Lindy Etkisi felsefesini benimseyerek, temel insan ihtiyaçlarına yönelik çözümler sunan alanlara odaklanmak akıllıca olacaktır.

How Small Businesses Can Capitalize on Their Artificial Intelligence Opportunities

Kapsamlı Özet
Yapay zeka, günümüzün en sıcak teknoloji yatırım alanlarından biri olarak öne çıkmaktadır. Uzmanlar, AI'nın küçük işletmeler için daha önce görülmemiş kapılar açtığını belirtiyor. En büyük faydalar, zaman alıcı ve tekrarlayan günlük görevlerin otomatikleştirilmesinde yatmaktadır.

İş Fikri Olarak Fırsatlar (Upside)
AI-as-a-Service (AIaaS) ve Mikro-Entegrasyon Çözümleri: Küçük işletmelerin spesifik, tekrarlayan sorunlarına odaklanan, uygun fiyatlı AI çözümleri sunmak büyük bir pazar boşluğudur.
AI Köprüleri ve Eğitim/Danışmanlık Hizmetleri: İşletmeleri AI teknolojisinin karmaşıklığından koruyarak, yalnızca somut iş değeri yaratacak çözümlere yönlendirmeyi ve kullanım eğitimlerini içerir.

Sektörel Riskler ve Kırılganlık (Downside)
Hype Döngüsü ve Güven Kırılganlığı: Eğer sunulan AI çözümleri vaat edilen somut getiriyi sağlamazsa, küçük işletmelerin AI'ya olan güveni hızla sarsılabilir.

Yatırım ve Aksiyon Stratejisi
Küçük işletmelerin kanıtlanmış, kadim sorunlarına odaklanan AI uygulamalarına öncelik verilmelidir. Kendi AI araçlarını sıfırdan geliştirmek yerine, AI danışmanlığı ve entegrasyonu modeliyle sürdürülebilir bir iş modeli oluşturmayı hedefler.

This Artificial Intelligence (AI) Innovator Could Be Sitting on a $100 Billion Opportunity That Could Send Shares Soaring 67%

Kapsamlı Özet
Makale, SoundHound AI şirketinin, sesli yapay zeka teknolojileriyle 100 milyar dolarlık devasa bir pazar fırsatına sahip olabileceğini vurgulamaktadır. Şirketin teknolojisi, özellikle sipariş alma, müşteri hizmetleri ve bilgi sağlama gibi süreçleri otomatize ederek işletmelerin verimliliğini artırmayı hedeflemektedir.

İş Fikri Olarak Fırsatlar (Upside)
Otomasyon ve Verimlilik Artışı: Sesli yapay zeka, insan gücüne dayalı süreçleri dönüştürerek işletmeler için önemli maliyet tasarrufu sağlayabilir.
Özelleştirilmiş ve Ölçeklenebilir Çözümler: Sektöre özel sesli arayüzler ve etkileşim modelleri geliştirme potansiyeli bulunmaktadır.

Sektörel Riskler ve Kırılganlık (Downside)
Yoğun Rekabet ve Teknolojik Eskime Hızı: Sesli yapay zeka alanı dev teknoloji şirketlerinin yanı sıra sayısız startup ile doludur.
Yüksek AR-GE Maliyeti ve Karmaşıklık: Dünya standartlarında bir çözüm geliştirmek astronomik maliyetlere ulaşabilir.

Yatırım ve Aksiyon Stratejisi
Genel amaçlı, geniş pazarlara odaklanmak yerine, dikey bir nişte uzmanlaşmak kritik öneme sahiptir. Özelleşmiş bir sektördeki belirli, çözülmemiş bir soruna odaklanarak benzersiz veri setleri ve domain bilgisi geliştirmelidir.
""",
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
