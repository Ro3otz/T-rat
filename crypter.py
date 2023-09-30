import base64

dosya_adı = input("Base64 olarak kodlamak istediğiniz dosyanın adını girin: ")

try:
    with open(dosya_adı, "rb") as dosya:
        dosya_icerik = dosya.read()
    base64_icerik = base64.b64encode(dosya_icerik).decode("utf-8")
    print("Base64 Kodlanmış İçerik:")
    print(base64_icerik)

except FileNotFoundError:
    print(f"{dosya_adı} adında bir dosya bulunamadı.")
except Exception as e:
    print(f"Bir hata oluştu: {e}")
