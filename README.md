# 🖼️ Steganography Project

This project is a Python-based application that allows users to hide secret messages inside images and extract them later. It provides both a command-line interface and an optional GUI for easy use, ensuring messages are stored covertly without visibly altering the original image.

---

## ✨ Features

- 📂 Encode secret text into images (supports PNG, JPG)  
- 🔓 Decode hidden messages from images  
- 🖌️ Optional GUI using Tkinter for easy interaction  
- 🌐 Supports Unicode messages  
- 🛠️ Uses all RGB channels for maximum storage capacity  
- ⏹️ Stops decoding automatically when delimiter is detected  

---

## 🛠️ Tech Stack

- **Python 3.10+**  
- **Pillow (PIL)** for image processing  
- **Tkinter** for GUI interface  
- **OpenStego** (explored as an external steganography tool)  

---

## 🚀 How It Works

- **Encode:** User selects an image and a text message. The message is embedded into the image using the least significant bit (LSB) technique.  
- **Decode:** User selects the stego image to extract the hidden message. Decoding stops automatically when the delimiter is reached.  
- **GUI:** Provides file pickers for images and messages, buttons for Encode/Decode, and a text box to display extracted messages.  

---

## 📂 Project Structure

STEGA/
├── docs/
│ └── read.me
├── input_images/
│ ├── Cat.jpg
│ └── madhuri_demo.txt
├── outputs/
│ └── Cat_secret.png
└── src/
├── stego.py
└── stego_gui.py

## 🔑 Security

- Messages are hidden within images, making them invisible to the naked eye  
- Supports Unicode and ensures complete retrieval of hidden messages  
- Can stop extraction automatically to prevent reading extra unintended data  

## 🎯 Use Cases

- Securely transmit messages without drawing attention  
- Educational tool to learn steganography techniques  
- Demonstration of practical image-based cryptography 