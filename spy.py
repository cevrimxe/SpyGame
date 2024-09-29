import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Oyuncu listesi ve ülke listesi
oyuncular = ["oyuncu1@example.com", "oyuncu2@example.com", "oyuncu3@example.com", "oyuncu4@example.com"]
# Oynamak istediğiniz konuya bağlı olarak içeriği güncelleyebilirsiniz.
ulkeler = [
    "Amerika Birleşik Devletleri", "Çin", "Japonya", "Almanya", "Birleşik Krallık", 
    "Fransa", "İtalya", "Kanada", "Rusya", "Brezilya", "Hindistan", "Meksika", 
    "Avustralya", "İspanya", "Hollanda", "İsviçre", "Güney Kore", "Türkiye", 
    "Suudi Arabistan", "İsveç", "Arjantin", "Norveç", "Belçika", "Danimarka", 
    "İsrail", "Güney Afrika", "Endonezya", "Polonya", "Malezya", "Singapur", 
    "İrlanda", "Yeni Zelanda", "Portekiz", "Çek Cumhuriyeti", "Avusturya", 
    "Finlandiya", "Yunanistan", "Macaristan", "Tayland", "Filipinler", "Mısır"
]

# Rastgele ülke seçimi
secilen_ulke = random.choice(ulkeler)

# Rastgele ajan seçimi
ajan_index = random.randint(0, len(oyuncular) - 1)

# Mail gönderim fonksiyonu
def mail_gonder(alici, konu, mesaj):
    fromaddr = "gönderici mail adresi"
    toaddr = alici
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = konu

    body = mesaj
    msg.attach(MIMEText(body, 'plain'))

    # Mail sunucusu ayarları
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "sifre")  # https://youtu.be/ueqZ7RL8zxM?t=116 Bu videodaki adımları takip ederek mail adresiniz için kullanacağınız şifreyi alabilirsiniz.
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

# Oyunculara mesajları gönder
for i, oyuncu in enumerate(oyuncular):
    if i == ajan_index:
        mesaj = "Siz AJAN'sınız! Ülke bilgisi yok."
    else:
        mesaj = f"Ülkeniz: {secilen_ulke}"
    
    mail_gonder(oyuncu, "Oyun Bilgilendirmesi", mesaj)

print("Tüm oyunculara mail gönderildi.")
