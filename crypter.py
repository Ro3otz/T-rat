import base64

dosya_adı = input("File: ")

try:
    with open(dosya_adı, "rb") as dosya:
        dosya_icerik = dosya.read()
    base64_icerik = base64.b64encode(dosya_icerik).decode("utf-8")
    print("Base64:")
    print(base64_icerik)

except FileNotFoundError:
    print(f"{dosya_adı} Cant find")
except Exception as e:
    print(f"Error: {e}")
