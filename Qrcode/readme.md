# QR Code Generator

A small command-line script that generates a QR code from any text or URL.

## Features

- Generates a QR code from text or a URL
- Takes input as a command-line argument or an interactive prompt
- Configurable error correction, box size, and border via `qrcode.QRCode`
- Saves the result as a PNG image

## Requirements

- Python 3.x
- Required Python libraries:
  - `qrcode`
  - `pillow`

Install the required libraries using pip:

```bash
pip install qrcode pillow
```

## Usage

Run the script and pass the text or URL as an argument:

```bash
python generate_qr.py "https://example.com"
```

Or run it without an argument to be prompted for input:

```bash
python generate_qr.py
```

The QR code is saved as `qr.png` in the current directory.

## Project Structure

```
/Qrcode
├── generate_qr.py   # Script for generating QR codes
├── readme.md        # Project documentation
└── requirements.txt # Python dependencies
```
