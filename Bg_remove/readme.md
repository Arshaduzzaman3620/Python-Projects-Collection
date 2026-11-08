# Background Remover — Natural White Background with Soft Shadow

A Python script that removes the background from a photo and replaces it with a natural-looking white background and a soft shadow, for a realistic, professional result.

Useful for:
- Profile photos
- Passport/ID pictures
- Product shots for e-commerce

## Features

- File picker to choose any image (`.jpg`, `.jpeg`, `.png`, `.heic`)
- AI-powered background removal using `rembg`
- Clean white background with soft edges
- Optional soft shadow for a natural, 3D feel
- Output in HD `.jpg` format

## Install

```bash
python -m pip install --upgrade pip
pip install rembg pillow pillow-heif
```

## Usage

```bash
python bg_remover_white_bacground.py
```

A file picker opens — select an image. The processed result is saved next to the script as `<original-filename>_natural_white_bg.jpg`.
