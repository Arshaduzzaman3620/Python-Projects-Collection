from rembg import remove
from PIL import Image, ImageFilter, ImageEnhance
from pillow_heif import register_heif_opener
from tkinter import filedialog, Tk
import os

# === Step 0: Register HEIC support ===
register_heif_opener()  # now Pillow can open HEIC images

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
output_path = f"{name}_natural_white_bg.jpg"

# === Step 2: Open image and remove background ===
try:
    image = Image.open(input_path).convert("RGBA")
    image_no_bg = remove(image)  # works directly with PIL Image
except Exception as e:
    print("❌ Error removing background:", e)
    exit()

# === Step 3: Create white background ===
white_bg = Image.new("RGBA", image_no_bg.size, (255, 255, 255, 255))

# Optional shadow for realism
shadow = image_no_bg.copy().convert("RGBA")
shadow = shadow.filter(ImageFilter.GaussianBlur(3))
shadow = ImageEnhance.Brightness(shadow).enhance(0.3)
white_bg.paste(shadow, (5, 5), shadow)

# Slight blur on image edges
image_blurred = image_no_bg.filter(ImageFilter.GaussianBlur(radius=0.5))

# Paste original image
white_bg.paste(image_blurred, (0, 0), image_no_bg)

# Final conversion and save
final_image = white_bg.convert("RGB")
final_image.save(output_path, "JPEG", quality=100)

print(f"✅ Background removed with natural white finish. Saved as: {output_path}")
