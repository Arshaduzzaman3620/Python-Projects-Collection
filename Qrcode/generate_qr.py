import sys

import qrcode

data = sys.argv[1] if len(sys.argv) > 1 else input("Enter text or a URL to encode: ")

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")

print("Saved as qr.png")
