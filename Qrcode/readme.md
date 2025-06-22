# QR Code Generator and Reader

This project is a Python-based application for generating and reading QR codes. It allows users to create QR codes from text or URLs and decode QR codes to extract the embedded information.

## Features

- **QR Code Generation**: Create QR codes from text, URLs, or other data.
- **QR Code Reading**: Decode QR codes from images to retrieve the embedded information.
- **User-Friendly**: Simple and intuitive interface for both generating and reading QR codes.
- **Customizable**: Customize the size, color, and error correction level of generated QR codes.

## Requirements

- Python 3.x
- Required Python libraries:
  - `qrcode`
  - `pillow`
  - `opencv-python`

You can install the required libraries using pip:

```bash
pip install qrcode pillow opencv-python
```

## Usage

### QR Code Generation

1. Run the script for generating QR codes.
2. Enter the text or URL you want to encode.
3. The QR code will be saved as an image file in the specified directory.

Example code snippet for generating a QR code:

```python
import qrcode

data = "https://example.com"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode.png")
```

### QR Code Reading

1. Run the script for reading QR codes.
2. Provide the path to the QR code image.
3. The decoded information will be displayed.

Example code snippet for reading a QR code:

```python
import cv2

image_path = "qrcode.png"
img = cv2.imread(image_path)
detector = cv2.QRCodeDetector()

data, vertices_array, _ = detector.detectAndDecode(img)
if vertices_array is not None:
    print("Decoded Data:", data)
else:
    print("QR Code not detected")
```

## Project Structure

```
/Qrcode
├── generate_qrcode.py  # Script for generating QR codes
├── read_qrcode.py      # Script for reading QR codes
├── qrcode.png          # Example QR code image
└── readme.md           # Project documentation
```



