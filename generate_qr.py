import qrcode

session_id = "session123"
url = f"https://your-domain.com/connect/{session_id}"  # Remplace par ton domaine réel

qr = qrcode.make(url)
qr.save("qr_code.png")

print("QR code généré et sauvegardé dans qr_code.png")