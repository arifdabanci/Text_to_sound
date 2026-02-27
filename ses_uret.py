import asyncio
import edge_tts

# Yapay zekanın okuyacağı metin
METIN = """
Sistemler aktif. RoboAI Cafe otonom moduna geçiş yaptı. 
İnsan hatası sıfıra indirildi. Verimlilik maksimum seviyede. 
Geleceğin işletmesine hoş geldiniz.
"""

# Kullanılacak Ses (Ahmet veya Emel seçilebilir)
SES = "tr-TR-AhmetNeural" 
DOSYA_ADI = "roboai_vokal.mp3"

async def main():
    print("Yapay zeka sesi sentezliyor...")
    communicate = edge_tts.Communicate(METIN, SES)
    await communicate.save(DOSYA_ADI)
    print(f"Başarılı! {DOSYA_ADI} dosyası oluşturuldu.")

if __name__ == "__main__":
    asyncio.run(main())
