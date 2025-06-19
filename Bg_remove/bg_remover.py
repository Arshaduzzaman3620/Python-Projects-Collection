from rembg import remove
from PIL import Image, ImageFilter, ImageEnhance
from tkinter import filedialog, Tk
import os

# === Step 1: Choose an image file ===
root = Tk()
root.withdraw()
input_path = filedialog.askopenfilename(
    title="Select an image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png")]
)

if not input_path:
    print("❌ No file selected.")
    exit()

filename = os.path.basename(input_path)
name, _ = os.path.splitext(filename)
output_path = f"{name}_natural_white_bg.jpg"

# === Step 2: Remove the background ===
with open(input_path, 'rb') as input_file:
    input_data = input_file.read()
    output_data = remove(input_data)

with open("transparent.png", 'wb') as out_file:
    out_file.write(output_data)

# === Step 3: Open and process the transparent image ===
image = Image.open("transparent.png").convert("RGBA")

# Create a clean white background
white_bg = Image.new("RGBA", image.size, (255, 255, 255, 255))

# === Step 4: Optional shadow for realism ===
shadow = image.copy().convert("RGBA")
shadow = shadow.filter(ImageFilter.GaussianBlur(3))
shadow = ImageEnhance.Brightness(shadow).enhance(0.3)

# Paste shadow first, slightly offset for natural effect
white_bg.paste(shadow, (5, 5), shadow)

# === Step 5: Slight blur on image for smooth edges ===
image_blurred = image.filter(ImageFilter.GaussianBlur(radius=0.5))

# Paste original image on top of white + shadow
white_bg.paste(image_blurred, (0, 0), image)

# === Step 6: Final conversion and save ===
final_image = white_bg.convert("RGB")
final_image.save(output_path, "JPEG", quality=100)

print(f"✅ Background removed with natural white finish. Saved as: {output_path}")
