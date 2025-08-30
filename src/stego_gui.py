import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

# ---------- Encoding ----------
# ---------- Encoding ----------
def encode_message(img_path, message, output_path):
    img = Image.open(img_path)
    encoded = img.copy()
    width, height = img.size
    message_bytes = (message + "%%END%%").encode('utf-8')
    bits = ''.join([format(byte, '08b') for byte in message_bytes])
    index = 0

    for row in range(height):
        for col in range(width):
            if index >= len(bits):
                break
            r, g, b = img.getpixel((col, row))
            new_rgb = []
            for color in (r, g, b):
                if index < len(bits):
                    color = (color & ~1) | int(bits[index])
                    index += 1
                new_rgb.append(color)
            encoded.putpixel((col, row), tuple(new_rgb))
        if index >= len(bits):
            break

    encoded.save(output_path)
    return output_path

# ---------- Decoding ----------
def decode_message(img_path):
    img = Image.open(img_path)
    width, height = img.size
    bits = ""
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            for color in (r, g, b):
                bits += str(color & 1)

    # Convert bits to bytes until delimiter is found
    message_bytes = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            break
        message_bytes.append(int(byte, 2))
        if bytes(message_bytes[-6:]).decode('utf-8', errors='ignore') == "%%END%%":
            break

    try:
        message = bytes(message_bytes).decode('utf-8')
        return message.split("%%END%%")[0]
    except:
        return "Decoding error!"


# ---------- Decoding ----------
def decode_message(img_path):
    img = Image.open(img_path)
    width, height = img.size
    bits = ""
    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            bits += str(r & 1)

    # Convert bits to bytes
    message_bytes = []
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            continue
        message_bytes.append(int(byte, 2))

    try:
        message = bytes(message_bytes).decode('utf-8')
        return message.split("%%END%%")[0]
    except:
        return "Decoding error!"

# ---------- GUI Functions ----------
def browse_image():
    filepath = filedialog.askopenfilename(
        title="Select Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")]
    )
    if filepath:
        entry_image.delete(0, tk.END)
        entry_image.insert(0, filepath)

def encode_action():
    img_path = entry_image.get()
    message = text_message.get("1.0", tk.END).strip()
    if not img_path or not message:
        messagebox.showerror("Error", "Please select image and enter message")
        return

    output_path = os.path.join(os.path.dirname(img_path), "encoded_output.png")
    encode_message(img_path, message, output_path)
    messagebox.showinfo("Success", f"Message encoded and saved as:\n{output_path}")

def decode_action():
    img_path = entry_image.get()
    if not img_path:
        messagebox.showerror("Error", "Please select an encoded image")
        return

    message = decode_message(img_path)
    text_message.delete("1.0", tk.END)
    text_message.insert(tk.END, message)

# ---------- GUI Layout ----------
root = tk.Tk()
root.title("Steganography - Unicode Safe")
root.geometry("600x400")

# Image input
frame1 = tk.Frame(root)
frame1.pack(pady=10)
tk.Label(frame1, text="Image File:").pack(side=tk.LEFT, padx=5)
entry_image = tk.Entry(frame1, width=50)
entry_image.pack(side=tk.LEFT, padx=5)
tk.Button(frame1, text="Browse", command=browse_image).pack(side=tk.LEFT)

# Message box
tk.Label(root, text="Secret Message:").pack()
text_message = tk.Text(root, height=10, width=60)
text_message.pack(pady=5)

# Buttons
frame2 = tk.Frame(root)
frame2.pack(pady=10)
tk.Button(frame2, text="Encode", command=encode_action, width=15).pack(side=tk.LEFT, padx=20)
tk.Button(frame2, text="Decode", command=decode_action, width=15).pack(side=tk.LEFT, padx=20)

root.mainloop()
