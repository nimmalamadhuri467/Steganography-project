from PIL import Image
import argparse

MARKER = "#####END#####"


def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)


def bits_to_text(bits):
    chars = [bits[i:i+8] for i in range(0, len(bits), 8)]
    return ''.join(chr(int(c, 2)) for c in chars if len(c) == 8)


def encode(img_path, msg, output_path):
    img = Image.open(img_path)
    binary_msg = text_to_bits(msg + MARKER)
    pixels = list(img.getdata())

    new_pixels = []
    idx = 0
    for r, g, b in pixels:
        if idx < len(binary_msg):
            r = (r & ~1) | int(binary_msg[idx])
            idx += 1
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(output_path)
    print(f"[✅] Message hidden in {output_path}")


def decode(img_path):
    img = Image.open(img_path)
    pixels = list(img.getdata())
    binary_msg = ""

    for r, g, b in pixels:
        binary_msg += str(r & 1)

        # Process only when we have a full byte
        if len(binary_msg) % 8 == 0:
            current_text = bits_to_text(binary_msg)
            if MARKER in current_text:
                hidden_msg = current_text.split(MARKER)[0]
                return hidden_msg

    return "[❌] No hidden message found."


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Steganography Tool")
    parser.add_argument("mode", choices=["encode", "decode"], help="Choose mode: encode or decode")
    parser.add_argument("--input", required=True, help="Input image path")
    parser.add_argument("--output", help="Output image path (only for encode)")
    parser.add_argument("--message", help="Message to hide (only for encode)")

    args = parser.parse_args()

    if args.mode == "encode":
        if not args.output or not args.message:
            print("❌ For encode: --output and --message are required")
        else:
            encode(args.input, args.message, args.output)

    elif args.mode == "decode":
        hidden_msg = decode(args.input)
        print(f"[🔎] Hidden message: {hidden_msg}")
