from rembg import remove
from PIL import Image
from pillow_heif import register_heif_opener
from tkinter import filedialog, Tk
import os

# === Step 0: Register HEIC support ===
register_heif_opener()  # now Pillow can open HEIC files

# === Step 1: Choose an image file ===
root = Tk()
root.withdraw()
input_path = filedialog.askopenfilename(
    title="Select an image", filetypes=[("Image files", "*.jpg *.jpeg *.png *.heic")]
)

if not input_path:
    print("❌ No file selected.")
    exit()

filename = os.path.basename(input_path)
name, _ = os.path.splitext(filename)
output_path = f"{name}_transparent.png"

# === Step 2: Open image and remove background ===
try:
    image = Image.open(input_path).convert("RGBA")
    image_no_bg = remove(image)  # remove background
except Exception as e:
    print("❌ Error removing background:", e)
    exit()

# === Step 3: Save transparent PNG ===
image_no_bg.save(output_path, "PNG")
print(f"✅ Background removed! Saved as: {output_path}")
